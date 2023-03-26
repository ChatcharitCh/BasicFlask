from flask import Flask, render_template,request # render_template ใช้ในการแสดงผล
from flask_wtf import FlaskForm # ตัวที่ใช้สำหรับออกแบบฟอร์ม
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm): # ออกแบบฟอร์ม
    name = StringField("Enter your name")
    submit = SubmitField("Save")


@app.route('/', methods = ['GET', 'POST']) # นิยามเส้นทางในการเข้าถึงข้อมูล # GET แสดงหน้าเว็บขึ้นมา / POST ส่งข้อมูลจากแบบฟอร์ม
def index():
    form = MyForm()
    name = False
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("index.html", form = form, name = name)

if __name__ == "__main__":
    app.run(debug= True) # เปิดโหมดสำหรับดีบัค