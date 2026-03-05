import random

class My_Random:
    def set_seed(self,seed):
        self.seed = seed % 10000

    def dice(self):
        a = self.seed*self.seed
        a2 = str(a).zfill(8)
        a3 = int(str(a2)[2:6])

        self.seed = a3

        return (int(a3) % 6) + 1
        






