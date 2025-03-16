import grpc
import threading
import time
from concurrent import futures
import chat_pb2
import chat_pb2_grpc

class ChatNode(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.message_queues = []

    def ChatStream(self, request_iterator, context):
        message_queue = []
        self.message_queues.append(message_queue)

        try:
            for message in request_iterator:
                print(f"Recebido: {message.message}")
                for queue in self.message_queues:
                    queue.append(message)
        except grpc.RpcError:
            pass
        finally:
            self.message_queues.remove(message_queue)

        while True:
            if message_queue:
                yield message_queue.pop(0)
            time.sleep(0.1)

    def send_messages(self, stub):
        while True:
            msg = input("Você: ")
            stub.ChatStream(iter([chat_pb2.ChatMessage(message=msg)]))


def start_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatNode(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Servidor iniciado na porta {port}")
    server.wait_for_termination()


def start_client(target):
    channel = grpc.insecure_channel(target)
    stub = chat_pb2_grpc.ChatServiceStub(channel)
    
    threading.Thread(target=ChatNode().send_messages, args=(stub,), daemon=True).start()
    
    for response in stub.ChatStream(iter([])):
        print(f"Remoto: {response.message}")


if __name__ == "__main__":
    choice = input("Deseja iniciar como servidor (s) ou cliente (c)? ")
    port = "50051"
    if choice.lower() == "s":
        start_server(port)
    else:
        target = input("Digite o endereço do servidor (ex: localhost:50051): ")
        start_client(target)
