from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola flask, te estoy corriendo aunque no lo creas"

if __name__ == '__main__':
    app.run(debug=True)