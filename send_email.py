import smtplib, ssl
from email.mime.text import MIMEText


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "yourgmail.com"
    password = "your-app-password"   # <-- App Password, not your real Gmail password

    receiver = "whereyouwantosend@gmail.com"
    context = ssl.create_default_context()

    # Wrap message in MIMEText with UTF-8 encoding
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "Tesla News Update"
    msg["From"] = username
    msg["To"] = receiver

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())

# # Call with your news_fetch output
# send_email(main.news_fetch())