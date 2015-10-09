class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __repr__(self):
        return '%s/%s' % (self.num, self.den)
