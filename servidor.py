import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index, deleta, update, error404

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()

    route = extract_route(request)

    filepath = CUR_DIR / route
    if filepath.is_file():
        response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    elif route.startswith('deletar'):
        id = route.split('/')[-1]
        response = deleta(id)
    elif route.startswith('update'):
        id = route.split('/')[1]
        response = update(request, id)
    else:
        response = error404()
    
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()