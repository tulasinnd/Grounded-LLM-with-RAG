from ollama import chat


class Generator:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self, prompt):
        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content