from itemadapter import ItemAdapter
import mysql.connector
import json  # Import for JSON serialization

class BookcraperPipeline:
    def process_item(self, item, spider):
        return item

class SaveToMySqlPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Subh@deep2003',
            database='Product'
        )
        print(self.conn)
        self.curr = self.conn.cursor()

        # Create table if not exists
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(255),
                name VARCHAR(255),
                url VARCHAR(255),
                price VARCHAR(255),
                mrp VARCHAR(255),
                description TEXT,
                Fit VARCHAR(255),
                Fabric VARCHAR(255),
                Neck VARCHAR(255),
                Sleeve VARCHAR(255),
                Pattern VARCHAR(255),
                Length VARCHAR(255)
            )
        """)

    def process_item(self, item, spider):
        # Handle list data by converting it to JSON or strings
        def handle_list(data):
            if isinstance(data, list):
                return json.dumps(data)  # Convert list to JSON string
            return data

        # Insert data into MySQL
        self.curr.execute(""" 
            INSERT INTO products(category, name, url, price, mrp, description, Fit, Fabric, Neck, Sleeve, Pattern, Length) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
            item.get('category'),
            item.get('name'),
            item.get('url'),
            item.get('price'),
            item.get('mrp'),
            handle_list(item.get('description')),  # Convert list to JSON
            item.get('Fit'),
            item.get('Fabric'),
            item.get('Neck'),
            item.get('Sleeve'),
            item.get('Pattern'),
            item.get('Length')
        ))
        print("Data Inserted Successfully")
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.curr.close()
        self.conn.close()
