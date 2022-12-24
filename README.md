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

1. Create a git repository on GitHub for `fastapi-demo`
2. Clone the repository to your local machine and `cd` into your repository directory.
3. Create a `dev` branch.
```shell
$ git checkout -b dev
```
4. Create an `src/` directory
5. Create a file `app.py`.
6. Add the following imports
```python 
from fastapi 
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)
```
7. Test your setup


