import threading

import grpc

import chat_pb2
import chat_pb2_grpc

address = "localhost"
port = "50051"


class Client:
    def __init__(self, username: str):
        self.username = username

        # criacao de um canal grpc + stub
        channel = grpc.insecure_channel(f"{address}:{port}")
        self.connection = chat_pb2_grpc.ChatServiceStub(channel)

        # criando uma nova thread para escutar novas mensagens
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

        self.run()

    def listen_for_messages(self):
        # escuta novas mensagens vindo do servidor e printa no console
        for message in self.connection.ChatStream(chat_pb2.Empty()):
            if (self.username != message.name):
                print(f"[RECEBIDO] [{message.name}]: {message.message}")

    def send_message(self, message: str):
        # manda mensagem pro servidor
        if message.strip():
            n = chat_pb2.ChatMessage(name=self.username, message=message)
            print(f"[ENVIADO] [{self.username}]: {message}")
            self.connection.SendMessage(n)

    def run(self):
        print("Digite suas mensagens abaixo. Aperte Ctrl+C para sair.")
        try:
            while True:
                message = input()
                self.send_message(message)
        except KeyboardInterrupt:
            print("\nSaindo do chat...")
            exit()


if __name__ == "__main__":
    username = input("Insira seu nome de usuário: ")
    Client(username)
