class Phone:
    name: str

    def __init__(self, name: str) -> None:
        """
        init
        """
        self.__name = name

    def get_name(self) -> str:
        """
        get the name
        """
        return self.__name
