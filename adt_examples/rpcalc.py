"""Reverse Polish."""
from numbers import Number
from math import cos, sin


class RPCalc():
    """Reverse Polish."""

    def __init__(self):
        """Init."""
        self.list = []

    def __len__(self):
        """Return length."""
        return len(self.list)

    def pop(self):
        """_summary_.

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        if len(self.list) == 0:
            raise Exception
        return self.list.pop()

    def peek(self):
        """_summary_.

        Returns:
            _type_: _description_
        """
        return self.list[-1]

    def _twovariable(self, a, b, op):
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case "/":
                return a / b

    def _onevariable(self, a, op):
        match op:
            case 'cos':
                return cos(a)
            case 'sin':
                return sin(a)

    def push(self, n):
        """_summary_.

        Args:
            n (_type_): _description_
        """
        if isinstance(n, Number):
            self.list.append(n)
            return
        if isinstance(n, str):
            match n:
                case '+' | '-' | '*' | '/':
                    val2 = self.pop()
                    val1 = self.pop()
                    self.list.append(self._twovariable(val1, val2, n))
                case 'sin' | 'cos':
                    self.list.append(self._onevariable(self.pop(), n))
