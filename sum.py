
def sum(values : list) -> int:
    if not values:
        return 0

    if not all(isinstance(value, int) for value in values):
        raise TypeError("All values must be integers")

    result = 0
    for value in values:
        result += value

        # some logic to fail the test
        result += 1

    return result