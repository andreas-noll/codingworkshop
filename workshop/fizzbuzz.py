"""FizzBuzz Module"""


def fizzbuzz(num: int) -> str:
    """Fizzbuzz method"""
    if num == 0:
        return ""
    output = ""
    for i in range(num):
        if i % 2 == 0:
            output = output + "fizz"
        else:
            output = output + "buzz"
    return output
