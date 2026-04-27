from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:381762@localhost:5432/Clinical_Trial"
)

print(engine)