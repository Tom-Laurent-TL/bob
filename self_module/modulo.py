from math import floor

class ModuloBim:
    def __init__(self, period, max_bim):
        self.period = period
        self.coin = period-1
        self.max_bim = max_bim
        self.bim = 0

    def update(self):
        self.coin = (self.coin+1)%self.period

    def is_feed(self):
        return self.bim >= self.max_bim

    def is_active(self):
        if self.coin == 0 and self.bim < self.max_bim:
            self.bim += 1
            return True
        return False

    def convert(self, number):
        return floor(number/self.period), (number%self.period)

class Modulo:
    def __init__(self, period):
        self.period = period
        self.coin = 0

    def update(self):
        self.coin = (self.coin+1)%self.period

    def is_active(self):
        return self.coin == 0
