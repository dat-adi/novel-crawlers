# Base Image
FROM python:3.8

# Creating a non root user
RUN useradd -ms /bin/bash user
USER user

# Defining the workspace that we're going to be
# working in
WORKDIR /home/user

# Updating the dependencies
RUN pip install -U \
    pip

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY . .

# Marking the Docker container
ARG GIT_HASH
ENV GIT_HASH=$(GIT_HASH:-dev)

# Exposing the port
EXPOSE 10000

# Defining the entrypoint
ENTRYPOINT ["python", "./src/main.py"]
