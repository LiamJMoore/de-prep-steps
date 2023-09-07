# Data Engineering Pre-Course Exercises

## Purpose
These exercises are intended to give you some experience of writing simple Python code.

## Prerequisites
You need to _fork and clone_ this repository. You should already have watched [this introduction](https://www.youtube.com/watch?v=4VjoJyqQkNQ&ab_channel=Tutor1) to forking and cloning. When you have cloned the repository to the local machine, then open it with Visual Studio Code (or the IDE of your choice).

Before you start, you should have the latest version Python 3 installed. If you have not already done so, follow the steps described in `Preparing For The Course` in the Pre-Course notes.

To test if Python is installed correctly, type at the terminal command prompt:
```bash
python --version
```

You should see something like:
```
Python 3.11.5
```
(The digits will be different depending on what exact version you installed. As long as the version number is higher than 3.9.0, everything should be fine.)
If you don't have python installed then go back to the `Preparing For The Course` section and repeat the steps there, failing that get in touch with us in your pre-course slack channel.

## Installing `pytest`

You will be asked to write some code in the exercise. To check whether you have got it right, we will run some automated tests using a tool called 
`pytest`. You will be learning a _lot_ more about testing in general and `pytest` in particular during the course. For now, please just install 
`pytest` by typing:

```bash
pip install pytest
```
at the command prompt.

You should see various messages telling you that components of the package are being downloaded. Then, to verify that the application has been installed
correctly, type:
```bash
pytest --version
```

You should see a response such as `pytest 7.4.1` or similar.
As before, the version numbers do not need to match exactly. So long as you don't get an error you're go to go 👍 

## Completing and testing the exercises.

There are two types of exercise included here. 

### REPL Exercises

The exercises in Section `01_variables` are intended to be executed in the Python REPL.

The Python _REPL_ (**R**ead **E**valuate **P**rint **L**oop) is a command line tool for running Python code interactively one instruction at a time. 
To start the REPL, just type
```bash
python
```
at the command prompt.

You should see a new Python prompt, like this:

![Python Prompt](./python_prompt.png)

Now, you can type Python code instructions, followed by the `Return` key. 

The exercises invite you to type in various commands, 
predicting what they might do in advance. For example, what might this command do?
```
>>> print('Hello New Northcoder!')
```
To terminate the REPL session, type `exit()` or hit `Ctrl+d`

### Function Exercises

The remaining exercises all require you to write (or rewrite) some Python _functions_. Make sure you have read the pre-course
notes on functions first. Testing how you coded these functions is what we accomplish with `pytest`. 

For example, the file `counter.py` in the `00_demonstration` folder has a very simple function that is going wrong. You
should be able to test this by typing (at the command prompt):
```
pytest -vvv 00_demonstration/counter.py
```

You should see a message saying that one of the tests is failing. Now, in VS Code, navigate to the `counter.py` file. The problem is on Line 17: change the 1 to a 2.

Now, at the terminal prompt re-run the `pytest` command above. You should now see the tests passing. Congratulations! 

In most cases, you will be asked to write or change functions to illustrate different points about Python code. Please do not change the tests themselves, which are written below the function being tested.

Happy Coding!
