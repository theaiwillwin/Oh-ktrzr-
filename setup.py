from setuptools import setup, find_packages

setup(
    name='scalar_field_simulations',
    version='0.1',
    description='Toolkit for scalar field evolution simulation using multiple methods',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'mpi4py',
        'fenicsx'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
