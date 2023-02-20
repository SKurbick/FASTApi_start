from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.workshop.settings import settings

engine = create_engine(
    settings.database_url,
    # connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    # закомитил по своему желанию, так как не открывалась БД в АПИ приложения
    autoflush=False,
    # authocommit=True,
)


# закрытие сессии
def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
