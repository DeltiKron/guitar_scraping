from setuptools import setup, find_packages

setup(
    name='guitar_scraping',
    version='1.0.0',
    url='foo',
    author='Carl Schaffer',
    author_email='cfmschaffer@hotmail.de',
    description='Guitar scraping analysis',
    packages=find_packages(),
    install_requires=['matplotlib', 'sqlalchemy', 'pandas','beautifulsoup4'],
)