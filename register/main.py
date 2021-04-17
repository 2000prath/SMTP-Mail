from flask import Flask,request,render_template
import smtplib 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
app=Flask(__name__)

students=[]

@app.route("/")
def index():
   return render_template("index.html")




#register by emails
@app.route("/register",methods=["POST"])
def register():
   name=request.form.get("name")
   country=request.form.get("country")
   email=request.form.get("email")
   if not name :
      return render_template("fails.html")
   
   students.append(name+" from "+country)
   
      
  
   try:
      message="""Subject: this is subject """
      server= smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login("your_email_address","password")
      server.sendmail("your_email_address",email,message)
   except:
      return "something went wrong" 
   return render_template("info.html",students=students)
   




   

   
   
   
