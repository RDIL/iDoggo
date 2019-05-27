import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iDoggo",
    version="2.1.0",
    author="RDIL",
    author_email="me@rdil.rocks",
    description="Text dog library in Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheICC/iDoggo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
    ],
    project_urls={
        "Bug Tracker": "https://github.com/TheICC/iDoggo/issues",
        "Source Code": "https://github.com/TheICC/iDoggo",
        "Documentation": "https://github.com/TheICC/iDoggo/blob/master/README.md"
    }
)
