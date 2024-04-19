from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="SwiftML",
    version="0.1.0",
    author="Arpit Sengar (arpy8)",
    author_email="arpitsengar99@gmail.com",
    description="A tool to automate end-to-end machine learning model development and deployment with high level of abstraction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arpy8/SwiftML",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "openpyxl",
        "scikit-learn",
        "pycaret",
        "phik",
        "streamlit-on-hover-tabs",
        "streamlit_custom_ydata_profiling",
        "tqdm",
        "termcolor",
    ],
    entry_points={
        "console_scripts": [
            "swiftml=SwiftML.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    license="MIT",
    package_data={'SwiftML': ['*.png', '*.css', '*.csv', '*.html']},
)