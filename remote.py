import pyautogui
import socket

# Change these variables with your remote machine's details
REMOTE_HOST = '192.168.0.100'  # Remote machine's IP address
REMOTE_PORT = 5000  # Remote machine's port number

def connect_to_remote():
    # Connect to the remote machine
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((REMOTE_HOST, REMOTE_PORT))
    return remote_socket

def send_mouse_position(remote_socket, x, y):
    # Send the mouse position to the remote machine
    position = f"{x},{y}"
    remote_socket.send(position.encode())

def remote_desktop():
    remote_socket = connect_to_remote()
    while True:
        try:
            # Receive the mouse position from the remote machine
            position = remote_socket.recv(1024).decode()
            if not position:
                break
            x, y = position.split(",")
            x, y = int(x), int(y)

            # Move the mouse on the local machine
            pyautogui.moveTo(x, y, duration=0.1)
        except Exception as e:
            print(f"Error: {e}")
            break

    remote_socket.close()

if __name__ == '__main__':
    remote_desktop()
