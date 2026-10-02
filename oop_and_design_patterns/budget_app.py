class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        status = self.check_funds(amount)
        if not status:
            return False
            
        self.ledger.append({'amount': -1*amount, 'description': description})
        total = 0

        return True 
        
        
        

    def get_balance(self):
        current_balance = 0
        for entry in self.ledger:
            current_balance += entry["amount"]
        return current_balance
    
    def transfer(self, amount, destination):
        status = self.withdraw( amount, f'Transfer to {destination.name}')
        if not status:
            return False
        destination.deposit(amount,f'Transfer from {self.name}')
        return True
    
    def check_funds(self, amount):
        current_balance = self.get_balance()
        if current_balance < amount:
            return False
        else:
            return True
    
    def __str__(self):
        result = self.name.center(30, "*")

        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]

            result += "\n" + description[:23].ljust(23)
            result += f"{amount:.2f}".rjust(7)

        result += f"\nTotal: {self.get_balance():.2f}"
        
        return result



def create_spend_chart(categories):
    spending = []
    
    for category in categories:
        spent = 0

        for item in category.ledger:
            amount = item["amount"]

            if amount < 0:
                spent += -amount

        spending.append(spent)

    total_spending = sum(spending)

    percentages = []

    for amount in spending:
        percentage = int((amount / total_spending) * 100 // 10 * 10)
        percentages.append(percentage)

    result = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        result += str(level).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= level:
                result += "o  "
            else:
                result += "   "
        result += "\n"

    result += "    " + "---" * len(categories) + "-\n"

    max_len = 0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    for i in range(max_len):
        result += "     "
        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "
        if i < (max_len - 1):
         result +='\n'
    
    return(result)

    



food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "deposit")
food.withdraw(100, "groceries")
food.withdraw(50, "restaurant")

clothing.deposit(500, "deposit")
clothing.withdraw(100, "clothes")

auto.deposit(1000, "deposit")
auto.withdraw(200, "gas")

print(create_spend_chart([food, clothing, auto]))