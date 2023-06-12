import socket
import threading
import tkinter as tk

server_socket = None
server_thread = None

def handle_client(client_socket):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'exit':
            break
        print(f"Received message from client: {message}")

        # Send response to client
        response = "Message received!"
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

def start_server():
    global server_socket
    global server_thread

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name and choose a port
    host = socket.gethostname()
    port = 12345

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on {}:{}".format(host, port))

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print("Connected to {}:{}".format(addr[0], addr[1]))

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def stop_server():
    global server_socket
    global server_thread

    if server_socket is not None:
        # Close the server socket
        server_socket.close()
        server_socket = None

    if server_thread is not None:
        # Wait for the server thread to complete
        server_thread.join()
        server_thread = None

def on_start_button_click():
    start_server_button.config(state=tk.DISABLED)
    stop_server_button.config(state=tk.NORMAL)
    start_server()

def on_stop_button_click():
    start_server_button.config(state=tk.NORMAL)
    stop_server_button.config(state=tk.DISABLED)
    stop_server()

# Create the GUI window
window = tk.Tk()

# Create the start button
start_server_button = tk.Button(window, text="Start Server", command=on_start_button_click)
start_server_button.pack()

# Create the stop button
stop_server_button = tk.Button(window, text="Stop Server", command=on_stop_button_click, state=tk.DISABLED)
stop_server_button.pack()

# Run the GUI event loop
window.mainloop()