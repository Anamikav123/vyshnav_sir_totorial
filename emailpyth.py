import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('anamikapy661@gmail.com','lluhjxfjhixaucnn')
msg="hi python programer\n regards your lovely"
s.sendmail('anamikapy661@gmail.com',['anamikamanoharan@gmail.com','anamikapy661@gmail.com'],msg)
print("email send successfull in terminal")
s.quit()

