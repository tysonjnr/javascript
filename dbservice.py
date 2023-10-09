import psycopg2

conn = psycopg2.connect(database="myduka_class", user='postgres', password='12345',host='localhost', port= '5432')
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
def calc_profit():
    cursor=conn.cursor()
    y = "SELECT DATE(created_at) AS Date,SUM((products.selling_price-products.buying_price)*sales.quantity) AS profit FROM sales JOIN products ON sales.product_id=products.product_id  GROUP BY Date ORDER BY Date ASC"
    cursor.execute(y)
    data = cursor.fetchall()
    return data

def check_email(email):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    exists = cursor.fetchone()

    if exists:
        return exists 
    else:
        return False
def check_pass_match(email,password):
    cursor = conn.cursor()
    match = "SELECT COUNT(*) FROM users WHERE email = %s AND password = %s"
    cursor.execute(match,(email,password))
    data = cursor.fetchone()
    return data
def create_user(values):
    cursor = conn.cursor()
    insert_query = "INSERT INTO users(full_name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, values)
    conn.commit()

values = ('james brown','james@gmail.com','1233456')
jr=create_user(values)
print(jr)





































def create_user():
    cursor = conn.cursor()
    insert_query= "INSERT INTO users(full_name,email,password) VALUES(%s,%s,%s)"
    cursor.execute(insert_query)
    conn.commit()
        
  
  


