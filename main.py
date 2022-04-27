from dao_factory import DaoFactory
from dao.video_game_dao import VideoGameDao
from dao.sales_dao import SaleDao
from sqlalchemy import create_engine

from model.update_models import UpdateVideoGame

if __name__ == "__main__":
    sqlite_db = "vgsales.db"

    engine = create_engine(f"sqlite:///{sqlite_db}")
    # Session = sessionmaker()
    # Session.configure(bind=engine)
    # session = Session()

    # video_game_by_year = session.query(VideoGame).order_by(VideoGame.Year).all()
    # for row in video_game_by_year:
    #     print(row.Name)
    # print(len(video_game_by_year))
    # print()

    factory = DaoFactory(engine)
    factory.register_dao("video_game", VideoGameDao)
    factory.register_dao("sales", SaleDao)

    video_game_factory = factory.get_dao("video_game")
    print(video_game_factory.get(1))
    video_game_factory.update(1, UpdateVideoGame(Name="Wiiiiiiiii Sports"))
    print(video_game_factory.get(1))
    video_game_factory.update(1, UpdateVideoGame(Name="Wii Sports"))
    print(video_game_factory.get(1))

    sale_factory = factory.get_dao("sales")
    print(sale_factory.get(1))

    print("end")
