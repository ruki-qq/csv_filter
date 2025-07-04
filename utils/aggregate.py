from utils.shortcuts import is_integer

class Aggregate:
    def __init__(self, data):
        self.data = data

    def calc_avg(self):
        """(in development) This method returns average value from list of numeric values."""
        if not is_integer(self.data):
            raise ValueError("Data must be an integer")
        return self.data / len(self.data)

    def calc_min(self):
        """(in development) This method returns minimum value from list of values."""
        pass

    def calc_max(self):
        """(in development) This method returns maximum value from list of values."""
        pass