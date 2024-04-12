# Project Name

API_PROJ_AULA12

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This is a simple API using FastAPI project created for learning purposes. All it does is use a fake database (with the use of the Faker module) to retrieve information on several alumni from a non-specified school.

It has three get methods that allow you, the user, to retrieve the entire DB, or search by ID or alumni name.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository.
2. Build the Docker image using the command `docker build -t my-api .`.
3. Run the Docker container using the command `docker run -p 8000:8000 my-api`.

Or, alternatively

1. Clone the repository
2. Use the command `docker compose up`.

## Usage

1. (Optional) Generate a new database by running the command `python scripts/facedb.py`.
2. Start the server using `docker compose up` or `docker run -p 8000:8000 my-api`.
3. Access the API documentation by visiting `http://localhost:8000/docs` in your web browser.
4. Use the provided menu to retrieve the alumni database information or try out the ID or name endpoints.

# API Endpoints

This API provides several endpoints for accessing alumni data.

## Get All Alumni

- **Endpoint:** `/alumni`
- **Method:** `GET`
- **Description:** Returns a list of all alumni.

Example usage:

```bash
curl -X GET http://localhost:8000/alumni
```

## Get Alumni by ID

- **Endpoint:** `/alumni/id/{alumni_id}`
- **Method:** `GET`
- **Description:** Returns the alumnus with the specified ID. If no such alumnus exists, returns a 404 error.

Example usage:

```bash
curl -X GET http://localhost:8000/alumni/id/1234
```

## Get Alumni by Name

- **Endpoint:** `/alumni/name/{alumni_name}`
- **Method:** `GET`
- **Description:** Returns the alumnus with the specified name. If no such alumnus exists, returns a 404 error.

Example usage:

```bash
curl -X GET http://localhost:8000/alumni/name/John%20Doe
```

## License

This project is licensed under the [MIT License](LICENSE).