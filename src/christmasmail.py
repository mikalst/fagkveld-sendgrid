
def generate_christmas_email(overskrift, url, avsender, toUserEmail):
    email_msg = {
        'Message': {
            'Subject': f"{overskrift}",
            'Body': {
                'ContentType': 'HTML', 
                'Content': html_content(overskrift, url, avsender),
            },
            'ToRecipients': [
                {
                    'EmailAddress': {
                            'Address': toUserEmail
                    }
                }
            ]
        }
    }

    return email_msg


def html_content(overskrift, bildeURL, avsender):
    result = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Christmas Greetings</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f2f2f2;
                    margin: 0;
                    padding: 0;
                }}
        
                .container {
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #C94057;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
        
                h1 {
                    text-align: center;
                    color: #ffffff;
                }
        
                p {
                    color: #ffffff;
                    line-height: 1.6;
                }
        
                img {
                    max-width: 100%;
                    height: auto;
                    border: 2px solid #ddd;
                    border-radius: 10px;
                    margin-top: 20px;
                }
        
                .footer {
                    text-align: center;
                    margin-top: 20px;
                }
            </style>
            </head>
            <body>
        '''

    result += f'''
        <div class="container">
            <h1>{overskrift}</h1>
            
            <img src="{bildeURL}" alt="Christmas Greetings" />
        
            <p>Hilsen,</p>
            <p>{avsender}</p>
        
            <div class="footer" />
        </div>
        </body>
        </html>
    '''
    
    return result