"""Import every ORM model here so Base.metadata is fully populated before
Alembic autogenerate runs. Add one line per model as it's created.
"""

from app.models.user import User  # noqa: F401
