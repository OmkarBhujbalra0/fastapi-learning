from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import Session,sessionmaker,declarative_base
from fastapi import FastAPI,Depends

app = FastAPI()

DATABASE_URL = 'sqlite:///./test2.db'

engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread':False})

Base = declarative_base()

Sessionlocal = sessionmaker(bind=engine)

class tables(Base):
    __tablename__ = 'tables'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(db:Session = Depends(get_db)):
    return {"message":"SQLAlchemy is setup successfully"}