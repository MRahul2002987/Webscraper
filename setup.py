from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open("requirements.txt", "r", encoding="utf8") as f:
    requirements = f.read().splitlines()

# Filter out any lines that are comments or empty
requirements = [req for req in requirement if req and not req.startswith("#")]

setup(
    name='Webscraper',
    version='0.1.0',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MRahul2002987/Webscraper',
    author='MRahul2002987',
    author_email='mujerahul@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': [
            # List your development dependencies here
            # For example:
            # 'pytest>=3.7',
        ],
    },
    python_requires='>=3.6, <4',
)