# --------------
import pandas as pd
import numpy as np
import math

class complex_numbers:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        res_real = self.real + other.real
        res_imag = self.imag + other.imag
        return complex_numbers(res_real,res_imag)

    def __sub__(self,other):
        res_real = self.real - other.real
        res_imag = self.imag - other.imag
        return complex_numbers(res_real,res_imag)

    def __mul__(self,other):
        res_real = self.real*other.real - self.imag*other.imag
        res_imag = self.real*other.imag + self.imag*other.real
        return complex_numbers(res_real,res_imag)

    def __truediv__(self,other):
        res_real = (self.real*other.real + self.imag*other.imag)/(pow(other.real,2)+pow(other.imag,2))
        res_imag = (self.imag*other.real-self.real*other.imag)/(pow(other.real,2)+pow(other.imag,2))
        return complex_numbers(res_real,res_imag)

    def absolute(self):
        return math.sqrt(pow(self.real  , 2) + pow(self.imag , 2))

    def argument(self):
        return round(math.degrees(math.atan(self.imag/self.real)),2)

    def conjugate(self):
        return complex_numbers(self.real,-self.imag)


comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)
comp_sum = comp_1 + comp_2
comp_diff = comp_1 - comp_2
comp_prod = comp_1 * comp_2
comp_quot = comp_1 / comp_2
comp_abs = complex_numbers.absolute(comp_1)
comp_conj = complex_numbers.conjugate(comp_1)
comp_arg = complex_numbers.argument(comp_1)



