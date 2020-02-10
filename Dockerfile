FROM python:3.6

RUN mkdir -p /bloomon

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /bloomon
COPY bloomon/ /bloomon/

CMD ["python", "/bloomon/app.py"]

