import math
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    # RELU when alpha = 0
    """
    return [alpha * (math.exp(i) - 1) if i<=0 else i for i in x ]
