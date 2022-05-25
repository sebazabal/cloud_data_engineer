import pandas as pd 
from sqlalchemy import create_engine
import logging 
import traceback

logger = logging.getLogger('Log_add_data')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug_add_data.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
#logger.debug('mensaje debug')
#logger.info('mensaje info')
#logger.warning('mensaje warning')
#logger.error('mensaje error')
#logger.critical('mensaje critical')
host_ = "ps_12_7"
database_ = "crypto_db"
user_ = "postgres"
pass_ = "postgres"
port_ = "5432"

# host, database, user, pass, port
#logger.info('mensaje info')
logger.info("create engine")
try:
    engine = create_engine(f'postgresql://{user_}:{pass_}@{host_}:{port_}/{database_}')
except Exception as e:
    logger.error("create engine failed")
    logger.error(f"Error message: {e}")


#engine.connect()

# Define data path to download datasets
#df = pd.read_csv("nft_data.csv")
logger.info("read csv file")
try:
    df = pd.read_csv("data_file_nft.csv")
except Exception as er:
    logger.error("error while reading file")
    logger.error(f"error message: {e}")
    
# Use SQLAlchemy to upload DataFrame to database in postgreSQL
#Base, conection, if exists, index
logger.info("df to SQL")
try:
    df.to_sql(name = "nft_data",con = engine, if_exists='replace',index=True, schema= "public")
except Exception as e:
    logger.error("Error while df_toSQL")
    logger.error(f"Error message: {e}")
    #logging.error(traceback.format_exc())
    #print(traceback.print_exc())
    # Logs the error appropriately. 

#
# Close Connection
engine.dispose()




