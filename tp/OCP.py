class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self):
        return self.price


class VIPDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.8


class RegularDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.95


class FirstTimeCustomerDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.9


if __name__ == "__main__":
    price = 1000

    vip = VIPDiscount(price)
    print(f"VIP client: Old Price = {price}$ → New Price = {vip.apply_discount()}$")

    regular = RegularDiscount(price)
    print(f"Regular client: Old Price = {price}$ → New Price = {regular.apply_discount()}$")

    first_time = FirstTimeCustomerDiscount(price)
    print(f"First-time client: Old Price = {price}$ → New Price = {first_time.apply_discount()}$")
