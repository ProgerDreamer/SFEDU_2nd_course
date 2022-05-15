class Condition:
    def __init__(self, condition_func, no_true_value):
        self.check = condition_func
        self.no_true_value = no_true_value
