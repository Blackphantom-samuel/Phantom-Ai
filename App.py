from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Textgenerierungspipeline initialisieren
pipe = pipeline("text-generation", model="kingabzpro/llama-3.2-3b-it-Ecommerce-ChatBot")

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        messages = [{"role": "user", "content": user_input}]
        response = pipe(messages)
        return render_template('index.html', user_input=user_input, response=response[0]['generated_text'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
