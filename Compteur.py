from abc import ABC, abstractmethod


class Compteur(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def incrementer(self):
        pass

    @abstractmethod
    def decrementer(self):
        pass


class CompteurLimite(Compteur):

    def __init__(self, value, max, min):
        Compteur.__init__(self, value)
        self.max = max
        self.min = min
        pass

    def incrementer(self):
        if (self.value < self.max):
            self.value += 1
        else:
            print(f"Max à : {self.value}.")
            pass
        print(self.value)
        pass

    def decrementer(self):
        if (self.value > self.min):
            self.value -= 1
        else:
            print(f"Min à : {self.value}.")
            pass
        print(self.value)
        pass


class CompteurModulo(CompteurLimite):

    def __init__(self, value, max, min):
        CompteurLimite.__init__(self, value, max, min)
        pass

    def incrementer(self):
        if (self.value < self.max):
            self.value += 1
        else:
            self.value = self.min
            pass
        print(self.value)
        pass

    def decrementer(self):
        if (self.value > self.min):
            self.value -= 1
        else:
            self.value = self.max
            pass
        print(self.value)
        pass


c1 = CompteurLimite(0, 10, 0)
for k in range(1, 16):
    c1.incrementer()
for k in range(1, 16):
    c1.decrementer()
print("================================")
c2 = CompteurModulo(0, 10, -10)
for k in range(1, 25):
    c2.decrementer()
