import json

class CRM:
    def _init_(self):
        self.customers = []

    def add_customer(self, name, email, phone):
        customer_id = len(self.customers) + 1
        customer = {
            'id': customer_id,
            'name': name,
            'email': email,
            'phone': phone
        }
        self.customers.append(customer)
        print(f"Customer {name} added successfully!")

    def view_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        for customer in self.customers:
            print(f"ID: {customer['id']}, Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}")

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        for customer in self.customers:
            if customer['id'] == customer_id:
                if name:
                    customer['name'] = name
                if email:
                    customer['email'] = email
                if phone:
                    customer['phone'] = phone
                print(f"Customer ID {customer_id} updated successfully!")
                return
        print(f"Customer with ID {customer_id} not found.")

    def delete_customer(self, customer_id):
        for customer in self.customers:
            if customer['id'] == customer_id:
                self.customers.remove(customer)
                print(f"Customer ID {customer_id} deleted successfully!")
                return
        print(f"Customer with ID {customer_id} not found.")
        
    def save_to_file(self, filename='customers.json'):
        with open(filename, 'w') as file:
            json.dump(self.customers, file)
        print("Customer data saved to file.")

    def load_from_file(self, filename='customers.json'):
        try:
            with open(filename, 'r') as file:
                self.customers = json.load(file)
            print("Customer data loaded from file.")
        except FileNotFoundError:
            print(f"No file named {filename} found.")