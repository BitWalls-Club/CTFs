from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
import os
from dotenv import load_dotenv

load_dotenv()

# Only allow access if user is "admin"
def is_admin(user):
    return user.is_authenticated and user.username == "admin"

@login_required
@user_passes_test(is_admin)
def flag1(request):
    flag = os.getenv("FLAG1", "FLAG_NOT_SET")
    return HttpResponse(flag)
