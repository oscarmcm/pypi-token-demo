from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='random_names',
    version='0.0.2',
    description='A sample PyPI Tokens demo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/oscarmcm/pypi-tokens-demo',
    author='Oscar Cortez',
    author_email='oscarmcm@pm.me',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='sample pypi random name',
    py_modules=['main'],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'random_name=main:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/oscarmcm/pypi-tokens-demo/issues',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/oscarmcm/',
    },
)

