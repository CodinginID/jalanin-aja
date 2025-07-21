from flask import Flask, render_template, url_for
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__" :
    port = int(os.getenv('APP_PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
