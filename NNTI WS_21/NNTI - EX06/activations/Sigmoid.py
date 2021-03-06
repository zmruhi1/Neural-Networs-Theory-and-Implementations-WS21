import numpy as np

class Sigmoid:
    def __init__(self) -> None:
        pass

    def __call__(self, x):
        self.x = x
        return 1 / (1 + np.exp(-x))

    def get_type(self):
        return 'activation'
    
    def grad(self, in_gradient):
        sigm_out = self.__call__(self.x)
        return sigm_out * (1-sigm_out) * in_gradient
