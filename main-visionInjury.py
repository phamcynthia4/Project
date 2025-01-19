import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties like voice and speech rate (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)


# from groq import Groq
# import base64


# # Function to encode the image
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # Path to your image
# image_path = "C:/Users/phamc/Downloads/a2e7c170-79ba-11ef-8547-c93707d8f8aa.png"

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
#                 {"type": "text", "text": "Provide advice to the image as if a 911 responder and suggest 911 only if urgent and very severe"},
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
                    "text": "Every image is an image of a problem. Provide advice to the image as if a 911 responder and suggest 911 only if urgent and very severe. If the problem is severe and requires 911, put the numbers 911 as the first thing in the output. Then suggest next step the individual must take in this situation."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.twopedsinapod.org/wp-content/uploads/2016/03/splinter.png"
                    }
                }
            ]
        },
         {
            "role": "user",
            "content": "Tell me more about the solution"        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
# Convert text to speech
def text_speech():
    text = completion.choices[0].message
    engine.say(text)
    engine.runAndWait() #wait for speech to run

