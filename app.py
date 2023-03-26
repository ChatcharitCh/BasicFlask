from flask import Flask, render_template,request # render_template ใช้ในการแสดงผล

app = Flask(__name__)

@app.route('/') # นิยามเส้นทางในการเข้าถึงข้อมูล
def index():
    data = {"name": "Chatcharit", "age": 27, "salary": 25000}
    #return "<h1>Hello Flask Framework</h1>"
    return render_template("index.html",mydata = data)

@app.route('/about')
def about():
    products = ["Larb", "Som-Tum", "Pad-Thai", "Tom-Yum-Kung", "Panage"]
    return render_template("about.html", myproduct = products)

@app.route('/admin')
def admin():
    
    username = "Chatcharit"
    return render_template("admin.html", username = username) # ส่งข้อมูลไปใน Template

@app.route('/sendData')
def signupForm():
    name = request.args.get('name')
    description = request.args.get('description')
    return render_template("thankyou.html", data = {"name": name, "description": description})


@app.route('/user/<name>/<age>') # นิยามพารามิเตอร์ (Dynamic Routing)
def member(name,age):
    return "<h1>Hello Member: {}, Age: {}</h1>".format(name,age)

if __name__ == "__main__":
    app.run()
    #app.run(debug= True) # เปิดโหมดสำหรับดีบัค