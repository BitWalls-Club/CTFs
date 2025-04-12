from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

load_dotenv()

# Only allow access if user is "admin"
def is_admin(user):
    return user.is_authenticated and user.username == "admin"

@login_required
@user_passes_test(is_admin)
def admin_panel(request):
    users = User.objects.all()
    
    # Load passwords from .env
    passwords = {
        'admin': os.getenv('ADMIN_PASSWORD'),
        'user1': os.getenv('USER1_PASSWORD'),
        'user2': os.getenv('USER2_PASSWORD'),
        'user3': os.getenv('USER3_PASSWORD'),
    }

    return render(request, 'admin_panel.html', {
        'users': users,
        'passwords': passwords
    })
