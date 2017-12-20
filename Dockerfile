FROM python:3.6

# Setup Python Environment
RUN apt-get update

# Set working directory
WORKDIR /axds/

COPY requirements.txt ./

# Some python dependencies might have native extensions
RUN apt-get install -y curl build-essential

# Install python libs
RUN pip install -r requirements.txt

# Apply migrations and start server
CMD ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
