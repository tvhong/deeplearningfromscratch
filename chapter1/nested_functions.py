import numpy as np
from typing import Callable, List

ArrayFunction = Callable[[np.ndarray], np.ndarray]
Chain = List[ArrayFunction]

def apply(chain: Chain, input_: np.ndarray) -> np.ndarray:
    temp = input_
    for func in chain:
        temp = func(temp)

    return temp

chain: Chain = [
        lambda x: x + 1,
        lambda x: x * x,
        lambda x: x + 3,
]

print(apply(chain, np.array([1,2,3])))
