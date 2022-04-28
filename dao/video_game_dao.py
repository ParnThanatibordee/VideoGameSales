from model.models import VideoGame
from model.update_models import UpdateVideoGame


class VideoGameDao:
    def __init__(self, session):
        self.session = session

    def get(self, GameID):
        return self.session.query(VideoGame).filter_by(GameID=GameID).first()

    def get_all(self):
        return self.session.query(VideoGame).all()

    def update(self, GameID, game: UpdateVideoGame):
        video_game = self.get(GameID)
        print('*')

        try:
            print(game.Name)
            if game.Name:
                video_game.Name = game.Name
            if game.Platform:
                video_game.Platform = game.Platform
            if game.Year:
                video_game.Year = game.Year
            if game.Genre:
                video_game.Genre = game.Genre
            if game.Publisher:
                video_game.Publisher = game.Publisher
            self.session.commit()
        except:
            self.session.rollback()
            raise
