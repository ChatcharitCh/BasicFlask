from flask import Flask

app = Flask(__name__)

@app.route('/') # นิยามเส้นทางในการเข้าถึงข้อมูล
def index():
    return "<h1>Hello Flask Framework</h1>"

if __name__ == "__main__":
    app.run()