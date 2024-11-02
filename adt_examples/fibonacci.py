"""Fibonacci module."""


class Fib():
    """Return fibonacci numbers through iterator."""

    def __init__(self):
        """Define self."""
        self.value1 = 0
        self.value2 = 1

    def __iter__(self):
        """Iterate."""
        return self

    def __next__(self):
        """Define next in Fib class."""
        self.value1, self.value2 = self.value2, self.value1 + self.value2
        return self.value2


for n in Fib():
    print(n)
    if n >= 10:
        break