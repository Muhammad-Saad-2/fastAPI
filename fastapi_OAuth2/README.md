# FastAPI Authentication System

This project demonstrates a basic authentication system using FastAPI, where users are verified by their username and password. The system generates JWT tokens for authenticated users and includes endpoints for various functionalities such as login, getting all users, accessing special endpoints, and decoding tokens.

## Features

- **User Authentication**: Verify users by their username and password.
- **JWT Token Generation**: Generate JWT tokens for authenticated users.
- **Protected Endpoints**: Access endpoints protected by token authentication.
- **Token Decoding**: Decode and verify JWT tokens.

## Requirements

- Python 3.7+
- FastAPI
- python-jose
- Uvicorn

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/fastapi-auth-system.git
    cd fastapi-auth-system
    ```

2. **Install Poetry** (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install dependencies using Poetry**:

    ```bash
    poetry install
    ```

4. **Create a fake database file** (`fakedb.py`):

    ```python
    fake_db = {
    "Rose Marry" : {
            "useranme": "Rose Marry",
            "password": "my_password",
            "email":"rosemarry@example.com"

        },

        "Alice Benjamin":{
            "username":"Alice Benjamin",
            "password":"your_password",
            "email":"alice@example.com"
        }
    }
    ```

5. **Run the application**:

    ```bash
    poetry run uvicorn main:app --reload
    ```

## Endpoints

### Login

- **URL**: `/login`
- **Method**: `POST`
- **Description**: Authenticates a user and returns a JWT token.
- **Payload**:

    ```json
    {
        "username": "Rose Marry",
        "password": "my_password"
    }
    ```

- **Response**:

    ```json
    {
        "username": "john",
        "access_token": "your.jwt.token.here"
    }
    ```

### Get All Users

- **URL**: `/all-user`
- **Method**: `GET`
- **Description**: Returns all users in the fake database (requires token).
- **Headers**:

    ```http
    Authorization: Bearer your.jwt.token.here
    ```

### Special Endpoint

- **URL**: `/special-endpoint`
- **Method**: `GET`
- **Description**: Returns a message for authorized users (requires token). This is designed for a multiple microservices architecture where you don't authenticate the user for every endpoint you create. Instead, you use dependency injection from the login endpoint, where you've already authenticated the user.

- **Headers**:

    ```http
    Authorization: Bearer your.jwt.token.here
    ```

### Get Token

- **URL**: `/get-token`
- **Method**: `GET`
- **Description**: Generates a token for a given username.
- **Query Parameters**:

    - `name`: The username for which to generate the token.

### Decode Token

- **URL**: `/decoded-token`
- **Method**: `GET`
- **Description**: Decodes and returns the content of a given token.
- **Query Parameters**:

    - `access_token`: The JWT token to decode.


## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- [Poetry](https://python-poetry.org/)

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is highly appreciated!
