class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # @classmethod
    # def check_type(cls, val1, val2):
    #     return (cls, val1, val2)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        # try:
        #     result = self.a / self.b
        # except ZeroDivisionError as error:
        #     print(error)
        # finally:
        #     return result
        return self.a / self.b