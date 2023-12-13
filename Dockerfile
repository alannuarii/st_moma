FROM python:3.9.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--host=0.0.0.0"]

EXPOSE 8501