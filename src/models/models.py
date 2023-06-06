from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


Base = declarative_base()

class Bot(Base):
    __tablename__ = "bot"

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, autoincrement=True
    )
    alias: Mapped[str] = mapped_column(nullable=False)
    token: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column(nullable=False)
    channel: Mapped[Optional["Channel"]] = relationship(back_populates="bot")


class Channel(Base):
    __tablename__ = "channel"
    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, autoincrement=True
    )
    channel_link: Mapped[str] = mapped_column(nullable=False)
    bot_link: Mapped[str] = mapped_column()
    bot_id: Mapped[Optional[int]] = mapped_column(ForeignKey("bot.id"), nullable=True)
    bot: Mapped[Optional["Bot"]] = relationship(back_populates="channel")
