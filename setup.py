import setuptools

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="uchu-cli",
    version="0.1.0",
    description="A CLI based tool for working with the Uchu API",
    author="Jettford",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UchuServer/cli",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 