import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

BASE_DIR = Path(__file__).parent
class Mailer:
    

    
    def __init__(self):
        self.SMTP_USERNAME = os.getenv("SMTP_USERNAME")
        self.SMTP_APP_PASSWORD = os.getenv("SMTP_APP_PASSWORD")
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587
        
        env = Environment(loader=FileSystemLoader(BASE_DIR / "templates"))
        self.template= env.get_template("daily_snapshot.html")
        
    def send_message(self,to_email:str, data,subject:str=None) :
        msg = MIMEMultipart()
        html = self.template.render(data=data)
        
        msg["From"] = self.SMTP_USERNAME
        msg["To"] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(html,"html"))
        
        with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
            server.starttls()
            server.login(self.SMTP_USERNAME, self.SMTP_APP_PASSWORD)
            server.send_message(msg)

        
        
        
    
    
    