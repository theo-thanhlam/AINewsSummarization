from libs.mailer import Mailer
from libs.database.queries import getNewsSnapshot,getSubscribers

def sendSnapshot():
   mailer = Mailer()
   news_snapshot = getNewsSnapshot()
   subscribers = getSubscribers()
   
   
   for subscriber in subscribers["data"]:
      mail = mailer.createMail(sender="summary@summerizenews.club",to=subscriber, data=news_snapshot)
      mailer.send(mail)
   
        
        
        
        
            
            
    
    

if __name__ == "__main__":
    sendSnapshot()