from sqlalchemy import create_engine

from models.sql_models import Base


def db_connection_engine():
    # TODO Enter information of Database
    user = ""
    pwd = ""
    host = ""
    db_name = ""
    engine = create_engine(
        f'postgresql://{user}:{pwd}@{host}/{db_name}',
    )
    return engine


core_engine = db_connection_engine()
Base.metadata.bind = core_engine
