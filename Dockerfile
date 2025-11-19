FROM python:3.12-alpine AS builder

WORKDIR /var/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine

WORKDIR /var/app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY main.py .

EXPOSE 7777

CMD ["python", "main.py"]