from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Allow your Vite React app to call Flask
CORS(app, origins=["http://localhost:5173"])

@app.route("/")
def home():
    return jsonify({"message": "Flask backend is running"})

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"status": "ok", "message": "React can call Flask"})

@app.route("/api/product-draft", methods=["POST"])
def product_draft():
    data = request.get_json()

    title = data.get("title", "")
    colors = data.get("colors", [])
    sizes = data.get("sizes", [])

    variants = []
    for color in colors:
        for size in sizes:
            variants.append({
                "color": color,
                "size": size
            })

    return jsonify({
        "title": title,
        "variants": variants
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)