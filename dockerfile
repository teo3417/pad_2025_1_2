FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -e . \
    && rm -rf /root/.cache/pip

# Comando para ejecutar tu script
CMD ["python", "beautiful.py"]
