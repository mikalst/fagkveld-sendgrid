import smtplib, ssl,os
from resources.names import names
import random

port = 465
smtp_server_domain_name = "smtp.gmail.com"
sender_mail = "mikkelrevmann@gmail.com"
password = os.environ.get('GMAIL_PASS')

ssl_context = ssl.create_default_context()
service = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
service.login(sender_mail, password)

hemmelig_venn = names[random.randint(0, len(names))]["name"]
budsjett = round(random.expovariate(0.005).real)

service.sendmail(sender_mail, "mikal.stapnes@visma.com", f"Subject: Hei, din hemmelige venn er {hemmelig_venn}\nog budsjettet ditt er {budsjett} ,- ")

service.quit()