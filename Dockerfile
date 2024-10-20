# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy Python script and text files into the container
COPY scripts.py /home/data/scripts.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Create an output directory for storing results
RUN mkdir -p /home/data/output

# Run the Python script when the container starts
CMD ["python", "/home/data/scripts.py"]
