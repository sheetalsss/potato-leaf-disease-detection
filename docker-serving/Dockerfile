FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install tensorflow==2.13.0 flask==2.3.3 numpy==1.24.3

# Copy the serving script
COPY serve_model.py .

EXPOSE 8601

CMD ["python", "serve_model.py"]
