from mailjet_rest import Client
import os


def send_mail(sub,content,to):
    api_key = os.environ.get('API_KEY')
    api_secret = os.environ.get('SECRET_KEY_API')
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": os.environ.get('EMAIL'),
            "Name": "Amar A.J"
        },
        "To": [
            {
            "Email": f"{to.email}",
            "Name": f"{to.first_name} {to.last_name}"
            }
        ],
        "Subject": f"{sub}",
        "TextPart": "",
        "HTMLPart": f"{content}",
        "CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.json())
    return result.status_code

def SignUpMail(to,link):
    sm = send_mail(sub="SignUp Verification",content=f'<h3>Klick <a herf="{link}">here</a> to verify your email.</h3>',to=to)
    if sm == 200:
        print(f"SignUp Verification to : {to.email} sent sucssesfuly")
    else:
        print(f"SignUp Verification to : {to.email} Field ")
        
    
    