import socket
import datetime

host = '127.0.0.1'
port = 12000

# create the proxy server's socket
socket_proxyserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_proxyserver.bind((host, port))  # bind the host ip address and the port number
socket_proxyserver.listen(1)  # 1 client in which the server can listen to simultaneously
try:
    client, address = socket_proxyserver.accept()
    current_time0 = datetime.datetime().now()
    print("Connected at" + str(current_time0))
    request = client.recv(4096).decode()
    current_time1 = datetime.datetime().now()
    print("Client requesting to connect to: ", request, "at time: ", current_time1, "received.")
    # we connect the destination to the proxy server
    destination = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destination.connect((str(request), 80))  # We connect to port 80 (known port for http webpages)
    current_time2 = datetime.datetime().now()  # current time code got from google
    print("Link Established to Destination Server at " + str(current_time2))
    destination.send(bytes("GET / HTTP/1.1\r\nHost:" + str(request) + ":80\r\n\r\n",
                           'utf-8'))  # We send the actual request to the destination server.
    current_time3 = datetime.datetime().now()
    print("Request sent to destination server at ", current_time3)
    response = destination.recv(4096)  # the proxy server gets back the response from the destination server
    current_time4 = datetime.datetime().now()
    print("Response received from destination server: ", current_time4)
    current_time5 = datetime.datetime().now()  # current time code got from google
    client.send(response)  # send the destination server's response to the client
    print("Response sent to the client: ", current_time5)
except:
    print("Error")


