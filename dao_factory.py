from sqlalchemy.orm import sessionmaker


class DaoFactory:
    def __init__(self, engine):
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

        self.factory = {}

    def register_dao(self, factory_name, dao):
        self.factory[factory_name] = dao

    def get_dao(self, factory_name):
        factory = self.factory.get(factory_name)
        if not factory:
            raise ValueError("Doesn't have" + factory_name)
        return factory(self.session)

    def search(self):
        pass
