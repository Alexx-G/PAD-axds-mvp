## Awesome eXtensible Distributed System 

It's an MVP for demonstration purposes **only**.

### How to run it

#### Using Docker (the easy way)
- Install Docker - https://www.docker.com/get-docker
- Run `docker build -t axds .` to build the image
- Run `docker run -p 8000:8000 -v "$PWD/axds/":/axds/axds/ axds`
- Go to `http://localhost:8000/api/v1/categories/` in your browser

#### In a valid Python environment (min Pyhton3.4)
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver` (go to localhost:8000 in browser)
