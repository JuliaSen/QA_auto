import _sqlite3

class Database():

    def __init__(self):
        self.connection = _sqlite3.connect('/Users/juliaseniukgmail.com/Desktop/python_basics_prometeus/QA_auto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected successfuly.SQLite Database Version is: {record}')

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name,\
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_all_products(self):
        query = "SELECT name, description, quantity FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_different_value_quantity_of_product(self):
        query = "SELECT DISTINCT quantity FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def check_quantity_product_more_than(self, qnt):
        query = f"SELECT name FROM products WHERE quantity > {qnt}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_user_adr_by_id(self, user_id, adr):
        query = f"UPDATE customers SET address = '{adr}' WHERE id = {user_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def select_user_adr_by_id(self, user_id):
        query = f"SELECT address FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_user(self, user_id, name, adr, city, postCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({user_id}, '{name}', '{adr}', '{city}', {postCode}, '{country}')"
        self.cursor.execute(query)
        self.connection.commit()