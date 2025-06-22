from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Render! This is the sensor data server."

@app.route("/sensor")
def sensor_data():
    # 模擬溫度和濕度數值
    temperature = round(random.uniform(20.0, 30.0), 2)  # 20 ~ 30 度之間，兩位小數
    humidity = round(random.uniform(40.0, 60.0), 2)     # 40% ~ 60% 濕度
    
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "unit": {
            "temperature": "°C",
            "humidity": "%"
        }
    }
    # 用 jsonify 回傳 JSON 格式資料給前端
    return jsonify(data)
