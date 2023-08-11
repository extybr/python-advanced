FROM python:3.11-bookworm

RUN mkdir /new_year_app

COPY requirements.txt /new_year_app/

RUN pip install -r /new_year_app/requirements.txt

COPY new_year_app /new_year_app/

WORKDIR /new_year_app

ENTRYPOINT ["python", "app.py"]
