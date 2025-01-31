FROM python:latest
# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install selenium 
RUN pip install selenium
# Set environment variable for Chromium
ENV PATH="$PATH:/usr/bin/chromium-driver"
WORKDIR /app
COPY . /app
COPY Scores.txt /Scores.txt
RUN pip install -r requirements.txt
EXPOSE 8777
CMD ["python", "UpdatedMainGame.py"]
