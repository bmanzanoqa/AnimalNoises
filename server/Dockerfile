FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests
EXPOSE 5000
ENTRYPOINTS ["python", "app.py"]
