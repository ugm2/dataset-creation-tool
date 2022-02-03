import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="imagines",
    version="0.0.2",
    author="Unai Garay",
    author_email="unaigaraymaestre@gmail.com",
    description="ImagineS (Image Engine Search) tool augments an image dataset by searching a series of queries in Google Images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ugm2/ImagineS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)