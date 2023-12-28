import sys
import numpy as np
from typing import Callable

FUNCTIONS = {
    "identity": lambda x: x,
    "xsquare": lambda x: x*x,
    "xcube": lambda x: np.power(x, 3),
    "sin": lambda x: np.sin(x),
}


def deriv(func: Callable[[np.ndarray], np.ndarray],
          input_: np.ndarray,
          delta: float = 0.001) -> np.ndarray:
    """
    Evalutes the derivative of function `func` at every element in the the
    `input_` array.
    """
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"""Usage: python {sys.argv[0]} <funcname> <inputarray> <delta>
Functions: {FUNCTIONS.keys()}
Example: python {sys.argv[0]} xsquare "1 2 3 4" 0.001"
""")
        exit(1)

    func = FUNCTIONS[sys.argv[1]]
    input_ = np.fromstring(sys.argv[2], sep=' ')
    delta = float(sys.argv[3])
    print(deriv(func, input_, delta))
