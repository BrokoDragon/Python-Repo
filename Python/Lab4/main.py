import copy
import random

from pandas._libs.index import StringEngine


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(self.balance)

print("Problema 1")
guy = BankAccount("guy", 100)
guy.display_balance()
guy.deposit(50)
guy.display_balance()
guy.withdraw(100)
guy.display_balance()

print("================")

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def update_quantity(self,new_quantity):
        self.quantity += new_quantity

    def description(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: {self.total_value()}")

print("Problema 2")
the_product = Product("Apples",10,3)
the_product.update_quantity(5)
the_product.description()

print("================")

class Invoice:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self,product):
        self.products.append(product)

    def total_value(self):
        total = 0
        for i in self.products:
            total += i.total_value()
        return total

    def most_expensive(self):
        if not self.products:
            return None

        max_index = 0
        max_value = 0
        for i in self.products:
            if i.price > max_value:
                max_value = i.price
                max_index = copy.copy(i)
        print(max_index.name)
        return max_index

    def display(self):

        for i in self.products:
            i.description()
        print(self.total_value())

print("Problema 3")

Apples = Product("Apples",10,3.5)
Pears = Product("Pears",20,5)
Toy = Product("Toy",10,5)
New_Product = Product("New_Product",20,999)

Invoice = Invoice([Apples,Pears,Toy])
Invoice.add_product(New_Product)
Invoice.total_value()
Invoice.most_expensive()
Invoice.display()

print("==========")
class DiceGame:
    def __init__(self, players, rounds):
        self.players = players
        self.scores = {i for i in players.get("score")}
        self.rounds = rounds
    def play_round(self):
        for i in self.players:
            roll = random.randint(1,6)
            i.score += roll
    def display_scores(self):
        for i in self.scores:
            print(i)
    def tied(self, players):
        score = players[0].score
        for i in players:
            if i.score != score:
                return False
        return True

    def winner(self):
        winners = []
        for i in self.players:
            if i.score > self.scores[i]:
                winners.append(i)
            if len(winners) == 1:
                return winners[0]
            else:
                while self.tied(winners):
                    self.play_round()
                for i in winners:
                    if i.score > self.scores[i]:
                        return i

player1 = {
    "name" : "James",
    "score" : 3,
}

player2 = {
    "name" : "Jim",
    "score" : 6,
}

player3 = {
    "name" : "Jim",
    "score" : 6,
}

class DiceGames:
    def __init__(self, players, rounds):
        self.players = players
        self.scores = {p: 0 for p in players}
        self.rounds = rounds

    def play_round(self):
        for p in self.players:
            self.scores[p] += random.randint(1, 6)

    def display_scores(self):
        for p in self.players:
            print(p, self.scores[p])

    def winner(self):
        maxim = max(self.scores.values())
        winners = [p for p in self.players if self.scores[p] == maxim]
        while len(winners) > 1:
            rolls = {p: random.randint(1, 6) for p in winners}
            maxim = max(rolls.values())
            winners = [p for p in winners if rolls[p] == maxim]
        return winners[0]



