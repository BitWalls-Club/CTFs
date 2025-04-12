import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from chat.utils import message_validation

@database_sync_to_async
def save_message(sender_name, receiver_name, message):
    from django.contrib.auth.models import User
    from chat.models import Messages
    # Get User instances for sender and receiver
    sender = User.objects.get(username=sender_name)
    receiver = User.objects.get(username=receiver_name)
    
    # Create a new message
    new_message = Messages(
        description=message,
        sender_name=sender,
        receiver_name=receiver,
        time=timezone.now().time(),  # Store the current time
        timestamp=timezone.now(),   # Store the timestamp
        seen=True
    )
    new_message.save()
    
    # Return if this is an admin message and the sender username
    return receiver.username == "admin", sender.username

class AdminMessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'admin_pool'
        
        # Join admin pool group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave admin pool group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        # This likely won't be used much, but included for completeness
        pass
    
    async def new_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'username': event['username'],
            'message': event['message']
        }))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_name = text_data_json['sender_name']
        receiver_name = text_data_json['receiver_name']
        
      
        if not  message_validation.is_safe_message(message):
            await self.send(text_data=json.dumps({
                'error': '⚠️ Message contains unsafe content and was blocked.'
            }))
            return

        is_admin_message, sender_username = await save_message(sender_name, receiver_name, message)
        
        if is_admin_message:
            await self.channel_layer.group_send(
                "admin_pool",
                {
                    'type': 'new_message',
                    'username': sender_username,
                    'message': message
                }
            )
        
        # Broadcast message to chat room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_name
            }
        )

    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))