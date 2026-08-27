from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class EmailAlreadyRegisteredError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, email: str, password: str) -> User:
        if self.user_repository.get_by_email(email):
            raise EmailAlreadyRegisteredError()
        password_hash = hash_password(password)
        return self.user_repository.create(email=email, password_hash=password_hash)

    def authenticate(self, email: str, password: str) -> User:
        user = self.user_repository.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()
        return user

    def create_token_for_user(self, user: User) -> str:
        return create_access_token(subject=str(user.id))
