# Test for API!

This pytest test contains 3 tests for checking various fields returned from the web API. To run the test, clone the repository and follow the instructions below. 

## Creating python virtual environment

The assumption is you already have python3 installed. Enter the commands below in your bash/zsh shell.

    python3 -m venv testenv
    source testenv/bin/activate
    pip install -r requirements.txt

If you are using a different environment, the command to activate the python virtual environment can be found [here](https://docs.python.org/3/library/venv.html#how-venvs-work).

## Running the test

Now the python environment is set up, you can execute the tests with the following command.

    pytest test_api.py

