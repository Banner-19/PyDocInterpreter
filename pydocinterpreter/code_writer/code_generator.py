# Code Writer
import openai

openai.api_key = 'YOUR_API_KEY'

def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    code = response.choices[0].text.strip()
    return code