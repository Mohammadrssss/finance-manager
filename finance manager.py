import userrr
import transaction

class FinanceManager: 
    def __init__(self): 
        self.users = [] 
    
    def add_user(self, user): 
        self.users.append(user) 
    
    def get_user(self, name): 
        
        for user in self.users: 
            
            if user.name == name: 
                return user 
        return None 
    
    def run(self): 
        print("Welcome to the Personal Finance Manager!") 
        
        while True: 
            print("\nMain Menu:") 
            print("1. Add User") 
            print("2. Add Transaction") 
            print("3. View Transactions")
            print("4. Delete Transaction") 
            print("5. Exit") 
            choice = input("Enter your choice (1-5): ") 
            if choice == "1": 
                name = input("Enter the user's name: ") 
                user = User(name) 
                self.add_user(user) 
                print(f"User '{name}' has been added.") 
            
            elif choice == "2": 
                user_name = input("Enter the user's name: ") 
                
                user = self.get_user(user_name) 
                if user: 
                    date = input("Enter the date (YYYY-MM-DD): ")
                    
                    description = input("Enter the description: ")
                    amount = float(input("Enter the amount: ")) 
                    
                    transaction_type = input("Enter the transaction type (Income/Expense): ") 
                    
                    transaction = Transaction(date, description, amount, transaction_type) 
                    
                    user.add_transaction(transaction) 
                    print("Transaction added successfully.") 
                    
                else:
                    print(f"User '{user_name}' not found.") 
                    
            elif choice == "3": 
                user_name = input("Enter the user's name: ") 
                
                user = self.get_user(user_name) 
                
                if user: user.view_transactions()
                else: print(f"User '{user_name}' not found.") 
            
            elif choice == "4": 
                user_name = input("Enter the user's name: ") 
                
                user = self.get_user(user_name) 
                if user: 
                    date = input("Enter the date of the transaction to delete (YYYY-MM-DD): ") 
                    
                    description = input("Enter the description of the transaction to delete: ") 
                    
                    for transaction in user.transactions: 
                        
                        if transaction.date == date and transaction.description == description: 
                            user.delete_transaction(transaction) 
                        
                            print("Transaction deleted successfully.") 
                            
                            break 
                    else: 
                        print("Transaction not found.") 
                
                else: print(f"User '{user_name}' not found.")
            
            elif choice == "5": 
                print("Exiting the Personal Finance Manager...") 
                break 
            else: print("Invalid choice. Please try again.") 
            
if __name__ == "__main__": 
    finance_manager = FinanceManager() 
    finance_manager.run()