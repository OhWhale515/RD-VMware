import socket

SERVER_HOST = 'IP_ADDRESS_OF_UBUNTU_VM'  # Replace with the IP address of the Ubuntu VM
SERVER_PORT = 5000

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT}")

    while True:
        command = input("Enter command to execute on the server or 'exit' to quit: ")
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        output = client_socket.recv(1024).decode()
        print(output)

    client_socket.close()

start_client()
