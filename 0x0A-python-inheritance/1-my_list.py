#!/usr/bin/python3
"""definition for derived class My list"""


class MyList(list):
    """defines a subclass of list"""
    def print_sorted(self):
        """custom method to sort and print a list"""
        self.sort()
        print(self)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/1-my_list.txt')
