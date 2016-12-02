def mean(data):
    # Calculates the mean of a list of ints

    return sum(data) / len(data)

  
def median(data):
    # Calculates median of a list of ints

    data.sort()

    if len(data) % 2 == 0:
        lower_value = data[len(data) // 2 - 1]
        upper_value = data[len(data) // 2]
        return mean([lower_value, upper_value])
    else:
        return data[len(data) // 2]


def mode(data):
    # Calculates mode of a list of ints and returns it as a list of modes

    modes = {}

    for i in data:
        modes[i] = modes.get(i, 0) + 1

    mode = 0
    mode_key = []

    for key in modes.keys():
        if modes[key] > mode:
            mode = modes[key]
            mode_key = [key]
        elif modes[key] == mode:
            mode_key.append(key)

    return mode_key


def range(data):
    # Calculates range of a list of ints

    data.sort()

    return data[len(data) - 1] - data[0]
