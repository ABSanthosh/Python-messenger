import imaplib
import email
import email.parser
global ik
ans="y"
while ans=="y"or ans=="Y":
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('mail1', 'mail1pass')#edit
    mail.list() 
    mail.select('inbox') 
    result, data = mail.uid('search', None, '(FROM "mail2")')#edit
    i = len(data[0].split()) 
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
    print ("Message:",email_message.get_payload().strip())
    #ik=input("Message:")
    ans=input("Reload?(y/n)")
    if ans=="y"or ans=="Y":
        continue
    else:
        print("Thank you for using Julius Coder!Come back again")


















##    if email_message.is_multipart():
##        for payload in email_message.get_payload():
##            #print ("Message:",payload.get_payload())
##            ik=input("Message:")
##    else:    
##        print ("Message:",email_message.get_payload())
##    
