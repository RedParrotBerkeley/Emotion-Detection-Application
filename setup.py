# setup.py

from setuptools import setup, find_packages

setup(
    name="final_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # Add other dependencies here if necessary
    ],
    author="RedParrotBerkeley",
    author_email="NANA@example.com",
    description="A package for detecting emotions using the Watson NLP Library's Emotion Predict API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RedParrotBerkeley/EmotionDetection",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
