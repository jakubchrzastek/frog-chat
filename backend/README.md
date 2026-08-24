# Frog Chat

Simple real-time chat application built with Python and FastAPI.

## Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- uv
- WebSockets


## Install 
```bash
uv sync

```
## Migration 

```bash
uv run alembic upgrade head
```

## Server
```bash
uv run fastapi dev src/frog_chat/main.py
```


