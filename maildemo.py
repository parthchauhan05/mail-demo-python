from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "" #From Address
toaddr = "" # To Address
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "" #Subject

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
msg.attach(MIMEText(html, 'html'))
import smtplib
server = smtplib.SMTP('', 587) #SMTP address
server.ehlo()
server.starttls()
server.ehlo()
server.login("", "") # username, password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)