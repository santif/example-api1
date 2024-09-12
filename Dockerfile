# Usar una imagen base ligera de Python
FROM python:3.9-alpine

WORKDIR /app
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
COPY main.py .
COPY securities.csv .
COPY market_data.csv .
COPY historical_prices.csv .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
