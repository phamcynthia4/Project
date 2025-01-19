# from groq import Groq
# import base64


# # Function to encode the image
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # Path to your image
# image_path = "C:/Users/phamc/Downloads/Photos-001/DSC_1020_2.JPG"

# # Getting the base64 string
# base64_image = encode_image(image_path)

# client = Groq(
#     api_key="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",
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "What's in this image?"},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_image}",
#                     },
#                 },
#             ],
#         }
#     ],
#     model="llama-3.2-11b-vision-preview",
# )

# print(chat_completion.choices[0].message.content)


from groq import Groq

client = Groq(
     api_key="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",
)
completion = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Provide advice to the image as if a 911 responder and suggest 911 only if urgent and very severe"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://i.redd.it/ny8y66ev27sc1.jpeg"
                    }
                }
            ]
        },
         {
            "role": "user",
            "content": "Tell me more about the solution"
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)

