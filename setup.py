import sys
from setuptools import setup, find_packages

requirements = ['flask', 'flask-restful', 'flask-cors', 'webargs']

setup(
    name='rvau-api',
    version='0.1',
    url='',
    license='BSD',
    author='Brian Brown',
    author_email='brbrowngeo@gmail.com',
    description='League API application',
    packages=find_packages(),
    package_data = {},
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])