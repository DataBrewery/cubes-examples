#
#

import sys
from sqlalchemy.engine import create_engine
import re
import datetime
import csv

cache = {}
connection = None

def main():
 
    global connection
    
    # Open source
    engine = create_engine("sqlite:///webshop.sqlite")
    connection = engine.connect()
    
    # Cleanup
    connection.execute("DELETE FROM dates");
    connection.execute("DELETE FROM customers");
    connection.execute("DELETE FROM countries");
    connection.execute("DELETE FROM products");
    connection.execute("DELETE FROM sales");
    

    # Generate all dates
    generate_dates()
    
    # Import facts and dimension data
    import_sales()
    
    # Add extra dimensions for left joins
    insert_product ("Books", "200 ways of slicing a cube")
    

def save_object(table, row):
    
    if (table in cache):
        if (row["id"] in cache[table]):
            return row["id"]
    else:
        cache[table] = {}
    
    keys = row.keys();
    sql = "INSERT INTO " + table + " ( "
    sql = sql + ", ".join(keys)
    sql = sql + ") VALUES ( "
    sql = sql + ", ".join([ ("'" + str(row[key]) + "'") for key in keys])
    sql = sql + ")"
    
    print "Inserting - Table: %-14s Id: %s" % (table, row["id"])
    #print sql
    
    connection.execute(sql);
    cache[table][row["id"]] = row      
                              
    return row["id"]

def sanitize(value):
    
    if (value == ""):
        value = "(BLANK)"
    elif (value == None):
        value = "(NULL)"
    else:
        value = re.sub('[^\w]', "_", value.strip())
    return value

def insert_country (continent, country):
    
    row = {
           "id": sanitize(country),
           "continent": continent,
           "country": country
    }
    return save_object ("countries", row)

def insert_product (category, product):
    
    row = {
           "id": sanitize(product),
           "category": category,
           "name": product
    }
    return save_object ("products", row)

def insert_customer (customer_name):
    
    row = {
           "id": sanitize(customer_name),
           "name": customer_name
    }
    return save_object ("customers", row)

def insert_date (year, month, day):
    
    row = { }
    prefix = "date"

    date = datetime.date(int(year), int(month), int(day));

    if date != None:
        row["id"] = sanitize(datetime.datetime.strftime(date, "%d/%b/%Y"))
        row[prefix + "_year"] = date.year
        row[prefix + "_quarter"] = ((date.month - 1) / 3) + 1
        row[prefix + "_month"] = date.month
        row[prefix + "_day"] = date.day
        row[prefix + "_week"] = date.isocalendar()[1]

        if row[prefix + "_month"] == 12 and row[prefix + "_week"] <= 1:
            row[prefix + "_week"] = 52
        if row[prefix + "_month"] == 1 and row[prefix + "_week"] >= 52:
            row[prefix + "_week"] = 1

    return save_object ("dates", row)

def insert_fact(fact):
    return save_object ("sales", fact)

def generate_dates():
    
    start_date =  datetime.datetime.strptime("2012-01-01", "%Y-%m-%d")
    end_date =  datetime.datetime.strptime("2013-12-31", "%Y-%m-%d")
    
    cur_date = start_date
    while (cur_date <= end_date):
        insert_date (cur_date.year, cur_date.month, cur_date.day)
        cur_date = cur_date + datetime.timedelta(days = +1)
    
def import_sales():
    
    count = 0
    header = None
    with open('webshop-facts.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            
            count = count + 1
            fact = { "id" : count }
            
            if (header == None):
                header = row
                continue
            
            arow = {}
            for header_index in range (0,  len(header)):
                arow[(header[header_index])] = row[header_index]
            
            # Process row
            fact["date_id"] = insert_date(arow["date_created.year"], arow["date_created.month"], arow["date_created.day"])
            fact["customer_id"] = insert_customer(arow["customer.name"])
            fact["country_id"] = insert_country(arow["country.region"], arow["country.country"])
            fact["product_id"] = insert_product(arow["product.category"], arow["product.name"])
            
            fact["quantity"] = arow["quantity"]
            fact["price_total"] = arow["price_total"]
            
            insert_fact(fact)
            
    print "Imported %d facts " % (count)

if __name__ == "__main__":
    main()

