from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model from Hugging Face
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Use the free GPU from Colab

# Function to generate an image based on a text prompt
def generate_image(prompt):
    image = pipe(prompt).images[0]  # Generate image
    image.save("generated_image.png")  # Save the image
    return image                                                                                                                                           

# Get user input for the prompt
prompt = input("Describe the image you want to generate: ")
image = generate_image(prompt)

# Show the image in Colab
image.show() 
