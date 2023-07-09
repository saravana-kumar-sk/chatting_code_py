import socket as soc 
s=soc.socket()
s.bind(("192.168.205.43",300))
s.listen(10)
c,addr=s.accept()
print(addr)
a=""
while(a!="bye"):
        a=input("server:")
        c.send(a.encode())
        msg=c.recv(1000)
        print("client:",msg.decode())
if (a=="bye"):
        print("server left the chat")
c.close()
        


