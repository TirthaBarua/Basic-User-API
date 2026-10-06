# Basic-User-API
# Simple User API

A tiny, easy-to-understand Flask API for creating and retrieving user records.  
This project is intended as a learning example and a starting point for building a more feature-rich REST API.

## Features
- `GET /get-user/<user_id>` — retrieve a user by id (supports optional `extra` query param)
- `POST /create-user` — create a user with `name` and `email`
- JSON request/response
- Minimal dependencies, easy to run locally or in Docker

## Quick start

### Prerequisites
- Python 3.10+ (recommended)
- `pip` or `venv`

### Install
```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run Locally

export FLASK_APP=app.py
export FLASK_ENV=development

Open http://127.0.0.1:5000

## API
| Endpoint | Method | Description |
| --- | --- | --- |
| /get-user/&lt;user_id&gt; | GET | Returns user JSON. Optional query param: ``extra``. |
| /create-user | POST | Create a user. Body: ``{ ``"name": ``"...", ``"email": ``"..." ``}`` |

## Example

# GET
curl "http://127.0.0.1:5000/get-user/42?extra=some-info"
# RESPONSE
{
  "user_id": "42",
  "name": "Self Nerfed",
  "email": "tirthabarua06@gmail.com",
  "extra": "some-info"
}
# POST
curl -X POST http://127.0.0.1:5000/create-user \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
# RESPONSE
{
  "user_id": "12345",
  "name": "Alice",
  "email": "alice@example.com"
}

