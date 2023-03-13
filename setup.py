from setuptools import setup, find_packages

setup(
    name='OathWarden',
    version='1.0.0',
    description='Python Package for Twitch requests',
    author='Yokozuna',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
)