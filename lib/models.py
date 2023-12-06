from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())


# relationship('Review') - This establishes a relationship between the two classes: Game and Review.
# backref=backref('game') - This adds a new property to the ‘Review’ class. After defining this, you can access the ‘game’ from a ‘Review’ instance, and SQLAlchemy will automatically join the related rows and return the related ‘game’.
# cascade='all, delete-orphan' - This is a delete cascade option. It means that when a ‘game’ is deleted, all related ‘Review’ instances will be deleted as well. The ‘delete-orphan’ cascade option means that child objects (in this case ‘Review’) that are no longer associated with any parent (here, ‘game’) will be deleted.
    reviews = relationship('Review', backref=backref('game'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'
