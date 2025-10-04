from libs.mailer import Mailer
from libs.database.queries import getNewsSnapshot

def sendSnapshot():
   mailer = Mailer()
   news_snapshot = getNewsSnapshot()

   
   mailer.send_message(to_email="theo.thanhlam@gmail.com", data=news_snapshot['data'], subject="Today's News Snapshot")
   
        
        
        
        
            
            
    
    

if __name__ == "__main__":
    sendSnapshot()