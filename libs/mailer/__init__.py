import os
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv
load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


sg_client = SendGridAPIClient(SENDGRID_API_KEY)
template_id = "d-68be7f2d51864a378525267e2d578103"
