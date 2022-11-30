from sendgrid_dynamic import sendmail
from random import shuffle

from resources.names import names

print(len(names))

def gi_gave(per1, per2):
    print(per1["name"], " gir gave til ", per2["name"])
    # sendmail(per1["name"], per2["email"])

shuffle(names)

for i in range(0, len(names)-1):
    gi_gave(names[i], names[i+1])

gi_gave(names[len(names) - 1], names[0])

