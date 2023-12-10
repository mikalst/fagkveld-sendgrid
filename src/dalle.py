from settings import OPENAI_API_BASE, OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_VERSION
import openai 


# bruker ikke denne 
openai.api_type = OPENAI_API_TYPE
openai.api_base = OPENAI_API_BASE
openai.api_version = OPENAI_API_VERSION
openai.api_key = OPENAI_API_KEY

small_size = '256x256'
medium_size = '512x512'
large_size = '1024x1024'

def createImage(prompt: str, size='1024x1024'):

    response = openai.Image.create(
        prompt=prompt,
        size=size,
        n=1,
        # response_format="b64_json",
    )

    image_url = response["data"][0]["url"]
    print(response["data"])
    return image_url