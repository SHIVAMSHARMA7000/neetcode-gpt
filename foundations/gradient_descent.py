class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            minimizer = init
            derivative = 2*minimizer
            init = init - (learning_rate*derivative)
        
        return round(init,5)

            

