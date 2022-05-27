import pandas as pd 
from sqlalchemy import create_engine
import logging 



#Seteo Logger
logger = logging.getLogger('Log_add_data')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('add_data.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


#Variables de conexión a la db
host_ = "ps_12_7"
database_ = "crypto_db"
user_ = "postgres"
pass_ = "postgres"
port_ = "5432"


logger.info("create engine")
try:
    engine = create_engine(f'postgresql://{user_}:{pass_}@{host_}:{port_}/{database_}')
except Exception as e:
    logger.error("create engine failed")
    logger.error(f"Error message: {e}")


logger.info("read csv file")
try:
    df = pd.read_csv("data_file_nft.csv")
    logger.info("data successfully uploaded")
except Exception as er:
    logger.error("error while reading file")
    logger.error(f"error message: {e}")
    

logger.info("df to SQL")
try:
# Use SQLAlchemy to upload DataFrame to database in postgreSQL
#Base, conection, if exists, index
    df.to_sql(name = "nft_data",con = engine, if_exists='replace',index=True, schema= "public")

except Exception as e:
    logger.error("Error while df_toSQL")
    logger.error(f"Error message: {e}")


# Close Connection
engine.dispose()





