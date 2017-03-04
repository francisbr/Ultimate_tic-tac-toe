class Case:

    def __init__(self, case_bin):
        self._case_bin = case_bin

    def toString(self):
        if self._case_bin == "00":
            return " . "
        elif self._case_bin == "01":
            return " x "
        elif self._case_bin == "10":
            return " o "

