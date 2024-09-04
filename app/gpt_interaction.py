import openai
from config import config

# Set up OpenAI API key
openai.api_key = config.OPENAI_API_KEY

def interact_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
