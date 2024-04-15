---

# File Transfer Program

This Python program enables file transfer between a sender and a receiver using sockets.

## Usage

### Sender

1. Run `sender.py`.
2. Provide the file path, host, and port as command-line arguments.

Example:
```bash
python sender.py /path/to/file.txt localhost 9999
```

### Receiver

1. Run `receiver.py`.
2. Provide the saved path, host, and port as command-line arguments.

Example:
```bash
python receiver.py /path/to/file.txt localhost 9999
```

## Requirements

- Python 3.x

## How It Works

- **sender.py**: This script sends a file to a receiver. It establishes a connection with the receiver, sends the file name and size, and then sends the file data in chunks.

- **receiver.py**: This script receives a file from a sender. It listens for incoming connections, accepts the sender's connection, receives the file name and size, and then receives the file data in chunks until the end-of-file indicator `<END>` is received.

- **Important**: Make sure that the file you want to send is in the same directory as the `sender.py` file. 

## License

This project is licensed under the [MIT License](LICENSE).

---
