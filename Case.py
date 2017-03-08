class Case:

    def __init__(self, case_bin, maj = False):
        self._case_bin = case_bin
        self.maj = maj

    def toString(self):
        if self._case_bin == "00":
            return " . "
        elif self._case_bin == "01":
            if self.maj:
                return " X "
            return " x "
        elif self._case_bin == "10":
            if self.maj:
                return " O "
            return " o "

