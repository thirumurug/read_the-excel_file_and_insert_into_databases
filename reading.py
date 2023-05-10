import pandas as pd
 
from sqlalchemy import create_engine
 
user = "root"
password = "Thiru#2001"
host = "localhost"
port = 3306
database = "zogx"
 
engine = create_engine(url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
user, password, host, port, database))
 
excel_data_df=pd.read_excel(io = '/home/thirusubramaniyan/Desktop/bmi_calculator/dresses.xlsx', sheet_name="Sheet2",index_col=None) 
excel_data_df.to_sql(name="dresses",con=engine,if_exists='append',index_label='id')