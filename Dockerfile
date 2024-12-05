FROM python:3.12
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt
CMD ["python", "main.py","runserver", "0.0.0.0:1995"]
