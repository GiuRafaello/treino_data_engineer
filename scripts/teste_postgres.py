from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"
)

query = "SELECT version();"

df = pd.read_sql(query, engine)

print(df)