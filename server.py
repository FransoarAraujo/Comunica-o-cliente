import threading
import socket

clients = []#irá armazenar os clientes criados
host = 'localhost'
porta = 8000

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, porta))
        server.listen()#quantidade de conexões
    except:
        return print('\nServidor offline\n')

    while True:
        client, doc = server.accept()
        clients.append(client)
        print('cliente: ',doc, 'conectado com sucesso')

#cada cliente do servidor sera adicionado em uma nova thread e iniciada em paralela
        thread = threading.Thread(target=tratamentoMensagens, args=[client])
        thread.start()

def tratamentoMensagens(client):
    while True:
        try:
            msg = client.recv(1024)
            #se a mensagem foi recebida a mensagem sera envida para todos os outros clintes
            broadcast(msg, client)
            print(msg)
            #se ciente for desconectado o cliente sera removido da lista
        except:
            deleteClient(client)
            break

#ira enviar a mensagem para todos os clientes menos para o cliente que a enviou
def broadcast(msg, client):
    #cada cliente dentro da lista clients
    for clientItem in clients:
        #verifica quem enviou a mensagem
        if clientItem != client:
            try:
                clientItem.send(msg)
            #se ciente for desconectado o cliente sera removido da lista
            except:
                deleteClient(clientItem)

#remove os clientes da lista
def deleteClient(client):
    clients.remove(client)

main()
