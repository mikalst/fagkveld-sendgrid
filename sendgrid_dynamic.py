import sendgrid
import os
import random
from sendgrid.helpers.mail import Mail, Content, Personalization
from resources.gifs import urls

def sendmail(name, email):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    mail = Mail(from_email="mikal.stapnes@visma.com", to_emails=[email])

    mail.template_id = 'd-9dd397c8732f4c1f8df368eb104cab22'

    url = urls[random.randint(0, len(urls) - 1)]

    mail.dynamic_template_data = { 'secret_santa_name' : name, 'gif_url': url }


    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

if __name__ == "__main__":
    sendmail("Mikal", 'mikal.stapnes@visma.com')