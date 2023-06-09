# Imports
import os
import click
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import warnings
import logging

# Remove unnecessary logging and warnings
warnings.filterwarnings("ignore")
logging.disable(logging.WARNING)

def generate_image(pipe, prompt, save_path):
    # Make a prediction
    image = pipe(prompt=prompt).images[0]
    image.save(save_path)
    
    
@click.command()
@click.option(
    "--image", type=click.Path(exists=True), help="Path to image to be captioned"
)
@click.option(
    "--folder",
    type=click.Path(exists=True),
    help="Path to folder of images. If no extension is passed, all images will be used.",
)
@click.option(
    "--ext",
    type=str,
    help="Extension of images to be captioned. If no extension is passed, all images will be used. This is only used if a folder of multiple images is passed.",
)
def main(image, folder, ext):
    # Instantiate the pipelines
    image_to_text = pipeline(
        "image-to-text", model="nlpconnect/vit-gpt2-image-captioning"
    )
    
    text_to_image_model = "CompVis/stable-diffusion-v1-4"
    text_to_image = StableDiffusionPipeline.from_pretrained(text_to_image_model)
    
    # If an image is passed in, generate a caption for it
    if image:
        image_name = os.path.split(image)[-1]
        summary = image_to_text(image)[0]["generated_text"]
        print(f"{image_name}: {summary}")
        
        # Generate an image
        save_path = os.path.join(os.path.split(image)[0], image_name.split(".")[0] + "_generated.jpg")
        generate_image(text_to_image, summary, save_path)

    # If a folder is passed in, generate captions for all images in the folder
    elif folder:
        images = os.listdir(folder)
        # Only keep images with the specified extension if one is passed
        if ext:
            images = [image for image in images if image.endswith(ext)]
            if len(images) == 0:
                print(f"No images with extension {ext} found in {folder}.")
                return

        # Generate captions for each image
        for image in images:
            summary = image_to_text(os.path.join(folder, image))[0]["generated_text"]
            print(f"{image}: {summary}")
            
            # Generate images
            save_path = image.split(".")[0] + "_generated.jpg"
            generate_image(text_to_image, summary, save_path)
