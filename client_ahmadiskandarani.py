import socket
import datetime
import uuid
host = '127.0.0.1'
port = 12000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create the client socket
client.connect((host,port)) #connect to the host and port
ip_address = input("Enter destination IP address: ")
start = datetime.datetime.now() # time when request is sent
client.send(ip_address.encode())
current_time6 = datetime.datetime().now() #current time code got from google
print("Request sent to proxy server", current_time6 )
response=client.recv(1024)
end = datetime.datetime.now() #time when request received
current_time7 = datetime.datetime().now()

print("From Server: ",response.decode(),current_time7) 
x = end-start
print("Round time is: " , x.totalSeconds()) #final - initial inside variable x , then x.totalSeconds() get u number of seconds iza badak milliseconds just multiply by a 1000
mac_address = str(hex(uuid.getnode())) #mac address
print("Mac address: ",mac_address)