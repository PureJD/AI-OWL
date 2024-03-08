import os
from openai import OpenAI

def open_ai_chat(question):
    # Retrieve the API key securely from an environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
# Retrieve the API key securely from an environment variable
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a wise owl in the dark surrounded by fireflies. You offer advice and answer questions in the voice of an owl"},
                {"role": "user", "content": f"{question}"}
            ]
        )

        # Assuming there's at least one choice in the response and you want the message content of the first choice
        if response.choices:
            generated_message_content = response.choices[0].message.content  # Access the 'content' attribute of the 'message'
            print(generated_message_content)
        else:
            print("No choices were returned.")

    except UnicodeEncodeError as e:
        print(f"Unicode encoding error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return generated_message_content
