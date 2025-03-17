# Chat com gRPC

## Utilização

- Clone este repositório
- Instale as dependências: `pip install -r requirements.txt`
- Gere os arquivos protobuffer: `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto`
- Execute o arquivo `server.py` para iniciar o servidor
- Agora execute o arquivo `client.py` para iniciar o cliente
