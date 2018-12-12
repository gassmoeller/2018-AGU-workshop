import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_analysis",
    version="0.0.1",
    author="Rene Gassmoeller",
    author_email="someone@example.com",
    description="A bunch of data analysis routines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gassmoeller/2018-AGU-workshop",
    packages=setuptools.find_packages(),
    install_requires=["numpy","requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
