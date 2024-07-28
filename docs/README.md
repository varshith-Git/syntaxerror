# Typo: Python Code to Syntax-Free Representation Converter

## Overview

`typo` is a Python package designed to convert Python code into a syntax-free representation. This tool can be useful for educational purposes, code analysis, or preparing code for various transformation pipelines. The package is straightforward to use and provides a direct way to strip Python code down to its essential structure without syntax.

## Features

- **Syntax-Free Conversion**: Converts Python code into a syntax-free representation.
- **Comment Removal**: Option to remove comments from Python code.
- **Docstring Removal**: Option to remove docstrings from Python code.
- **Function Extraction**: Extract function names from Python code.
- **Syntax Validation**: Validate the syntax of Python code.
- **Easy to Use**: Simple and intuitive API.

## Installation

Install `typo` via pip:

```sh
pip install typo
```
## Usage

```sh
from typo import sf

code = """
def hello_world():
    print('Hello, world!')
"""

print(sf(code))

```