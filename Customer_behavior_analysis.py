# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 13:41:53 2026

@author: pavitra
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\pavitra\Downloads\customer_shopping_behavior.csv")
df

df.head()
df.info
df.describe()
df.isnull().sum()


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns= {'purchase_amount_(usd)' : 'purchase_amount'})
df.columns


# create a column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

df[['age', 'age_group']].head(10)



# create column purchase frequency days

frequency_mapping = {'Fortnightly' : 14, 
                     'Weekly' : 7, 
                     'Monthly' : 30, 
                     'Quarterly' : 90, 
                     'Bi-Weekly' : 14, 
                     'Annually' : 365, 
                     'Every 3 Months' : 90}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)



(df['discount_applied'] == df['promo_code_used']).all()
df = df.drop('promo_code_used', axis=1)
df.columns




!pip install pymysql sqlalchemy


from sqlalchemy import create_engine, text
import pandas as pd

username = "root"
password = "2298"
host = "localhost"
port = "3306"
database = "customer_behavior"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Write DataFrame to MySQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

# ✅ Correct way to read (SQLAlchemy 2.0)
with engine.connect() as connection:
    df_sample = pd.read_sql(text("SELECT * FROM customer LIMIT 5;"), connection)

print(df_sample)


































