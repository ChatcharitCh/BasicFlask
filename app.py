from flask import Flask

app = Flask(__name__)

@app.route('/') # นิยามเส้นทางในการเข้าถึงข้อมูล
def index():
    return "<h1>Hello Flask Framework</h1>"

@app.route('/about')
def about():
    return "<h1>About us</h1>"

@app.route("/admin")
def admin():
    return "<h1>Hello Admin</h1>"

if __name__ == "__main__":
    app.run()