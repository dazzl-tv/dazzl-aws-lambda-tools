import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dazzl',
    version='0.1',
    author='VAILLANT Jeremy',
    author_email='jeremy@dazzl.tv',
    description='Library python for simplify to create lambda function (AWS lambda) and Dazzl API service.',
    long_description=long_description,
    long_desciption_content_type="text/markdown",
    url='http://github.com/dazzl-tv/dazzl-aws-lambda-tools.git',
    packages=setuptools.find_packages(),
    install_requires=[
        'os',
        'logging',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
