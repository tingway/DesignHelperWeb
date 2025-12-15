from flask import Flask, request, jsonify, render_template
import json
import datetime
import os

app = Flask(__name__)

DATA_FILE = "records.jsonl"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods=["POST"])
def calc():
    data = request.json

    # 施工計算（範例：面積 * 單價）
    length = float(data["length"])
    width = float(data["width"])
    unit_price = float(data["unit_price"])

    area = length * width
    amount = area * unit_price

    record = {
        "date": data["date"],
        "location": data["location"],
        "length": length,
        "width": width,
        "area": area,
        "unit_price": unit_price,
        "amount": amount,
        "created_at": datetime.datetime.now().isoformat()
    }

    # 寫入 JSON Lines
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return jsonify(record)


if __name__ == "__main__":
    app.run()
