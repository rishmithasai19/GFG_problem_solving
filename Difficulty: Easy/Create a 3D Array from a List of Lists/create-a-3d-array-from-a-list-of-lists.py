class Solution:
    def create3DArray(self, data):
        import numpy as np
        import ast

        data = ast.literal_eval(data)
        return np.array(data)