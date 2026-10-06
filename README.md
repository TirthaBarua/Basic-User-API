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

