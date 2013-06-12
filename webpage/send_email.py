import smtplib

fromaddr = 'doktor.orwell@gmail.com'  
toaddrs  = 'taiyosogawa2013@u.northwestern.edu'  
subject = 'Hello from yur friend Dok Orwell!'
msg = 'Yo baby is pissed. go deal.\n\nLove,\nDoktor Orwell'
header = 'From: ' + fromaddr + '\nTo: ' + toaddrs + '\nSubject: ' + subject + '\n\n'

msg = header + msg

# Credentials (if needed)
username = 'doktor.orwell@gmail.com'
password = 'babymonitor'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()  
