class DigitalClock:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        """Constructs a digital clock object from three parameters (h, m, s)

        Args:
            h (int, optional): The current hour. Defaults to 0.
            m (int, optional): The current minutes. Defaults to 0.
            s (int, optional): The current seconds. Defaults to 0.
        """
        assert h < 24 and h >=0
        self.__h = h
        assert m < 60 and m >= 0
        self.__m = m
        assert s < 60 and s >= 0
        self.__s = s

    def get_time(self) -> tuple[int, int, int]:
        """Returns the current time the digital clock holds

        Returns:
            tuple[int, int, int]: h, m, s in 24-H format
        """
        return self.__h, self.__m, self.__s
    
    def clear_time(self) -> None:
        """Clears the current time
        """
        self.__h, self.__m, self.__s = 0, 0, 0

    def increment(self) -> None:
        """Increments one second the current time
        """
        self.__h = self.__h + 1 if self.__m == 59 and self.__s == 59 else self.__h
        self.__h = 0 if self.__h == 24 else self.__h
        self.__m = self.__m + 1 if self.__s == 59 else self.__m
        self.__m = 0 if self.__m == 60 else self.__m
        self.__s = self.__s + 1 if self.__s < 59 else 0















