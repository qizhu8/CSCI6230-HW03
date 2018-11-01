#!/usr/bin/env python3
import Number_Package as npkg

class Rabin(object):
    """docstring for Rabin."""
    def __init__(self, p=-1, q=-1):
        self.p = -1
        self.q = -1
        self.n = -1
        self.b = -1
        if p != -1:
            self.set_p(p)
        if p != -1:
            self.set_q(q)

    def set_p(self, p):
        if npkg.is_prime(p):
            self.p = p
            if self.q != -1:

        else:
            raise Exception("p should be a prime number")

    def set_q(self, q):
        if npkg.is_prime(q):
            self.q = q
        else:
            raise Exception("q should be a prime number")

    def update_n(self):
        if self.p != -1 and self.q != -1:
            self.n = self.p * self.q
        else:
            raise Exception("p and q should both be prime numbers")

    def set_n(self, n):
