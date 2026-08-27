import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session as SQLASession

from app.db.session import engine, get_db
from app.main import app


@pytest.fixture()
def db_session():
    """Each test runs inside its own transaction (with SAVEPOINT support so
    application code calling session.commit() doesn't escape it), rolled
    back at the end so tests never leave data behind in the real database.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = SQLASession(bind=connection, join_transaction_mode="create_savepoint")

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
