class Case:

    def __init__(self, case_bin, position, maj=False):
        self._case_bin = case_bin
        self._position = position
        self._maj = maj
        self._case_str = " . "
        self._is_empty = True
        self._convert()

    def _convert(self):
        if self._case_bin == "01":
            self._is_empty = False
            if self._maj:
                self._case_str = " X "
            else:
                self._case_str = " x "
        elif self._case_bin == "10":
            self._is_empty = False
            if self._maj:
                self._case_str = " O "
            else:
                self._case_str = " o "

    def toString(self):
        return self._case_str

    def is_x(self):
        if self._case_bin == '01':
            return True
        return False

    def is_o(self):
        if self._case_bin == '10':
            return True
        return False

    def is_empty(self):
        return self._is_empty

    def get_position(self):
        return int(self._position)

    def get_bin_position(self):
        bin_position = str(bin(int(self._position))[2:])
        while len(bin_position) < 7:
            bin_position = '0' + bin_position
        return bin_position
