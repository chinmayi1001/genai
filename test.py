import google.generativeai as palm
import os
import time
palm.configure(api_key='AIzaSyDuaob78SCgiUH_COrOASqftj2tycYetcE')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

file_path = 'C:\\Users\\Chinmayee\\Desktop\\genaihack\\a.txt'

with open(file_path, 'r') as file:
    text_to_guess = file.read()

prompt = """
Guess the coding language :
"""+text_to_guess

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)