# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from fisco_bcos_sol_toolbox.database import db
from fisco_bcos_sol_toolbox.user.models import User


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    password = PostGenerationMethodCall("set_password", "example")
    active = True

    class Meta:
        """Factory configuration."""

        model = User
