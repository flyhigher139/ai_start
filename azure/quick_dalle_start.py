import os
import requests
import json
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
# openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

# This will correspond to the custom name you chose for your deployment when you deployed a model.
deployment_name = 'gpt-35-turbo'
openai.api_version = '2023-06-01-preview'

# Create an image using the image generation API
generation_response = openai.Image.create(
    prompt='''Imagine a lone mail figure standing at the edge of a vast, still lake. 
    The water stretches out before them, reflecting the colors of the sunset in a perfect mirror image. 
    The figure stands tall and proud, their silhouette stark against the horizon. 
    In the background, a mountain range rises up to meet the sky, shrouded in mist. 
    The air is still, except for the occasional chirping of crickets and the gentle lapping of water against the shore. 
    The scene is both serene and haunting, evoking a sense of peace and tranquility amidst a world of unknown possibilities.
    ''',
    size='1024x1024',
    n=2
)

image_url = generation_response["data"][0]["url"]  # extract image URL from response
print(image_url)

# # Set the directory where we'll store the image
# image_dir = os.path.join(os.curdir, 'images')
# # If the directory doesn't exist, create it
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)
#
# # With the directory in place, we can initialize the image path (note that filetype should be png)
# image_path = os.path.join(image_dir, 'generated_image.png')
#
# # Now we can retrieve the generated image
# generated_image = requests.get(image_url).content  # download the image
# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image)
#
# # # Display the image in the default image viewer
# # display(Image.open(image_path))
