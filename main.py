from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    sqlite_db = "vgsales.db"

    engine = create_engine(f"sqlite:///{sqlite_db}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    video_game_by_year = session.query(VideoGame).order_by(VideoGame.Year).all()
    for row in video_game_by_year:
        print(row.Name)
    print(len(video_game_by_year))
    print()

    print("end")
