import socket
import tqdm


def receive_file(save_path, host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()

    # Accept a client connection
    client_socket, _ = server_socket.accept()

    # Receive the file name and size from the client
    file_name = client_socket.recv(1024).decode()
    print("Receiving:", file_name)
    file_size = int(client_socket.recv(1024).decode())
    print("File size:", file_size)

    # Open the file to save the received data
    with open(save_path, "wb") as file:
        # Receive and write the file data in chunks
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))
        while True:
            data = client_socket.recv(1024)
            if data[-5:] == b"<END>":
                break
            file.write(data)
            progress.update(len(data))

    # Close the sockets
    client_socket.close()
    server_socket.close()
