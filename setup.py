from setuptools import setup, find_packages
import os


with open("docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Utility function to read the README file.
# Used for the long_description. It's nice, because now:
# 1) we have a top-level README file and
# 2) it's easier to type in the README file than to put a raw string in below ...

setup(
    name="typo",
    version="0.1.0",
    author="Gudur Varshith",
    author_email="varshith.gudur17@gmail.com",
    description="typo is a Python package designed to convert Python code into a syntax-free representation. This tool can be useful for educational purposes, code analysis, or preparing code for various transformation pipelines.",
     long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varshith-Git/typo",
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "required_package1>=1.0",
        "required_package2>=2.0",
        # Add other dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=5.4.1",
            "sphinx>=3.0.3",
            "black",
            "flake8",
            "mypy",
            # Add other development dependencies here
        ],
    },
    entry_points={
        "console_scripts": [
            "project_name=project_name.module:main_function",
        ],
    },
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
        # Include all data files under data
        "project_name": ["data/*.dat"],
    },
    include_package_data=True,
    data_files=[
        # Include data files in distribution
        ("data", ["data/sample_data.dat"]),
    ],
    zip_safe=False,
)
