import threading
import socket

host = 'localhost'
porta = 8000

def main():

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp.connect((host, porta))
    except:
        return print('\nconexão não realizada\n')

    usuario = input('Usuário: ')
    print('Conectado')

    thread1 = threading.Thread(target=receber, args=[tcp])
    thread2 = threading.Thread(target=enviar, args=[tcp, usuario])

    thread1.start()
    thread2.start()

#ira receber um objeto socket
def receber(tcp):
    while True:
        try:
            msg = tcp.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nimpossivel conectar no servidor\n')
            print('\nPrecione ENTER\n')
            tcp.close()
            break
            

def enviar(tcp, usuario):
    while True:
        try:
            msg = input('\n')
            tcp.send(f'<{usuario}> {msg}'.encode('utf-8'))#vai enviar a mensagem codigica em PT-BR
        except:
            return


main()
