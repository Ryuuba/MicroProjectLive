class FSM:
    """This class is intended to implement a deterministic FSM modelling both the states and the events with integers
    """
    def __init__(self, initial_state: int = 0) -> None:
        """This method initializes a FSM object with the initial state

        Args:
            initial_state (int, optional): The initial state. Defaults to 0.
        """
        self.__current_state : int = initial_state
        self.__transitions : dict[tuple[int, int], int] = {}

    def get_current_state(self) -> int:
        """Gets the current state

        Returns:
            int: The current state of the FSM
        """
        return self.__current_state
    
    def compute_next_state(self, ev: int) -> None:
        """Updates the code of the current state according to the code of the next state

        Args:
            ev (int): The code of the event that produces the transition
        """
        self.__current_state = self.__transitions[(self.__current_state, ev)]

    def set_transition_rule(self, current_state : int, event_number : int, next_state : int) -> None:
        """Sets a new transition rule

        Args:
            current_state (int): The code number of the current state
            event_number (int): The code number of the event
            next_state (int): The code number of the next state
        """
        self.__transitions[(current_state, event_number)] = next_state














