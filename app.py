from flask import Flask, render_template # render_template ใช้ในการแสดงผล

app = Flask(__name__)

@app.route('/') # นิยามเส้นทางในการเข้าถึงข้อมูล
def index():
    #return "<h1>Hello Flask Framework</h1>"
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/user/<name>/<age>') # นิยามพารามิเตอร์ (Dynamic Routing)
def member(name,age):
    return "<h1>Hello Member: {}, Age: {}</h1>".format(name,age)

if __name__ == "__main__":
    app.run()
    #app.run(debug= True) # เปิดโหมดสำหรับดีบัค