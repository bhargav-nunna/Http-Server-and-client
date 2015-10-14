import httplib
import sys


conn = httplib.HTTPConnection(sys.argv[1]+':'+sys.argv[2]) #create http message.
conn.request("GET", "/"+sys.argv[3]) #create and send http request.
response = conn.getresponse() #recieve response from server and store in response variable.
data = response.read() #Read the response.

conn.close() #Close the http connection.

print data # Print the recieved data.
