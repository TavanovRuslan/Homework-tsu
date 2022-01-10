class Dual:
    real = 0.0
    dual = 0.0

    def __init__(self, a, b):
        self.real = a
        self.dual = b

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        else:
            return Dual(self.real + other, self.dual)

    # если я вообще правильно понял суть этого метода (тут other + self, а в add self + other)
    def __radd__(self, other):
        if isinstance(other, Dual):
            return Dual(other.real + self.real, other.dual + self.dual)
        else:
            return Dual(other.real + self.real, other.dual)

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        else:
            return Dual(self.real - other, self.dual)

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real * other.real, self.real * other.dual + self.dual * other.real)
