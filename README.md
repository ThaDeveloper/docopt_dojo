# Docopt Dojo

[![Build Status](https://travis-ci.org/ThaDeveloper/docopt_dojo.svg?branch=master)](https://travis-ci.org/ThaDeveloper/docopt_dojo)
[![Coverage Status](https://coveralls.io/repos/github/ThaDeveloper/docopt_dojo/badge.svg?branch=master)](https://coveralls.io/github/ThaDeveloper/docopt_dojo?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8a41c518a9f493cba775e1e97f3e655)](https://www.codacy.com/app/ThaDeveloper/docopt_dojo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ThaDeveloper/docopt_dojo&amp;utm_campaign=Badge_Grade)

Docopt Dojo is a command-line Room Alloction System.

__*Statement*__

The main objective of the project is to model a room allocation system for Andela facilities.

__*Problem Description*__

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise you will be required to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

__*Constraints*__

The Dojo has rooms, which can be offices or living spaces. An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

***

__*Sample Commands and Output*__

> *Sample input with one office*

`(Dojo)==> create_room office Orange`
> *Sample output with one office*

`An office called Orange has been successfully created!`

> *Sample input with multiple offices*

`(Dojo)==> create_room office Blue Black Brown`

> *Sample output with multiple offices*
```
An office called Blue has been successfully created!
An office called Black has been successfully created!
An office called Brown has been successfully created!
```

![alt text](https://github.com/ThaDeveloper/docopt_dojo/blob/master/assets/test_sample.png "Test sample output")

## Installation

To set up dojo, make sure that you have python and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Clone the Repo into a folder of your choice
```
git clone https://github.com/ThaDeveloper/docopt_dojo.git
```

Create a virtual enviroment.
```
virtualenv venv
```

Navigate to the root folder.
```
cd docopt_dojo
```

Install the packages.
```
pip install -r requirements.txt
```

Confirm your installed packages
```bash
$ pip freeze
```

## Usage

To get the app running...

```bash
$ python app.py
```

## Credits

[Justin Ndwiga](https://github.com/ThaDeveloper)

The amazing fellows at [Andela](https://www.andela.com)

## License

### MIT License

Copyright (c) 2017 **Justin Ndwiga**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


