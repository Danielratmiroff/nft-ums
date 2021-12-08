FROM python:3
WORKDIR /home/app/ums
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "./app.py"]