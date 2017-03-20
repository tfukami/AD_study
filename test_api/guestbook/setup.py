from setuptools import setup, find_packages

setup(
    name='guestbook',
    version='1.0.0',
    packages=find_packages(),
    include_pacage_data=True,
    install_requires=[
        'Flask',
    ],
)
