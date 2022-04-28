from sqlalchemy import create_engine

from dao.dao_factory import DaoFactory
from dao.sales_dao import SaleDao
from dao.video_game_dao import VideoGameDao
from model.update_models import Update

SQLITE_DB = "vgsales.db"


class GameSale:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{SQLITE_DB}")

        self.factory = DaoFactory(self.engine)
        self.factory.register_dao("video_game", VideoGameDao)
        self.factory.register_dao("sales", SaleDao)
        self.current_factory = None

    def set_factory(self, factory_name):
        self.current_factory = self.factory.get_dao(factory_name)

    def get(self, GameID):
        if self.current_factory is not None:
            return self.current_factory.get(GameID)
        return None

    def get_all(self):
        if self.current_factory is not None:
            return self.current_factory.get_all()
        return []

    def update(self, GameID, update: Update):
        if self.current_factory is not None:
            self.current_factory.update(GameID, update)
