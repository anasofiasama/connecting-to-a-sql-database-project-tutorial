# APP Heroku postgrade

# 1) Connect to the database here using the SQLAlchemy's create_engine function

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
"""import psycopg2 

conn = psycopg2.connect(database= 'd2eonei9tloora', 
                        user = 'adveesvubqwsub',
                        password= '09b84c6563e60ae2a71e74abaf0b743ab678cd94db687e963953940bb92eb60e',
                        host = 'ec2-52-206-182-219.compute-1.amazonaws.com',
                        port = 5432)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Movies(id VARCHAR(2) PRIMARY KEY, title VARCHAR(30), rating INT);")
conn.commit()


conn.close()"""


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

"""import psycopg2 

conn = psycopg2.connect(database= 'd2eonei9tloora', 
                        user = 'adveesvubqwsub',
                        password= '09b84c6563e60ae2a71e74abaf0b743ab678cd94db687e963953940bb92eb60e',
                        host = 'ec2-52-206-182-219.compute-1.amazonaws.com',
                        port = 5432)

cursor = conn.cursor()
cursor.execute("INSERT INTO Movies(id,title,rating) VALUES ('3','Toy Story 3',3), ('4','Harry Potters 1',5);")
conn.commit()
conn.close()"""

# 4) Use pandas to print one of the tables as dataframes using read_sql function
import psycopg2 
import pandas as pd

conn = psycopg2.connect(database= 'd2eonei9tloora', 
                        user = 'adveesvubqwsub',
                        password= '09b84c6563e60ae2a71e74abaf0b743ab678cd94db687e963953940bb92eb60e',
                        host = 'ec2-52-206-182-219.compute-1.amazonaws.com',
                        port = 5432)

cursor = conn.cursor()
pd.read_sql("SELECT * FROM Movies", conn)
conn.close()

