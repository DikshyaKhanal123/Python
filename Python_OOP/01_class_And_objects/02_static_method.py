class Laptop:
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount*price/100)

        print("final price: ", final_price)

l = Laptop()
l.calc_discount(1000,10)