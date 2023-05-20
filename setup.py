from setuptools import setup, find_packages

# Get the requirements from the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="caption",
    description="An Image Captioning Tool",
    packages=find_packages(),
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        caption=caption.generate_caption:generate_caption
    """,
    version="0.1.0",
    author="Bryce Whitney",
    url="https://github.com/brycewhit13/image-caption-generation",
)
