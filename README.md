# Text to Speech Application

This is a simple application that converts text input into speech. It utilizes Python with the FastAPI framework and uvicorn server for the backend, along with Docker for containerization.

## Features

- Converts text input into speech.
- Exposes a RESTful API endpoint for text-to-speech conversion.
- Dockerized for easy deployment and portability.

## Requirements

- Docker
- Python 3.8 or later

## Installation and Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/gtts-with-fastapi.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gtts-with-fastapi
    ```

3. Build the Docker image:

    ```bash
    docker build -t text_to_speech .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 80:80 text_to_speech
    ```

5. Access the application at `http://localhost:80`.
