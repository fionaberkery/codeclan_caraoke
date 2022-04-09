class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def check_wallet(self, amount):
        if self.wallet >= amount:
            return True

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount 
        return self.wallet