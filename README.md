# fastapi-demo

## Prerequisites

### Setup Your Virtual Environment

There are many (too many) package managers for python and while we could explore some of the new ones, we're 
going to keep it simple by using the venv module to create the virtual environment and requirements.txt to
store the application dependencies.

First create your virtual environment.

```shell
$ python -m venv .venv
```

Now activate the environment.  Note some IDEs will do this for you.

```shell
$ source .venv/Scripts/activate
```

NOTE: If git commands or python is not found on your path you may also 
need to source your `.bash_profile` if you setup your system path here. 

```shell
$ source ~/.bash_profile
```

## Exercise Steps
* Install Prerequisites
* Create a git repository on GitHub for `fastapi-demo`
* Clone the repository to your local machine and `cd` into your repository directory.
* Create a `dev` branch.
```shell
$ git checkout -b dev
```
### Install FastAPI Dependencies

Create a requirements.txt file in the root of the project.

requirements.txt
```
fastapi
uvicorn
```

Now install these requirements with the following command.
```shell
$ pip install -r requirements.txt
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
$ python app.py
```

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

## References
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [FastAPI Tutorial](https://www.youtube.com/watch?v=-ykeT6kk4bk)
* [SQLLite](https://fastapi.tiangolo.com/tutorial/sql-databases/)
* [Flyway](https://documentation.red-gate.com/fd)

