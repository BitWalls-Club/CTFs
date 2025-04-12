from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from chat.models import UserRelation
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import time
from django.utils import timezone
from channels.layers import get_channel_layer
from chat.models import Messages, UserRelation
import threading
from asgiref.sync import async_to_sync
import random

@login_required(login_url="login")
def delete_friend(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        try:
            print("starts")
            exists = UserRelation.objects.filter(user=user, friend=friend).exists()
            print("sts")
            if exists:
                pass
            else:
                return HttpResponseRedirect(
                    request.META.get("HTTP_REFERER", reverse("home"))
                )
            user_relation = UserRelation.objects.get(user=user, friend=friend)
            user_relation.delete()

            user_relation_reverse = UserRelation.objects.get(user=friend, friend=user)
            user_relation_reverse.delete()
            messages.success(request, "Friend deleted successfully.")

        except UserRelation.DoesNotExist:
            messages.success(request, "Request deleted successfully.")
            pass
        return redirect("home")
    else:
        return redirect("home")


@login_required(login_url="login")
def accept_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        accepted = True

        exists = UserRelation.objects.filter(user=user, friend=friend).exists()
        print("sts")
        if exists:
            return HttpResponseRedirect(
                request.META.get("HTTP_REFERER", reverse("home"))
            )
        relation_key = username + "_" + user.username
        user_relation = UserRelation(
            user=user, friend=friend, accepted=accepted, relation_key=relation_key
        )
        user_relation.save()

        user_relation_revrse = UserRelation.objects.get(user=friend, friend=user)
        user_relation_revrse.accepted = True
        user_relation_revrse.relation_key = relation_key
        user_relation_revrse.save()
        messages.success(request, "Friend Added successfully.")

        return redirect("home")
    else:
        return redirect("home")


@login_required(login_url="login")
def send_delayed_message(sender, receiver, message, delay):
    """Helper function to send a message after a delay"""
    def delayed_task():
        time.sleep(delay)
        # Create the message in the database
        msg = Messages.objects.create(
            sender_name=sender,
            receiver_name=receiver,
            description=message,
            time=timezone.now().time(),
            timestamp=timezone.now()
        )
        
        # Send WebSocket notification
        room_name = f"{min(sender.username, receiver.username)}_{max(sender.username, receiver.username)}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{room_name}',
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username
            }
        )
        return msg
    
    # Start the delayed task in a separate thread
    thread = threading.Thread(target=delayed_task)
    thread.daemon = True
    thread.start()

def add_friend(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        accepted = False
        
        # Check if relation already exists
        exists = UserRelation.objects.filter(user=user, friend=friend).exists()
        if exists:
            return HttpResponseRedirect(
                request.META.get("HTTP_REFERER", reverse("home"))
            )
        
        # Create the relation
        user_relation = UserRelation(user=user, friend=friend, accepted=accepted)
        user_relation.save()
        
        # Auto-accept if admin is the friend
        if friend.username == "admin":
            user_relation.accepted = True
            user_relation.save()
            starters = [
            "How can I help you, fellow internet explorer?",
            "You've summoned the almighty admin 😎",
            "Talk to me, goose.",
            "Welcome to the chat zone. Mind the bugs.",
            "What seems to be the problem, officer?",
            "Type your issue slowly, I'm old.",
            "This better not be a prank... 👀",
            "You're not here to Rickroll me, are you?",
            "Admin at your service. Coffee not included.",
            "Ready to pretend I know the answer. Go!"
            ]
            first_message = random.choice(starters)
            # Send initial "hello world" message immediately when user joins
            admin_msg = Messages.objects.create(
                sender_name=friend,
                receiver_name=user,
                description=first_message,
                time=timezone.now().time(),
                timestamp=timezone.now()
            )
            
            # Set up a listener for user messages to trigger subsequent admin responses
            def setup_message_listener():
                # Create a custom signal handler for new messages
                from django.db.models.signals import post_save
                from django.dispatch import receiver
                
                @receiver(post_save, sender=Messages)
                def on_message_created(sender, instance, created, **kwargs):
                    # Only respond to new messages from user to admin
                    if created and instance.sender_name == user and instance.receiver_name == friend:
                        # If this is the user's first message to admin, send "123"
                        user_msg_count = Messages.objects.filter(
                            sender_name=user,
                            receiver_name=friend
                        ).count()
                        
                        if user_msg_count == 1:  # This is the first message
                            # Send "123" after the user's first message
                            send_delayed_message(friend, user, "123", 0.5)  # Short delay for natural feel
                            
                            # Schedule "test" message to be sent 2 seconds after "123"
                            send_delayed_message(friend, user, "test", 2.5)  # 0.5s + 2s = 2.5s total delay
            
            # Set up the listener
            setup_message_listener()
            
        messages.success(request, "Request sent successfully.")
        return redirect("home")
    else:
        return redirect("home")
# def add_friend(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         user = request.user
#         friend = User.objects.get(username=username)
#         accepted = False
#         print("starts")
#         exists = UserRelation.objects.filter(user=user, friend=friend).exists()
#         print("sts")
#         if exists:
#             print("star")
#             return HttpResponseRedirect(
#                 request.META.get("HTTP_REFERER", reverse("home"))
#             )
#         # user_relation = UserRelation(user=user, friend=friend, accepted=accepted)
#         # user_relation.save()
#         user_relation = UserRelation(user=user, friend=friend, accepted=accepted)
#         user_relation.save()

#         # Auto-accept if admin is the friend
#         if friend.username == "admin":
#             user_relation.accepted = True
#             user_relation.save()

#             # Auto-send messages from admin to the requester
#             from chat.models import Messages
#             from django.utils import timezone

#             auto_messages = ["hello world", "123", "test"]
#             for i, text in enumerate(auto_messages):
#                 time.sleep(i + 1)  # 1s, 2s, 3s delay before each message
#                 Messages.objects.create(
#                     sender_name=friend,
#                     receiver_name=user,
#                     description=text,
#                     time=timezone.now().time(),
#                     timestamp=timezone.now()
#                 )
#         messages.success(request, "Request sended successfully.")

#         return redirect("home")
#     else:
#         return redirect("home")


@login_required(login_url="login")
def search(request):
    if request.method == "GET":
        query = request.GET.get("q", "")
        if query:
            users = User.objects.filter(username__icontains=query)
            if users:
                return render(
                    request,
                    "search.html",
                    {"query": query, "users": users, "user": request.user.username},
                )
            else:
                not_found_message = f'No users found for "{query}"'
                return render(
                    request,
                    "search.html",
                    {
                        "query": query,
                        "not_found_message": not_found_message,
                    },
                )

    return render(request, "search.html", {"user": request.user.username})

