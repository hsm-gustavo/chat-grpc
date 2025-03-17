# 📩 Chat com gRPC

## Equipe

| 👤 Nome                                    | Matrícula  |
|------------------------------------------- | ---------- |
| Caio Teixeira da Silva                     | 22112243   |
| Gustavo Henrique dos Santos Malaquias      | 22111978   |
| Noemy Torres Pereira                       | 22112110   |

## Universidade & Disciplina

- **Universidade:** Universidade Federal de Alagoas (UFAL)
- **Disciplina:** Sistemas Distribuídos
- **Professor:** Tércio de Morais

---

## Utilização

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/SeuUsuario/CHAT-GRPC.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Gere os arquivos do Protobuf:**
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto
   ```

4. **Execute o Servidor:**
   ```bash
   python server.py
   ```
   O servidor iniciará na porta `50051` e ficará aguardando as mensagens dos clientes.

5. **Execute o Cliente:**
   ```bash
   python client.py
   ```
   Ao iniciar o cliente, você deverá inserir seu nome de usuário e, em seguida, poderá enviar mensagens. As mensagens enviadas serão encaminhadas ao servidor e distribuídas para todos os clientes conectados.

---

## Descrição do Projeto

Este projeto implementa um chat utilizando gRPC em Python. Nele, o servidor mantém um histórico das mensagens e fornece uma stream que permite aos clientes receberem novas mensagens em tempo real. O servidor expõe dois métodos:

- **ChatStream:** Uma stream contínua que envia para os clientes todas as mensagens novas do histórico.
- **SendMessage:** Método para enviar uma mensagem ao servidor, que é adicionada ao histórico e repassada aos clientes.

No lado do cliente, uma thread é iniciada para ouvir as mensagens vindas do servidor, enquanto o usuário pode digitar e enviar novas mensagens. Apenas mensagens enviadas por outros usuários são exibidas, evitando duplicidade na exibição do próprio nome.

---

## Estrutura do Projeto

```
CHAT-GRPC/
│── chat.proto              # Definição do serviço e mensagens (Protobuf)
│── chat_pb2.py             # Código gerado a partir do chat.proto
│── chat_pb2_grpc.py        # Código gerado a partir do chat.proto para gRPC
│── server.py               # Implementação do servidor gRPC
│── client.py               # Implementação do cliente gRPC
│── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## Tecnologias Utilizadas

- **Python 3.x** – Linguagem de programação
- **gRPC** – Framework para comunicação remota (RPC)
- **Protobuf** – Serialização de dados e definição de serviços

---
