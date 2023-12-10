import os
import src.image_text as image_text
import src.dalle3 as dalle3

from dotenv import load_dotenv
import openai
from openai import AzureOpenAI

load_dotenv()

OPENAI_API_TYPE = "azure"
OPENAI_API_BASE = "https://oai-twoday-testing-2.openai.azure.com/"
OPENAI_API_VERSION = "2023-12-01-preview"
OPENAI_API_KEY = ""

def createOpenAIClient():
    api_key=os.environ.get('OPENAI_API_KEY')

    if (api_key == None):
        print("Missing api key. Create .env file with  'OPENAI_API_KEY' eqaul to api key. ")
        exit()

    client = AzureOpenAI(api_key=api_key, azure_endpoint=OPENAI_API_BASE, api_version=OPENAI_API_VERSION)

    return client

def generate_text(client: AzureOpenAI, gpt_prompt: str, gpt_system_message: str, deployment: str="gpt-4"):
    response = client.chat.completions.create(
        model=deployment,
        messages=
        [
            {"role": "user", "content": gpt_prompt},
            {"role": "system", "content": gpt_system_message},
        ],
        temperature=0.6,
    )
    
    return response.choices[0].message.content

def generate_image_b64(client: AzureOpenAI, dalle_prompt: str):
    # size:  1024x1024 | 1024x1792 | 1792x1024 
    # Quality: standard | hd
    # n: number of images generated

    image_object = client.images.generate(
        model="dall-e-3",
        prompt=dalle_prompt,
        size="1024x1024",
        n=1
    )

    return image_object

def createChristmasCard(dalle_image_prompt: str, gpt_prompt: str, gpt_system_message: str, run_without_open_ai: bool, gpt_deployment: str = "gpt-4"):
    if (run_without_open_ai):
        stored_file_jpeg_path = "GeneratedImages/jpeg/Realistic_2023-12-04_19-32-42.jpeg"
        with open("text.txt", 'r') as input_file:
            message = input_file.read()

        image_text.put_text_on_image(
            input_image_path=stored_file_jpeg_path, 
            text_content=message
        )

        return
    
    client = createOpenAIClient()

    message = generate_text(client, gpt_prompt, gpt_system_message, deployment=gpt_deployment)



    image_text.put_text_on_image(
        input_image_path=stored_file_jpeg_path, 
        text_content=message
    )

# generer tilfeldig tekster til bilde i en loop som sender mail med Mikal sin
# createChristmasCard(
#     dalle_image_prompt="Realistisk snømann",
#     gpt_prompt="create a cozy, warm and short christmas message to your grandma. Max 200 words",
#     gpt_system_message='you are an software developer who misses your grandma'
# )