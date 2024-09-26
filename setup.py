from setuptools import setup, find_packages

setup(
    name='pycsi',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[
        "tomlkit",
    ],
    author='Gordon Greene',
    author_email='greeng3@obscure-reference.com',
    description='PyCSI - tools for the analysis of python code..',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/greeng3/greeng3_python',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
