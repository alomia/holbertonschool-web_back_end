# 0x00. Python - Variable Annotations

### Welcome!

Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

- Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
- Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

![r/ProgrammerHumor - strongly statically typed weakly dynamically typed JS *strongly dynamically typed* python](https://preview.redd.it/y9y25tefi5401.png?width=960&crop=smart&auto=webp&s=222120ab49d9f98c87734ed60e8a4d2095fa6f57)

------

### Resources

- [Python 3 typing documentation](https://intranet.hbtn.io/rltoken/AgrgHs3ohrFJnT3Eece1UQ)
- [MyPy cheat sheet](https://intranet.hbtn.io/rltoken/iEWC38l9R9216w1Y-x8pMg)

------

### Learning Objectives

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy