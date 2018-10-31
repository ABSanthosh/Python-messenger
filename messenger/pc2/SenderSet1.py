import smtplib
ans="y"
while ans=="y"or ans=="Y":
    line=input("Message:")
    list=[]
    for i in (line):
        list+=i
		 

    Str1 = "".join(list)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('mail2', 'mail2pass')
    subject = (Str1)
    to='mail1'
    s.sendmail("mail3", to, subject)
    s.quit()
    ans="y"
    if ans=="y"or ans=="Y":
        continue
    else:
        print("Thank you for using Julius Coder!Come back again")
