# from transformers import AutoTokenizer, AutoModelForCausalLM

# class Generator:
#     def __init__(self, model_name):
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.model = AutoModelForCausalLM.from_pretrained(model_name)

#     def generate(self, prompt, max_length=200):
#         inputs = self.tokenizer(prompt, return_tensors="pt")

#         outputs = self.model.generate(
#             inputs["input_ids"],
#             max_length=150,
#             temperature=0.3,
#             do_sample=True
#         )

#         return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

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