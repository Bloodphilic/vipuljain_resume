from flask import Flask, render_template, request, url_for, redirect
#from email.mime.text import MIMEText
#import smtplib
#from email.message import EmailMessage
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/sendemail/", methods=['POST'])
# def sendemail():
#     if request.method == "POST":
#         name = request.form['name']
#         subject = request.form['Subject']
#         email = request.form['_replyto']
#         message = request.form['message']

#         your_name = "Vipul Jain"
#         your_email = "007.vipul.j@gmail.com"
#         your_password = "vipuljai"

#         # Logging in to our email account
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login(your_email, your_password)

#         # Sender's and Receiver's email address
#         sender_email = "007.vipul.j@gmail.com"
#         receiver_email = "s3910437@student.rmit.edu.au"

#         msg = EmailMessage()
#         msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
#         msg['Subject'] = 'New Response on Personal Website'
#         msg['From'] = sender_email
#         msg['To'] = receiver_email
#         # Send the message via our own SMTP server.
#         try:
#             # sending an email
#             server.send_message(msg)
#         except:
#             pass
#     return redirect('/');

if __name__ == "__main__":
    app.run(debug=True)
