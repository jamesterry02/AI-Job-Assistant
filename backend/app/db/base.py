from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Shared declarative base. All ORM models inherit from this.

    Alembic's env.py imports Base.metadata to autogenerate migrations, so
    every model module must be imported somewhere before that happens (see
    app/db/base_models.py, added once the first model exists).
    """
