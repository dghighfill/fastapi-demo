# fastapi-demo

## Prerequisites

### Install pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds to the Python world. 

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment. For the distinction between libraries and applications and the usage of setup.py vs Pipfile to define dependencies, see ☤ Pipfile vs setup.py.

```shell
$ pip install --user pipenv
```

On Windows you can find the user base binary directory by running `python -m site --user-site` and replacing site-packages with Scripts. 

If you install to your user home (i.e. --user), you might have to add PATH=~/AppData/Roaming/Python/Python39/Scripts:$PATH to your .bash_profile to add pipenv to your path.

```shell
$ cat ~/.bash_profile 
#!/bin/bash
PATH=~/AppData/Roaming/Python/Python39/Scripts:$PATH
```

### Intstall FastAPI Dependencies

With pipenv setup, from a terminal window run the following command

```shell
$ pipenv install fastapi uvicorn
```

## Exercise Steps

* Install Prerequisites
* Create a git repository on GitHub for `fastapi-demo`
* Clone the repository to your local machine and `cd` into your repository directory.
* Create a `dev` branch.
```shell
$ git checkout -b dev
```
* Create an `src/` directory
* Create a file `app.py`.
* Add the following imports
```python 
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)
```
* Test your setup - from a terminal window run the following from the `/src` directory.

```shell
$python app.py

You should see something like this.

```
$ python app.py
Will watch for changes in these directories: ['U:\\Users\\Dale\\Development\\fastapi-demo\\src']
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)    
Started reloader process using StatReload
Started server process
Waiting for application startup.
Application startup complete. 
```

