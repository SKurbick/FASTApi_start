from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.workshop.settings import settings

engine = create_engine(
    settings.database_url,
    # connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autoflush=False,
    authocommit=False,
)