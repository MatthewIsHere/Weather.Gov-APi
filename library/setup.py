import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WeatherNWS",
    version="0.0.1",
    author="Matthew Lyon",
    author_email="matthew@matthewlyon.net",
    description="Weather Functions and Data From NWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatthewIsHere/Weather.Gov-APi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
