import psycopg2

conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='12345')

def get_data(products):
    cursor = conn.cursor()
    query = f"SELECT * FROM {products}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_data(sales):
    cursor = conn.cursor()
    query = f"SELECT * FROM {sales}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def insert_products(values):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

def insert_sales(values1):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO sales (pid, quantity, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, values1)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()


def profit():
    cursor = conn.cursor()
    query =" SELECT SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit,\
    sales.created_at FROM sales JOIN products ON sales.product_id= products.product_id  WHERE sales.created_at >=\
    '2022-10-13 05:00:48'  AND sales.created_at <= '2023-10-05 20:33:31' GROUP BY sales.created_at\
    ORDER BY sales.created_at ASC;"

    cursor.execute(query)
    new_data=cursor.fetchall()
    return new_data


def check_email(email):
    cursor = conn.cursor()
   
    cursor.execute("SELECT * FROM users WHERE email= %s",(email,))
    email_data=cursor.fetchone()
    if email_data:
        return email_data
    else:
        return False

def email_pass(email,password):
    cursor = conn.cursor()
    select_query= 'SELECT * FROM users WHERE email=%s and password=%s'

    cursor.execute(select_query,(email,password))
    
    check_e=cursor.fetchone()
    

    if check_e :
        if check_e[3] == password: 
            return check_e
        else:
            return False  
    
   

def create_user(values):
    cursor = conn.cursor()
    query2 = "INSERT INTO users (full_name, email, password) VALUES (%s, %s,%s)"
    cursor.execute(query2,values)
    
    conn.commit()
   
# conn.close()