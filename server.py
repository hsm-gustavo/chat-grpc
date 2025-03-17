import time
from concurrent import futures

import grpc

import chat_pb2
import chat_pb2_grpc


class ChatServer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        # historico do chat
        self.chats = []

    # a stream que será usada pra mandar novas mensagens pros clientes
    def ChatStream(self, request_iterator, context):

        last_index = 0
        # pra cada cliente temos um loop infinito
        while True:
            # checagem por novas mensagens
            while len(self.chats) > last_index:
                n = self.chats[last_index]
                last_index += 1
                yield n

    def SendMessage(self, request: chat_pb2.ChatMessage, context):
        # print para o console do servidor
        print(f"[{request.name}] {request.message}")
        # adicionar mensagem ao historico
        self.chats.append(request)
        return (
            chat_pb2.Empty()
        )  # algo precisa ser retornado em protobuf, como nao tem nada pra retornar aqui retornamos vazio


if __name__ == "__main__":
    port = "50051"  # uma porta qualquer pro servidor rodar
    # definindo o maximo de clientes para 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatServer(), server
    )  # registrando o server no grpc

    print("Iniciando o servidor.")
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Servidor iniciado na porta {port}")

    server.wait_for_termination()
