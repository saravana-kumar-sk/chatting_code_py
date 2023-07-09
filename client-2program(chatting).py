import socket as soc
s=soc.socket()
hostname=soc.gethostname()
ipadress=soc.gethostbyname(hostname)
print(ipadress)
s.connect((ipadress,300))
print("connected")
a=""
while(a!="bye"):
        msg=s.recv(1000)
        print("server:",msg.decode())
        a=input("client:")
        s.send(a.encode())
if (a=="bye"):
        print("client left the chat")
s.close()

        
