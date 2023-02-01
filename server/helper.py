def generate_identifer():
    import random
    identifier = ''.join(random.choice('0123456789abcdef') for i in range(16))
    return identifier