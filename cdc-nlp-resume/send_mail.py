import smtplib
  
def send_mail(email_id , name):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("supermangreat55@gmail.com", "pass357word")
    message = "Welcome to our company "+name+". You can start your work from next monday"
    s.sendmail("supermangreat55@gmail.com", email_id, message)
    s.quit()