from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (using SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./reviews.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Review table model
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)
    review = Column(Text, nullable=False)

# Create the table if it does not exist
Base.metadata.create_all(bind=engine)
