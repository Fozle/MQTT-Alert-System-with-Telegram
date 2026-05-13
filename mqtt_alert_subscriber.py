import paho.mqtt.client as mqtt
import requests

# --- CONFIGURATION ---
# The broker used by Savonia UAS for this lab
BROKER = "broker.emqx.io"
TOPIC = "savonia/iot/temperature"

# The threshold set in your lab instructions
THRESHOLD = 28.0

# Your specific Telegram details
TOKEN = ""
# IMPORTANT: Replace the number below with the ID from @userinfobot
CHAT_ID = "" 

def send_telegram(message):
    """Sends a notification to your Telegram bot via the API."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram notification sent successfully!")
        else:
            print(f"❌ Failed to send Telegram. Error: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")

def on_message(client, userdata, msg):
    """Callback function that triggers whenever a new MQTT message arrives."""
    try:
        # Decode the bytes from the broker into a float
        temperature = float(msg.payload.decode())
        print(f"Current Temperature: {temperature}°C")

        # Logic to trigger the alert
        if temperature > THRESHOLD:
            alert_text = f"🔥 ALERT: High temperature detected! {temperature}°C"
            print(alert_text)
            send_telegram(alert_text)
            
    except ValueError:
        print("Received invalid data (not a number)")

def start_subscriber():
    """Initializes the MQTT client and starts the monitoring loop."""
    client = mqtt.Client()
    client.on_message = on_message
    
    print("Connecting to MQTT Broker...")
    client.connect(BROKER, 1883)
    
    # Subscribe to the specific topic used by your edge device
    client.subscribe(TOPIC)
    
    print(f"Monitoring system active. Threshold: {THRESHOLD}°C")
    print("Waiting for data...")
    
    # Keep the script running forever to listen for messages
    client.loop_forever()

if __name__ == "__main__":
    start_subscriber()
