import socket
import paho.mqtt.client as mqtt

# Socket Config
LISTENING_IP = "127.0.0.1"
LISTENING_PORT = 5000

# MQTT Config
BROKER = "broker.emqx.io"
TOPIC = "savonia/iot/temperature"

def start_edge():
    # Setup MQTT
    mqtt_client = mqtt.Client()
    mqtt_client.connect(BROKER, 1883)
    
    # Setup Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((LISTENING_IP, LISTENING_PORT))
    server_socket.listen(1)
    
    print(f"Edge Device listening on {LISTENING_IP}:{LISTENING_PORT}...")

    while True:
        conn, addr = server_socket.accept()
        data = conn.recv(1024).decode()
        if data:
            print(f"Received from sensor: {data}. Publishing to MQTT...")
            mqtt_client.publish(TOPIC, data)
        conn.close()

if __name__ == "__main__":
    start_edge()