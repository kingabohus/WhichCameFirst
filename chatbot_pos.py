API_key = "AIzaSyCIH6d_mtIYuEt0r3y3JrXcOfjFqkkKg0k"

from google import genai

client = genai.Client(api_key=API_key)

with open('historic_inventions_plain.txt', 'r') as file:

    for line in file:
        query = "The following sentence talks about the invention of what thing? Answer only with the name of the thing. \"{}\"".format(line)
        response = client.models.generate_content(model="gemini-2.0-flash",contents=query)

        print(response.text)
        f = open("chatbot_resps.txt", "a")
        f.write(response.text)
        f.write("\n")
        f.close()

# response = client.models.generate_content(model="gemini-2.0-flash",contents="hello")
#
# print(response.text)




#
# from openai import OpenAI
# API_key = "sk-ecc1c5e74462433593f1c33c50cce2c1"
# client = OpenAI(api_key=API_key, base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "The following sentence talks about the invention of what? Only answer with the name. \"The first Zeppelin is designed by Theodor Kober.\""},
#     ],
#     stream=False
# )
#
# print(response.choices[0].message.content)
