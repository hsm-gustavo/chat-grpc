# Chat com gRPC

## Utilização

- Clone este repositório
- Instale as dependências: `pip install -r requirements.txt`
- Gere os arquivos protobuffer: `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto`
- Execute o arquivo main.py como servidor, por padrão a conexão é em http://localhost:50051
- Agora execute como cliente utilizando a conexão aberta no servidor
