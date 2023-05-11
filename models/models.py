from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

bot = Table(
    'bot',
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("alias", String, nullable=False),
    Column("token", String, nullable=False),
    Column("description", String),
    Column("name", String, nullable=False),
)

channel = Table(
    "channel",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("channel_link", String, nullable=False),
    Column("bot_link", String),
    Column("bot_id", Integer, ForeignKey("bot.id")),
)
