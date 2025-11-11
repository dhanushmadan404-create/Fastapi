from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column,String,Integer
base=declarative_base()
class army(base):
    id=column(Integer,Primary_Key=True,index=True)
    name=column(String)
    price=column(float)