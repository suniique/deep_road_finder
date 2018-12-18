import threading
from dwebsocket.decorators import accept_websocket,require_websocket

clients = []

@accept_websocket
def client_register(request, id):
    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            clients.append({
                "conn": request.websocket,
                "id": id})
            print("Add to clients group:", request.path)
            request.websocket.send("Success!")
        finally:
            lock.release()


@accept_websocket
def client_release(request, id):
    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            clients.remove({
                "conn": request.websocket,
                "id": id})
            print("remove client:", request.path)
            request.websocket.send("Success!")
        finally:
            lock.release()


@accept_websocket
def send_websocket(data, id):
    for client in clients:
        if client["id"] == id:
            conn = client["conn"]
            conn.send(data)
