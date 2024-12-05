from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from models.sql_models import ExampleData


def insert_example_data(
        core_engine: Engine,
        data
):
    Session = sessionmaker(bind=core_engine)
    session = Session()
    try:
        for index, row in data.iterrows():
            new_insight = ExampleData(
                day=row['day'],
                temperature_max=row['Temperature Max'],
                temperature_min=row['Temperature Min'],
                average_temperature=row['Average Temperature'],
            )
            session.add(new_insight)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
