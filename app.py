from flask import Flask, render_template, jsonify
from flask_cors import CORS
app =  Flask(__name__)
CORS(app)
countries = {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120};

@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)
    
@app.get("/countries")
def get_countries():
    return jsonify(countries)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)