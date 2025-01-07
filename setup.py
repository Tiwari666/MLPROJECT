from setuptools import setup, find_packages

setup(
    name='my_ml_project',  # Name of your project
    version='0.1.0',  # Version number of your project
    author='Narendra Tiwari',  # Your name
    author_email='narendra76052@gmail.com',  # Your email address
    description='A small machine learning project',  # A short description of your project
    long_description=open('README.md').read(),  # A long description read from the README file
    long_description_content_type='text/markdown',  # Type of the long description, here markdown
    url='http://github.com/Tiwari666/my_ml_project',  # Link to your project's GitHub repo
    packages=find_packages(),  # Automatically find and include all packages in your project
    install_requires=[
        'numpy',  # Numpy library as a dependency
        'pandas',  # Pandas library for data manipulation
        'scikit-learn>=0.24',  # Specific version of Scikit-Learn or any other dependency
        'matplotlib'  # Matplotlib for plotting
    ],
    python_requires='>=3.12',  # Minimum version of Python required for your project
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status of your project
        'Intended Audience :: Developers',  # Intended audience
        'License :: OSI Approved :: MIT License',  # License as per OSI standards
        'Programming Language :: Python :: 3',  # Programming language
        'Programming Language :: Python :: 3.12',  # Specific version of Python
        'Operating System :: OS Independent',  # Compatible OS
    ],
    keywords='machine learning, data science, pandas',  # Keywords to find your project
    project_urls={  # Optional project URLs
        'Bug Reports': 'https://github.com/Tiwari666/my_ml_project/issues',
        'Source': 'https://github.com/Tiwari666/my_ml_project/',
    },
)
