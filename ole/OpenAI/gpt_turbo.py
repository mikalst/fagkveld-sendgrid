from openai import OpenAI


def generate_gpt_text_from_prompt(client: OpenAI, prompt, system_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=
        [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
    )
    
    print(response)
    print(response.choices[0].message.content)

    return response.choices[0].message.content

# https://platform.openai.com/docs/guides/text-generation/json-mode