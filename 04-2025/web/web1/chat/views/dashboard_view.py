from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Messages

def dashboard_index(request):
    user_count = User.objects.count()
    message_count = Messages.objects.count()

    return render(request, "statistics.html", {
        "user_count": user_count,
        "message_count": message_count,
    })
