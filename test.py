from libs.database.queries import getNewsSnapshot
import json
from libs.mailer import *
from sendgrid.helpers.mail import Mail, Email, To, Content

def main():
   data = getNewsSnapshot()
   data_json = json.dumps(data, indent=4)
   
   from_email = "theolam.dev@gmail.com"
   to_email = "theo.thanhlam@gmail.com"
   subject = f"{data['date']} News Snapshot"
   dynamic_template_data = data['data']
   
   message = Mail(from_email=from_email, to_emails=to_email, subject=subject)
   message.dynamic_template_data = data
   message.template_id = template_id
   
   try:
      
      response = sg_client.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
   except Exception as e:
      print(e)
      
        
        
        
        
            
            
    
    

if __name__ == "__main__":
    main()