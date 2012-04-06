from setuptools import setup, find_packages

setup(
    name='piston-oauth-biped',
    version="0.1",
    packages = find_packages(),
    install_requires = [
        'django-piston',
        'oauth2'
    ],
)
