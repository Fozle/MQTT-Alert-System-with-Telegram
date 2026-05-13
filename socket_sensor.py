import socket
import time
import random

# Configuration
EDGE_IP = "127.0.0.1" 
EDGE_PORT = 5000

def start_sensor():
    while True:
        try:
            # Create socket and connect to Edge Device
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((EDGE_IP, EDGE_PORT))
            
            # Generate a random temperature
            temp = round(random.uniform(20.0, 35.0), 1)
            print(f"Sending temperature: {temp}°C")
            
            # Send data
            s.sendall(str(temp).encode())
            s.close()
            
        except ConnectionRefusedError:
            print("Waiting for Edge Device to start...")
        
        time.sleep(5) # Send data every 5 seconds

if __name__ == "__main__":
    start_sensor()