from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='ponchi',
    version='0.0.1',
    author='ommatotritonophryticus',
    description='Simple telegram bot create library',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/ommatotritonophryticus/ponchi',
    #packages=['ponchi', 'ponchi.clear_app', 'ponchi.databases', 'ponchi.contrib'],
    packages=find_packages(),
    install_requires=['aiogram==3.4.1', 'redis==5.0.3'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='telegram aiogram telegram-bot',
    project_urls={
        'GitHub': 'https://github.com/ommatotritonophryticus/ponchi'
    },
    python_requires='>=3.10'
)
