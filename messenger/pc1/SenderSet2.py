import smtplib
ans="y"
while ans=="y"or ans=="Y":
    line=input("Message:")
    Str1=line
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('mail3', 'mail3pass')
    subject = (Str1)
    to='mail2'
    s.sendmail("mail3", to, subject)
    s.quit()
    ans="y"
    if ans=="y"or ans=="Y":
        continue
    else:
        print("Thank you for using Julius Coder!Come back again")
