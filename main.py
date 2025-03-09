from sqlalchemy import create_engine, Column, String, Integer, REAL, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

database_file = "database.db"
engine = create_engine(f"sqlite:///{database_file}")
Session = sessionmaker(engine)
s = Session()
Base = declarative_base()


class Tastes:
    __tablename__ = "tastes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    weight = Column(REAL)


class IceCream:
    __tablename__ = "icecream"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    size = Column(String(20))
    taste_id = Column(Integer, nullable=False)

    @hybrid_property
    def rem_weight(self):
        return s.query(Tastes).filter_by(id=self.taste_id).first().weight

    @hybrid_property
    def taste(self):
        return s.query(Tastes).filter_by(id=self.taste_id).first().name

    __table_args__ = (
        CheckConstraint(size.in_(["МегаУльтраБольшой", "Большой", "Средний", "Маленький", "СуперМаленький"]),
                        name="check_size"))
