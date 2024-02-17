import socket

# Set up the list of servers to balance across
servers = [("localhost", 8001), ("localhost", 8002), ("localhost", 8003)]
current_server_index = 0

# Set up the load balancer server
lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lb_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lb_socket.bind(("localhost", 8080))
lb_socket.listen()

print("Load balancer listening on port 8080...")

while True:
    # Accept a client connection
    client_socket, client_address = lb_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Get the next server to route the request to
    server = servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(servers)
    print(f"Routing request to {server[0]}:{server[1]}")

    # Connect to the selected server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server)

    # Relay the client request to the server
    request = client_socket.recv(4096)
    server_socket.sendall(request)

    # Get the response from the server and relay it back to the client
    response = server_socket.recv(4096)
    client_socket.sendall(response)

    # Close the sockets
    client_socket.close()
    server_socket.close()