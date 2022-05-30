# Trabajo Práctico Final Foundations
### ITBA - Cloud Data Engineering - Zabaljauregui Sebastian

The following task was resolved using ***one docker-compose file*** as expected with three different services:
1. A Postgres database (version 12.7) where we execute an init bash script to create the database as well as the table to be populated with service #2. This init bash script also grant access to the user declared in the docker-compose file.yml
2. The second service is the first python service called: `py-cont` (python content). This service is in charge of adding the corresponding data to the database. The dataset was taken from the official Kaggle site: [Kaggle - NFT History Sales](https://www.kaggle.com/datasets/mathurinache/nft-history-sales).
3. The third and last service is another python container, called `py-query`, and is responsible for creating a report file with the five business questions required. 

Both python services has their own logs file, where we can check every task/log of every step that's been execute.

There are three different folders in the github repository:
1. The first one called `db_psql12`, coming from database postgres version 12.7, in where we have the init bash script
2. The second folder called `add_data`, is where we have the files corresponding for the first python service, responsible for adding the data to the database. We can find the Dockerfile, the dataset as a '.csv' file and the requirements.txt with the required libraries to successfully run the python script.
3. The third and last folder is called `query_data`. We can find everything we need to run the second python service, responsible of creating the report file answering the five business questions.

### How can I run the repo?

In order to successfully run the docker-compose, a start bash script was created. So, after cloning the repo, you will need to have bash installed in your local machine, as well as *Docker version 20.10.14, build a224086* and *docker-compose version 1.29.2*. 
You can check both versions running the following commands:

```
docker --version
docker-compose version
```


After chequing the pre-requisists, we can run the bash `start.sh` script by doing the following:

```
bash start.sh
```

# Important callout:

***The bash script will check if you have any docker container running, stop all docker containers, remove all images from your local machine, remove any network previously created and run the `docker-compose up --build` command.***






