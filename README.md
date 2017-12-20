## Awesome eXtensible Distributed System 

It's an MVP for demonstration purposes **only**.

### How to run it

Note: run all commands from from the project root in terminal.

#### Using Docker (the easy way)
- Install Docker - https://www.docker.com/get-docker
- Run `docker build -t axds .` to build the image
- Run `docker run -it -p 8000:8000 -v "$PWD/axds/":/axds/axds/ axds` (Hit Ctrl+C to stop it)
- Go to `http://localhost:8000/api/v1/categories/` (or one of the endpoints below) in your browser

#### In a valid Python environment (min Python3.4)
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver` (go to localhost:8000 in browser)


### Available Endpoints

- `/api/v1/categories/` - **GET** (?page_size, page, name, search - available query params), **POST**
  - `/api/v1/categories/<id>/` - **GET**, **PUT**, **PATCH**, **DELETE**
- `/api/v1/products/` - **GET** (?page_size, page, price, search - available query params), **POST**
  - `/api/v1/products/<id>/` - **GET**, **PUT**, **PATCH**, **DELETE**
