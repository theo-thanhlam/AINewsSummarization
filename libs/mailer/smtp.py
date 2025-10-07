import mailtrap as mt
from dotenv import load_dotenv
import os
load_dotenv()

class Mailer:
    _MAILTRAP_API_KEY=os.getenv("MAILTRAP_API_KEY")
    def __init__(self):
        self.client = mt.MailtrapClient(token=self._MAILTRAP_API_KEY)
        
    def createMail(self, sender:str, to:list, data:any):
        mail = mt.MailFromTemplate(
            sender = mt.Address(email=sender, name="Summerize Club"),
            to = [mt.Address(email=to)],
            template_uuid="38c0dffa-8bb3-49b8-9a7c-d958fb5998e5",
            template_variables=data
        )
        return mail
        
        
    def send(self,  mail):
        try:
            self.client.send(mail)
        except Exception as e:
            print("SENDING EMAIL ERROR")
            raise e
            
        