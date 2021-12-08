# Base Image
FROM python:3.8.3-slim-buster

# Defining the workspace that we're going to be
# working in
WORKDIR /src

# Creating a non root user
RUN useradd -m -r user && \
    chown user /src

# Updating the dependencies
RUN pip install -U \
    pip

# Install Dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy files
COPY . .

# Marking the Docker container
ARG GIT_HASH
ENV GIT_HASH=$(GIT_HASH:-dev)

# Setting the user
USER user
