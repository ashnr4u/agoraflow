from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_email: Mapped[str]  = mapped_column(unique=True)
    name: Mapped[str]
    hashed_password: Mapped[str]
    role: Mapped[str]
    created_at: Mapped[datetime]

    __table_args__ =(
            CheckConstraint( 
                "role IN ('student','organiser')",
                name = "checking_roles" 
                # Name the constraint so the database/Alembic can identify it later
                # (useful for inspecting, modifying, or dropping the constraint).
            ),
    )



class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[int] = mapped_column(primary_key=True)
    event_name: Mapped[str] = mapped_column(unique=True)
    max_capacity: Mapped[int]
    registration_start: Mapped[datetime]
    registration_close: Mapped[datetime]
    event_start_date: Mapped[datetime]
    description: Mapped[str]
    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))


class Registration(Base):
    __tablename__ = "registrations"

    registration_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.event_id"))
    registered_at: Mapped[datetime]