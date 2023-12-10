import msal
import os
from dotenv import load_dotenv

def generate_app() -> msal.PublicClientApplication:
    client_id = 'f18479c4-0d4e-4620-a435-ab3fe06ee275'
    tenant_id = 'ba9d7305-30ed-42ca-8b54-65d98d0f2a29'
    authority = f"https://login.microsoftonline.com/{tenant_id}"

    app = msal.PublicClientApplication(client_id=client_id, authority=authority)

    return app

def generate_app(app: msal.PublicClientApplication) -> dict:

    scopes = ["mail.send"]

    flow = app.initiate_device_flow(scopes)

    print(f"Go to {flow["verification_uri"]} and put in {flow["user_code"]}")

    return flow

def get_access_token(app, flow):
    
    result = app.acquire_token_by_device_flow(flow)

    print(result)

    return result["access_token"]


def get_secret_access_token():
    load_dotenv()

    client_id = 'f18479c4-0d4e-4620-a435-ab3fe06ee275'
    client_secret = os.getenv("AZUREAD_CLIENT_SECRET")

    tenant_id = 'ba9d7305-30ed-42ca-8b54-65d98d0f2a29'
    authority = f"https://login.microsoftonline.com/{tenant_id}"

    scopes = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority)

    result = app.acquire_token_for_client(scopes=scopes)

    print(result)

    return result["access_token"]