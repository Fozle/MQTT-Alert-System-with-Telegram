# IoT Temperature Alert System with Telegram

## 📖 Project Overview
This project demonstrates a hybrid IoT architecture where temperature data is sent from a local sensor to an edge device via TCP sockets, bridged to a global MQTT broker, and finally processed by a cloud-based alert system that sends real-time notifications to Telegram.

## 🏗️ System Architecture
The data flows through the following stages:
1. **Sensor (Laptop 1):** Simulates a hardware sensor by generating temperature data and sending it over a **TCP Socket**.
2. **Edge Device (Laptop 2):** Acts as a gateway that receives local socket data and publishes it to the **MQTT Broker**.
3. **Cloud Server (Laptop 1):** Subscribes to the MQTT topic, monitors for values exceeding the threshold, and triggers the **Telegram Alert** via the Telegram Bot API.

## 📡 Technical Details
* **MQTT Broker:** `broker.emqx.io`
* **MQTT Topic:** `savonia/iot/temperature`
* **Alert Threshold:** 28.0 °C
* **Communication Protocols:** TCP Sockets (Local), MQTT (Global), HTTPS (Telegram Webhook)

## 📸 Proof of Operation
As verified in the terminal logs, the system successfully detects when the temperature exceeds the threshold and triggers the notification logic.

* **Terminal Output:** The subscriber identifies temperatures above 28°C and sends a POST request to Telegram.
* **Telegram Notification:** Messages appear in the custom bot chat: `🔥 ALERT: High temperature detected!`.

## 💡 Reflection Question

### Why is MQTT useful for building monitoring and alert systems in IoT?

MQTT is highly effective for monitoring and alert systems because:

1. **Decoupling:** The sensor does not need to know who is receiving the data. You can add multiple subscribers (like a dashboard and an alert system) without changing any code on the sensor.
2. **Efficiency:** It uses a "push" model rather than "polling." The alert system waits for a message to arrive instead of constantly asking the sensor for updates, which saves network bandwidth.
3. **Lightweight:** The protocol is designed for constrained devices, making it ideal for low-power IoT sensors like ESP32 or Raspberry Pi.
4. **Reliability:** MQTT supports Quality of Service (QoS) levels, ensuring that critical alerts are delivered even if the network connection is briefly unstable.
5. <img width="958" height="539" alt="Screenshot_2" src="https://github.com/user-attachments/assets/f653f0b1-c8ae-4a28-9181-e1a50f030fc5" />
<img width="649" height="460" alt="Screenshot_3" src="https://github.com/user-attachments/assets/f9cb36d9-6576-4916-996b-42a33075e2e2" />
<img width="960" height="540" alt="Screenshot_1" src="https://github.com/user-attachments/assets/f41f317f-c5be-44d6-bf5a-0de2d7e02e8f" />
