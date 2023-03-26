from flask import Flask, render_template,request, session # render_template ใช้ในการแสดงผล
from flask_wtf import FlaskForm # ตัวที่ใช้สำหรับออกแบบฟอร์ม
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app) # ตั้งค่า object flask

class MyForm(FlaskForm): # ออกแบบฟอร์ม
    name = StringField("Enter your name", validators = [DataRequired()])
    isAccept = BooleanField("Accept Policy")
    gender = RadioField("Sex", choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    skills = SelectField("Skills", choices = [('Python', 'Python'), ('JavaScript', 'JavaScript'), ('C++', 'C++'), ('C#', 'C#'), 
                                              ('C', 'C'), ('PHP', 'PHP'), ('Flutter', 'Flutter')])
    address = TextAreaField("Address")
    submit = SubmitField("Save")


@app.route('/', methods = ['GET', 'POST']) # นิยามเส้นทางในการเข้าถึงข้อมูล # GET แสดงหน้าเว็บขึ้นมา / POST ส่งข้อมูลจากแบบฟอร์ม
def index():
    form = MyForm()
    
    if form.validate_on_submit():
        # ช่วยให้สามารถกระจายข้อมูลไปทำงานในหน้าเว็บ
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skills'] = form.skills.data
        session['address'] = form.address.data
        
        # clear data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.address.data = ""
    return render_template("index.html", form = form)

if __name__ == "__main__":
    app.run(debug= True) # เปิดโหมดสำหรับดีบัค