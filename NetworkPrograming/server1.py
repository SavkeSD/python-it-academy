import socket
 
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    ### AF_INET znaci da je IPV4, a SOCK_STREAM znaci da je TCP protokol
sSocket.bind(("127.0.0.1",8005))
sSocket.listen()
print("Server is listening...")
sSocket.accept()
print("It was pleasure")
sSocket.close()

