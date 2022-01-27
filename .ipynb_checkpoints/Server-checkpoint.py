import socket
port =9000
s = socket.socket()
print ("Socket successfully created")
s.bind(('', port))
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )
    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    c.send('Server message send'.encode())
    # Close the connection with the client
    c.close()
    # Breaking once connection closed
    break
