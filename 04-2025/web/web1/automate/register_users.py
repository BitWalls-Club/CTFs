import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'http://127.0.0.1:1337'

users = [
    ('admin', os.getenv('ADMIN_PASSWORD')),
    ('user1', os.getenv('USER1_PASSWORD')),
    ('user2', os.getenv('USER2_PASSWORD')),
    ('user3', os.getenv('USER3_PASSWORD')),
]

def register_user(username, password):
    url = f"{BASE_URL}/signup/"
    data = {
        'username': username,
        'password1': password,
        'password2': password,
    }

    session = requests.Session()
    res = session.get(url)  # Get CSRF token from signup page

    if 'csrftoken' in session.cookies:
        data['csrfmiddlewaretoken'] = session.cookies['csrftoken']
        headers = {'Referer': url}
        response = session.post(url, data=data, headers=headers)
        if "user" in response.url:
            print(f"[+] Registered: {username}")
        elif "already exists" in response.text:
            print(f"[-] Already exists: {username}")
        else:
            print(f"[!] Error registering {username}")
    else:
        print("[!] CSRF token not found. Signup page may have changed.")

for username, password in users:
    if password:
        register_user(username, password)
    else:
        print(f"[!] No password found for {username}")
