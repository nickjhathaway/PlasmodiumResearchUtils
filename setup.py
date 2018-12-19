import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PlasmodiumResearchUtils",
    version="0.0.1",
    author="Nicholas Hathaway",
    author_email="nickjhathaway@gmail.com",
    description="A small set of tools to aid in Plasmodium research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickjhathaway/PlasmodiumResearchUtils",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
    ),
)

