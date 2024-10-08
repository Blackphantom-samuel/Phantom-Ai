import os

# Verzeichnisstruktur erstellen
def create_directories():
    os.makedirs("chatbot_app/static", exist_ok=True)

# app.py Datei erstellen
def create_app_py():
    app_py_content = """
import requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Hugging Face API Token und Modell
API_URL = "https://api-inference.huggingface.co/models/gpt-neo-2.7B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Eingabetext vom Benutzer
    user_input = request.json.get("input", "")

    # Abfrage an Hugging Face API senden
    output = query({
        "inputs": user_input
    })

    # Antwort an den Benutzer zurücksenden
    return jsonify(output)

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
    """

    with open("chatbot_app/app.py", "w") as f:
        f.write(app_py_content)

# index.html erstellen
def create_index_html():
    index_html_content = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body {
            background-color: #222;
            color: #fff;
            font-family: 'Arial', sans-serif;
        }
        .chatbox {
            width: 500px;
            margin: 0 auto;
            padding: 20px;
            background-color: #333;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        .message {
            margin: 10px 0;
        }
        .message.user {
            text-align: right;
            color: #00ff00;
        }
        .message.bot {
            text-align: left;
            color: #00bfff;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            background-color: #00bfff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chatbox">
        <div id="chatlog"></div>
        <input type="text" id="userInput" placeholder="Schreibe eine Nachricht...">
        <button onclick="sendMessage()">Senden</button>
    </div>

    <script>
        function sendMessage() {
            const userInput = document.getElementById("userInput").value;
            const chatlog = document.getElementById("chatlog");

            // Zeige die Benutzer-Eingabe an
            const userMessage = document.createElement("div");
            userMessage.className = "message user";
            userMessage.textContent = userInput;
            chatlog.appendChild(userMessage);

            // Sende Anfrage an den Flask-Server
            fetch("/chatbot", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input: userInput })
            })
            .then(response => response.json())
            .then(data => {
                // Zeige die Antwort des Chatbots an
                const botMessage = document.createElement("div");
                botMessage.className = "message bot";
                botMessage.textContent = data[0]["generated_text"];
                chatlog.appendChild(botMessage);
            });
        }
    </script>
</body>
</html>
    """

    with open("chatbot_app/static/index.html", "w") as f:
        f.write(index_html_content)

# Anforderungen in requirements.txt festlegen
def create_requirements_txt():
    requirements_content = """
flask
requests
    """

    with open("chatbot_app/requirements.txt", "w") as f:
        f.write(requirements_content)

# Alles zusammen erstellen
def setup_chatbot_app():
    create_directories()
    create_app_py()
    create_index_html()
    create_requirements_txt()
    print("Chatbot-App erfolgreich erstellt!")

# Skript ausführen
if __name__ == "__main__":
    setup_chatbot_app()
  
