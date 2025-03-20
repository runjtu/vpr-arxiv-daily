import os, openai
from openai import OpenAI
import tiktoken

class OpenAIClient:
    def __init__(self, api_key, default_url="https://api.openai.com", model_name="gpt-4o-2024-05-13"):

        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url=default_url + '/v1')

    def send_message(self, prompt_content):


        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt_content,
                },
            ],
        )
        
        return response.choices[0].message.content