import psycopg2

conn = psycopg2.connect(database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
# selecting from

def get_data(p):
   cur = conn.cursor()
   t = "select * from " + p
   cur.execute(t)
   data = cur.fetchall()
   return data

# inserting into
def insert_products(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO products (productname, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, values)
    conn.commit()
        
def insert_sale(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO sales (product_id, quantity, created_at) VALUES (%s,%s, now())"
    cursor.execute(insert_query,values)
    conn.commit()
