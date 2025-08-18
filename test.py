import google.generativeai as genai

genai.configure(api_key="AIzaSyBYJunwnZ5D9PYaP92VdOuV7IUmy82OfCw")

models = genai.list_models()
for m in models:
    print(m.name, "—", m.supported_generation_methods)