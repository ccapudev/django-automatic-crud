import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()


setup(
    name='django-automatic-crud',
    version='1.0.5',
    packages=['automatic_crud'],
    include_package_data=True,
    license='BSD License',
    description='CRUDS Automáticos con Django',
    url='https://github.com/developerpe/django-automatic-crud',
    author='Oliver Sandoval',
    author_email='developerpeperu@gmail.com',
    install_requires=[
        'Django>=2.2',
        'openpyxl==3.0.7',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3'
    ]
)