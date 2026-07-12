# Step 1: Use an official, lightweight Python base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Install OS-level dependencies needed to compile Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy and install Python dependencies first (maximises Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all application source code into the container
COPY . .

# Step 6: Inform Docker that the app listens on port 8501 (Streamlit default)
EXPOSE 8501

# Step 7: Health check — ensures container is responsive before traffic is routed
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Step 8: Launch the Streamlit application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
