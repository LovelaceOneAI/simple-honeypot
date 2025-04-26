import socket

def honeypot_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 2222))  # Dummy SSH port
    server_socket.listen(5)
    print("🍯 Honeypot listening for connections on port 2222...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"🚨 Unauthorized login attempt from: {address}")
        client_socket.send(b"Unauthorized.\n")
        client_socket.close()

if __name__ == "__main__":
    honeypot_server()
