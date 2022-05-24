from distutils.log import error
from matplotlib.pyplot import table
import pandas as pd 
from sqlalchemy import create_engine
import logging 



host_ = "ps_12_7"
database_ = "crypto_db"
user_ = "postgres"
pass_ = "postgres"
port_ = "5432"

# host, database, user, pass, port
engine = create_engine(f'postgresql://{user_}:{pass_}@{host_}:{port_}/{database_}')

#engine.connect()

# Define data path to download datasets
#df = pd.read_csv("nft_data.csv")
df = pd.read_csv("data_file_nft.csv")

# Use SQLAlchemy to upload DataFrame to database in postgreSQL
#Base, conection, if exists, index
df.to_sql(table = "nft_data",con = engine, if_exists='replace',index=True, schema= "public")

print("df.to_SQL corrió")
#
# Close Connection
engine.dispose()




