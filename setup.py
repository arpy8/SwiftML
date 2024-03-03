from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="unityml",
    version="0.0.1",
    author="Arpit Sengar (arpy8)",
    author_email="arpitsengar99@gmail.com",
    description="This package lauches the web app locally for unityml.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arpy8/unityml",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "pycaret",
        "termcolor",
        "streamlit",
        "tqdm",
        "openpyxl",
        "streamlit-on-hover-tabs"
    ],
    entry_points={
        "console_scripts": [
            "unityml=unityml.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    license="MIT",
    package_data={'unityml': ['*.png', '*.css', '*.csv', '*.html']}, 
)