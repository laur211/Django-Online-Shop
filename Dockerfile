FROM python:3

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app

COPY . .
COPY ./ShopingCart/requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y python3-pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

WORKDIR /usr/src/app/ShopingCart/shopingcart
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]