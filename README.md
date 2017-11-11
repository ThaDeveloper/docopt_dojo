__DOCOPT_DOJO__

[![Build Status](https://travis-ci.org/ThaDeveloper/docopt_dojo.svg?branch=master)](https://travis-ci.org/ThaDeveloper/docopt_dojo)
[![Coverage Status](https://coveralls.io/repos/github/ThaDeveloper/docopt_dojo/badge.svg?branch=master)](https://coveralls.io/github/ThaDeveloper/docopt_dojo?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8a41c518a9f493cba775e1e97f3e655)](https://www.codacy.com/app/ThaDeveloper/docopt_dojo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ThaDeveloper/docopt_dojo&amp;utm_campaign=Badge_Grade)

Docopt command line in python: Room alloction in the terminal

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
