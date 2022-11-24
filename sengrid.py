import sendgrid
import os
from sendgrid.helpers.mail import Mail, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
mail = Mail(
    from_email="mikal.stapnes@visma.com", 
    to_emails=["mikal.stapnes@visma.com"], 
    subject="test", 
    plain_text_content="test")

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)