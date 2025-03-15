import google.generativeai as genai

genai.configure(api_key="AIzaSyCQD7y4oZ3Fk_YVx_8_62PzKG-Rz3Jn7Ws")

models = genai.list_models()

for model in models:
    print(model.name)
