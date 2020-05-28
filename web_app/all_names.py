from flask import Blueprint
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgres://tystegvlgenmod:c9c4acb62825dd9b052d89f2974db2e910f441e4d3bf8194601db683d09d65a8@ec2-34-195-169-25.compute-1.amazonaws.com:5432/dbds6daqmiall8')

df = pd.read_sql("SELECT * FROM strain_info", engine)

def all_names():
    
    df1 = df['name']
    return df1.to_json(orient='records', indent=1)