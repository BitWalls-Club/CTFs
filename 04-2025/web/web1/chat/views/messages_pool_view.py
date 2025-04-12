from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chat.models import Messages

@login_required(login_url="login")
def messages_pool(request):
    if request.user.username != "admin":
        return redirect("home")

    admin_user = request.user
    messages = Messages.objects.filter(receiver_name=admin_user).order_by("timestamp")

    return render(request, "messages_pool.html", {
        "messages": messages,
        "curr_user": admin_user
    })
