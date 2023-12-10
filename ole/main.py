from OpenAI import dalle3, gpt_turbo
from dotenv import load_dotenv
from Image import image_text
from openai import OpenAI
import os

load_dotenv()

def createOpenAIClient():
    api_key=os.environ.get('OPENAI_API_KEY')

    if (api_key == None):
        print("Missing api key. Create .env file with  'OPENAI_API_KEY' eqaul to api key. ")
        exit()

    client = OpenAI(api_key=api_key)

    return client


def createChristmasCard(dalle_image_prompt: str, gpt_prompt: str, gpt_system_message: str, run_without_open_ai: bool):
    if (run_without_open_ai):
        stored_file_jpeg_path = "GeneratedImages/jpeg/Realistic_2023-12-04_19-32-42.jpeg"
        with open("text.txt", 'r') as input_file:
            message = input_file.read()

        image_text.putTextOnImage(
            image_path=stored_file_jpeg_path, 
            text_content=message
        )

        return
    
    
    client = createOpenAIClient()
    message = gpt_turbo.generate_gpt_text_from_prompt(
        client=client,
        prompt=gpt_prompt,
        system_message=gpt_system_message
    )

    stored_file_jpeg_path = dalle3.generate_dalle_image_from_prompt(
        client, 
        dalle_image_prompt, 
        size="1024x1024"
    )

    image_text.putTextOnImage(
        image_path=stored_file_jpeg_path, 
        text_content=message
    )



# generer tilfeldig tekster til bilde i en loop som sender mail med Mikal sin
# createChristmasCard(
#     dalle_image_prompt="Realistisk snømann",
#     gpt_prompt="create a cozy, warm and short christmas message to your grandma. Max 200 words",
#     gpt_system_message='you are an software developer who misses your grandma'
# )

createChristmasCard(
    dalle_image_prompt="Realistisk snømann",
    gpt_prompt="Lag en kort koselig julehilsen til min gode kollega, Mikal",
    gpt_system_message='Jeg heter Ole Martin og er en software developer som ønsker Mikal en god jul',
    run_without_open_ai=False
)







