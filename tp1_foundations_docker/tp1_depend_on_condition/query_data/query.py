from distutils.log import error
import pandas as pd 
from sqlalchemy import create_engine
import logging 
import contextlib

#Seteo Logger
logger = logging.getLogger('Log_query_data')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('query_data.log')
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




file_path = 'report.txt'

try:
    with open(file_path, "w+") as o:
        with contextlib.redirect_stdout(o):
            print("\nBusiness Question NRO1: \n")
            print("What's total amount of sales in USD per year?:\n")
            
            qry1= "select EXTRACT(YEAR from to_date(date_fecha, 'YYYY-MM-DD')) as y, sum(sales_usd) from nft_data group by 1 order by 1 DESC;"

            qry1_res= pd.read_sql(qry1, engine)
            print(qry1_res)



            print("\nBusiness Question NRO2: \n")
            print("How's the year-on-year evolution in sales??:\n")
            
            qry2= "WITH sales_year as (\
                select EXTRACT(YEAR from to_date(date_fecha, 'YYYY-MM-DD')) as y, sum(sales_usd) as sales_usd \
                    from nft_data \
                    group by 1 order by 1 DESC\
                    )\
                    SELECT y, \
                        sales_usd, \
                        LAG(sales_usd) OVER (ORDER BY y) as sales_previous_year, \
                        (((sales_usd / LAG(sales_usd) OVER (ORDER BY y))*100.0) - 100.0) as YoY_sales \
                    from sales_year; "

            
            qry2_res= pd.read_sql(qry2, engine)
            print(qry2_res)

            print("\nBusiness Question NRO3: \n")
            print("What was the best quarter in number of sales?:\n")
            
            qry3= "select EXTRACT(QUARTER from to_date(date_fecha, 'YYYY-MM-DD')) as q,EXTRACT(YEAR from to_date(date_fecha, 'YYYY-MM-DD')) as y, sum(sales_usd) from nft_data group by 1,2 order by 3 DESC LIMIT 1;"

            
            qry3_res= pd.read_sql(qry3, engine)
            print(qry3_res)

            print("\nBusiness Question NRO4: \n")
            print("What is the average number of sales per quarter-year?:\n")
            
            qry4= "select EXTRACT(YEAR from to_date(date_fecha, 'YYYY-MM-DD')) as y, EXTRACT(QUARTER from to_date(date_fecha, 'YYYY-MM-DD')) as q, avg(number_of_sales) as avg_number_of_sales from nft_data group by 1,2 order by 2 DESC,1 DESC;"

            
            qry4_res= pd.read_sql(qry4, engine)
            print(qry4_res)    


            print("\nBusiness Question NRO5: \n")
            print("Was the share/penetration between the secondary and primary market always stable?:\n")
            
            qry5= "select EXTRACT(YEAR from to_date(date_fecha, 'YYYY-MM-DD')) as y, \
                        EXTRACT(QUARTER from to_date(date_fecha, 'YYYY-MM-DD')) as q,  \
                        sum(sales_usd) as sales_usd,\
                        sum(primary_sales) as primary_sales_usd,\
                        (sum(primary_sales)/sum(sales_usd))*100.0 as SoB_Primary_Over_Sales \
                from nft_data group by 1,2 order by 1 DESC, 2 DESC;"

            
            qry5_res= pd.read_sql(qry5, engine)
            print(qry5_res)   

        o.close()
        logger.info("Report successfully created")


except Exception as e:
    logger.error("error while reading SQL")
    logger.error(f"Error message: {e}")



engine.dispose()
logger.info("connection closed")




