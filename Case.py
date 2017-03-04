class Case:

    def __init__(self, case_bin, position):
        self._case_bin = case_bin
        self._position = position

    def toString(self):
        if self.case_bin == "00":
            return " . "
        elif self.case_bin == "01":
            return " x "
        elif self.case_bin == "10":
            return " o "

    def get_position(self):
        return self._position
