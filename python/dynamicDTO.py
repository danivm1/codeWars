from dataclasses import make_dataclass

import pandas as pd
import sqlalchemy as sa
import numpy as np


connectionString = "Driver=ODBC Driver 17 for SQL Server;"\
                   "Server=192.168.190.71;"\
                   "Database=test_daniel;"\
                   "uid=newcon;"\
                   "pwd=p@ssw0rd;"

connectionDict = {"odbc_connect": connectionString}
connectionUrl = sa.engine.URL.create("mssql+pyodbc", query=connectionDict)

engine = sa.create_engine(connectionUrl)

qry = "SELECT tableName       = t.name \
             ,columnName      = c.name \
             ,typeName        = p.name \
             ,columnLength    = c.max_length \
             ,columnPrecision = c.precision \
             ,columnScale     = c.scale \
       FROM sys.tables t \
            INNER JOIN sys.columns c \
            ON t.object_id = c.object_id \
            INNER JOIN sys.types p \
            ON c.system_type_id = p.system_type_id \
       WHERE type = 'U'"
       
df = pd.read_sql(qry, engine)

df = df.where(df.columnName != np.nan)
print(df.where(df.columnName!=np.nan))
print(df.loc[df['tableName']=='a', :])

cols = {t:[c for c in df.loc[df['tableName'] == t, :]] for t in df.tableName.unique()}

# print(df.loc[df['columnName']==np.nan, :])
# print(df.where(df.columnName!=np.nan))

for k in cols.keys():
    for v in cols[k]:
        print(f'{k}: {v}', end='\n')