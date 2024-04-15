import os
import socket


def send_file(file_path, host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Open the file to be sent in binary mode
    with open(file_path, "rb") as file:
        # Get the file size
        file_size = os.path.getsize(file_path)

        # Send the file name and size to the server
        client_socket.send(f"Sending {file_path}".encode())
        client_socket.send(str(file_size).encode())

        # Read and send the file data in chunks
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

        # Send end-of-file indicator
        client_socket.send(b"<END>")

    # Close the socket
    client_socket.close()
