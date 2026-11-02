FROM python:3.11-slim
WORKDIR /lab
COPY main.py ./
COPY tests ./tests
USER 10001:10001
CMD ["python", "main.py", "demo"]
