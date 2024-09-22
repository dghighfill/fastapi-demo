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

## Exercise 1 Steps

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

## Exercise 2 Steps

Now we're going to create a new API fast.  I'm a coffee snob, so we're going to be building out a coffee API to fetch and save coffees.

* In the app.py create a coffee dictionary with the worlds best 7 coffee beans as follows.
```python
coffees = {
    1: { "name": "Hawaii Kona Coffee" },
    2: { "name": "Jamacian Blue Mountain" },
    3: { "name": "Panama Geisha" },
    4: { "name": "Sulawesi Toraja"},
    5: { "name": "TANZANIA PEABERRY" },
    6: { "name": "MOCHA JAVA" },
    7: { "name": "ETHIOPIAN HARRAR" },
}
```

* Now create an API to fetch this list of beans.

```python
@app.get("/coffees")
def get_coffees() -> dict:
    return coffees
```

* Test your application

You can copy and paste the URL from the terminal window to access your server.

http://127.0.0.1:8000/

This will show a page not found because you don't have a route to `/`. 

![](assets/ex_1_1.png)

Change the path the http://127.0.0.1:8000/coffees.  Viola your data!!

![](assets/ex_1_2.png)

Uvicorn comes with a build in Swagger UI. Swagger is an API tester to verify your API is
working as designed for all of your consumers (i.e. the user interface)

![](assets/ex_1_3.png)

When you `Try it Out` you will see the response in a nicely formatted JSON response.

![](assets/ex_1_4.png)

## Exercise 3 Steps

Now we're going to layer in some CRUD (Create, Read, Update, and Delete Operations) to 
our coffee list.  We've previously coded a GET operation, but now we're going to add in
PUT, POST, and DELETE HTTP Methods.

Each of these will be interacting with the coffees dictionary.

* First lets add a new GET operation to get a single coffee resource.

Add the following imports to app.py
```python
from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
```

```python
@app.get("/coffees/{coffee_id}")
def get_by_id(coffee_id: int = Path(description="The ID of the bean you'd like to retrieve", gt=0)):
    if coffee_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Bean ID does not exists")
    else:
        return coffees[coffee_id]
```

There's a lot going on here.

* We're now taking in a path parameter `coffee_id` on the URL
* We have a description that will show up in the Swagger tool.  Check it out with `Try it Out`
* If we don't find something, we raise an HTTPException and set a 404 status code. 

Now lets call write the CRUD operations

* Add the following import so that we can submit a JSON payload.

```python
from pydantic import BaseModel
```

* Add the following class to represent our Model.

```python
class Coffee(BaseModel):
    name: str
    roast: str = None  # light, medium, dark
```

pydantic will do all the magic of marshalling and unmarshalling the JSON string into
this object.

* Add the following routes to the `app.py`

```python
@app.post("/coffees")
def create_coffee(coffee: Coffee):
    item_id = len(coffees) + 1
    if item_id in coffees:
        raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail="Coffee ID already exists")
    else:
        coffees[item_id] = coffee
    return coffees[item_id]


@app.put("/coffees/{item_id}")
def update_coffee(item_id: int, coffee: Coffee):
    if item_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee ID does not exists")
    else:
        coffees[item_id] = coffee
    return coffees[item_id]


@app.delete("/coffees/{item_id}")
def delete_coffee(item_id: int):
    if item_id not in coffees:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Coffee ID does not exists")
    else:
        del coffees[item_id]
    return {}
```

## References
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [FastAPI Tutorial](https://www.youtube.com/watch?v=-ykeT6kk4bk)
* [SQLLite](https://fastapi.tiangolo.com/tutorial/sql-databases/)
* [Flyway](https://documentation.red-gate.com/fd)
