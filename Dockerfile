# Gunakan base image Python Alpine
FROM python:3.12.0-alpine

# Set working directory di dalam container
WORKDIR /app

# Salin file dependencies ke dalam working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh konten aplikasi ke dalam working directory
COPY . .

# Expose port yang digunakan oleh Streamlit
EXPOSE 8501

# Perintah untuk menjalankan aplikasi Streamlit
CMD ["streamlit", "run", "app.py", "--host=0.0.0.0"]
