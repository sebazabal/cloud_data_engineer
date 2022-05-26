#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE nft_data(
    index SERIAL,
    date_fecha DATE NOT NULL,
    sales_usd_cumsum NUMERIC,
    number_of_sales_cumsum INT,
    active_market_wallets_cumsum INT ,
    primary_sales_cumsum NUMERIC,
    secondary_sales_cumsum NUMERIC,
    averageusd_cum NUMERIC,
    sales_usd NUMERIC,
    number_of_sales INT ,
    active_market_wallets INT,
    primary_sales NUMERIC, 
    PRIMARY KEY(date_fecha)
    );
	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
EOSQL