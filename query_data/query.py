from distutils.log import error
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

#conn = engine.connect()

#rs = conn.execute("Select * from crypto_db.nft_data;")
#rs = conn.execute("Select * from nft_data;")

qry= "select * from nft_data;"
return_qry= pd.read_sql(qry, engine)

print(return_qry.head(10))

print("query returned")
#for row in rs:
#    print(row)
# Close Connection
engine.dispose()




