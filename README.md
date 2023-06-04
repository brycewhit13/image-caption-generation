# Image Caption Generation

[![Python Continuous Integration](https://github.com/brycewhit13/image-caption-generation/actions/workflows/main.yaml/badge.svg)](https://github.com/brycewhit13/image-caption-generation/actions/workflows/main.yaml)

## Description

This CLI tool allows you to generate captions for images automatically. This is accomplished using the [ViT GPT2 Image Captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) model from [Hugging Face](https://huggingface.co/). For example, if the following image is input into the model, it will produce the following caption:

![Example](assets/demo.jpeg)

```a soccer player kicking a soccer ball```

Once a caption is generated, it is then passed to the [Stable Diffusion v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) model to generate an image. This image is saved in the same folder where the original image exists with `_generated.jpg` appended to the end of the new file name. This allows user to compare how the generated image from the caption compares to original.

Here is an example of what a generated image may look like using the caption above. 

![Example Image](assets/generated_image.jpeg)

## Architecture

![Architecture](assets/Architecure_diagram.png)

## How to Run

### Setup the environemnt

```make setup```

This upgrades pip, installs the requirements from `requirements.txt` and then runs `python setup.py develop`

### Run on a single image

```caption --image [IMAGE_PATH]```

To try on your own, you can test it with the following command. This should produce a single caption for an image of a cat running.

```caption --image examples\cat_running.jpeg```

### Run on an entire folder

The following command will run the program for every file in a given folder

```caption --folder [FOLDER_PATH]```

To try on your own, you can test it out with the following command. This should produce three captions for three different images.

```caption --folder examples```

### Run on a partial folder

The following command will allow you to provide an extension so only files with the given extension are processed.

```caption --folder [FOLDER_PATH] --ext [EXTENSION]```

To try on your own, you can test it out with the following command. This should produce two captions. 

```caption --folder examples --ext jpeg```