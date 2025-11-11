from fastapi import FastAPI
from database_c import army
from database import session,engine
import database_models
man=FastAPI()
p=[
    army(id=1,name="dhanush",price=500),
    army(id=2,name="sari",price=500),
    army(id=3,name="hari",price=500),
    army(id=4,name="mada",price=500)
]

database_models.base.metadata.create_all(bind=engine)
# create the database in postgre 

@man.get("/")
def good():
    db=session()
    
    return "what is happing"

@man.get("/product/{id}")
def get_product_by_id(id:int):
    for product in p:
        if product.id==id:
            return product 
    return("product not found")

@man.post("/product")
def addProduct(product:army):
    p.append(product)
    return p  

@man.put("/product")
def update(id:int,product:army):
    for i in range (0,len(p)):
        if p[i].id==id:
            p[i]=product 
            return p
    return "No product found"


@man.delete("/product")
def delete_product(id:int):
    for i in range(0,len(p)):
        if p[i].id==id:
            del p[i]
            return p
    return "product not found"
           
           


