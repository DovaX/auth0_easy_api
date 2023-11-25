import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='auth0_easy_api',
    version='1.0.2',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='A Python wrapper around Auth0 Authentication API and Management API to make setup and basic operations easier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/auth0_easy_api',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'flask','pyjwt','dogui'
     ],
    python_requires='>=3.6',
)
    