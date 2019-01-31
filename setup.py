from setuptools import setup
import phoopy.kernel

long_description = open('README.rst', 'r').read()

setup(
    name='phoopy-kernel',
    version=phoopy.kernel.__version__,
    packages=['phoopy', 'phoopy.kernel'],
    setup_requires=['wheel'],
    install_requires=['phoopy-yaml>=1.1.2,<1.2.0'],
    description="Kernel of phoopy framework",
    long_description=long_description,
    url='https://github.com/phoopy/phoopy-kernel',
    author='Phoopy',
    author_email='reisraff@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
