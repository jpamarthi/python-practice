# Start your image with a node base image
FROM python:3.12

# The /app directory should act as the main application directory
WORKDIR /python-practice

# Install pytest
RUN pip3 install pytest

# Install coverage
RUN pip3 install coverage
