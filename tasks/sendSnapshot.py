from libs.mailer import Mailer
from libs.database.queries import getNewsSnapshot

def sendSnapshot():
   mailer = Mailer()
   news_snapshot = getNewsSnapshot()

   
   mail = mailer.createMail(sender="summary@summerizenews.club",to="theo.thanhlam@gmail.com", data=news_snapshot)
   mailer.send(mail)
   
        
        
        
        
            
            
    
    

if __name__ == "__main__":
    sendSnapshot()