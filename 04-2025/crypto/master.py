import socket
import jwt
import datetime
import threading
import os
from dotenv import load_dotenv

# Load FLAG from .env
load_dotenv()
FLAG = os.getenv("FLAG", "Error loading flag file")
SECRET_KEY = "supersecret123"  # Weak key

def generate_token(username, role="user"):
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def send_line(sock, msg):
    try:
        sock.sendall((msg + "\n").encode())
    except:
        pass  # Client disconnected abruptly

def recv_line(sock):
    try:
        data = sock.recv(1024)
        if not data:
            raise ConnectionResetError
        return data.decode().strip()
    except:
        raise ConnectionResetError

def handle_client(client_socket):
    try:
        send_line(client_socket, "Welcome !")

        while True:
            send_line(client_socket, "\nChoose an option:\n1. Explore\n2. Login\n> ")
            try:
                option = recv_line(client_socket)
            except:
                break

            token = None
            if option == "1":  # Explore
                send_line(client_socket, "Enter your name:")
                try:
                    username = recv_line(client_socket)
                except:
                    break
                token = generate_token(username)
                send_line(client_socket, "\nHere is your secret:")
                send_line(client_socket, token)

            elif option == "2":  # Login
                send_line(client_socket, "Enter your secret:")
                try:
                    token = recv_line(client_socket)
                except:
                    break

                try:
                    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                    username = decoded.get("username", "guest")
                    send_line(client_socket, f"Hello {username}")
                except jwt.InvalidTokenError:
                    send_line(client_socket, "Wrong secret.")
                    continue
            else:
                send_line(client_socket, "Invalid option. Try again.")
                continue

            # Enter flag menu
            while True:
                send_line(client_socket, "\nChoose an option:\n1. Get the flag\n2. Exit\n> ")
                try:
                    choice = recv_line(client_socket)
                except:
                    return

                if choice == "1":
                    try:
                        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                        if decoded.get("role") == "admin":
                            send_line(client_socket, f"\nWelcome, admin! Here is the flag: {FLAG}")
                        else:
                            send_line(client_socket, "\nOnly admin can access it.")
                    except jwt.ExpiredSignatureError:
                        send_line(client_socket, "\nYour secret has expired.")
                    except jwt.InvalidTokenError:
                        send_line(client_socket, "\nInvalid secret.")
                elif choice == "2":
                    send_line(client_socket, "Goodbye!")
                    client_socket.close()
                    return
                else:
                    send_line(client_socket, "Invalid option.")
    except:
        client_socket.close()

def start_server(host="0.0.0.0", port=1234):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server running on port {port}...")

    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    start_server()
