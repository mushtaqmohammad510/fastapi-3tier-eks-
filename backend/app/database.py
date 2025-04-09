SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://user:password@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
