# Imports
import os
import click
from transformers import pipeline
import warnings
import logging

# Remove unnecessary logging and warnings
warnings.filterwarnings("ignore")
logging.disable(logging.WARNING)


def generate_caption(pipe, image_path):
    # Make a prediction
    summary = pipe(image_path)[0]["generated_text"]

    # Print the results
    print(f"{os.path.split(image_path)[-1]}: {summary}")


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
    # Instantiate the pipeline
    image_to_text = pipeline(
        "image-to-text", model="nlpconnect/vit-gpt2-image-captioning"
    )

    # If an image is passed in, generate a caption for it
    if image:
        summary = image_to_text(image)[0]["generated_text"]
        print(f"{os.path.split(image)[-1]}: {summary}")

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