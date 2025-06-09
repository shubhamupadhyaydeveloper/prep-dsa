import re


# 1233 -> 1 + 2 + 3 + 3
def sumOfDigits(number):
    if number == 0:
        return 0

    valueToBeAdd = number % 10
    newNumber = round(number // 10)

    return valueToBeAdd + sumOfDigits(newNumber)


def calculatePower(number, power):
    if power == 0:
        return 1
    if power == 1:
        return number
    elif power < 0:
        return 1 / number * calculatePower(number, power + 1)

    return number * calculatePower(number, power - 1)


# def greatestCommonDiviser(numbers: list[int]):
#     def commonDiviser(numbers: list[int], diviser: int = 1):
#         if diviser >= max(numbers):
#             return []

#         if all(num % diviser == 0 for num in numbers):
#             return [diviser] + commonDiviser(numbers, diviser + 1)

#         return commonDiviser(numbers, diviser + 1)

#     allCommonFactor = commonDiviser(numbers, 1)

#     return max(allCommonFactor)

# print(greatestCommonDiviser([8,12]))


def greatestCommonDivisor(firstNum: int, secondNum: int):
    assert firstNum > secondNum, "first value must be greater than second value"
    assert (
        int(firstNum) == firstNum and int(secondNum) == secondNum
    ), "numbers must be integers only"
    if firstNum % secondNum == 0:
        return secondNum

    return greatestCommonDivisor(secondNum, firstNum % secondNum)


# print(greatestCommonDivisor(48,18))


def convertIntoBinary(number: int):
    assert int(number) == number, "The parameter must be integer only"

    nextNumber = number // 2
    remainder = number % 2

    if nextNumber == 0:
        return f"{remainder}"

    return convertIntoBinary(nextNumber) + f"{remainder}"


# print(convertIntoBinary(13))


def power(base, exponent):
    if exponent == 0:
        return 1
    return 2 * power(base, exponent - 1)


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    currentNum = arr[0]
    return currentNum * productOfArray(arr[1:])


def reverseString(word: str):
    if len(word) == 0:
        return ""

    return reverseString(word[1:]) + f"{word[0]}"


def isPalindrome(word: str) -> bool:
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return isPalindrome(word[1:-1])


# print(isPalindrome('tacocat'))


def isOdd(num: int):
    if num % 2 == 0:
        return False
    return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False

    if cb(arr[0]):
        return True

    return someRecursive(arr[1:], cb)


def flatten(arr: list[int]):
    if len(arr) == 0:
        return []

    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    else:
        return [arr[0]] + flatten(arr[1:])


def capitalizeFirst(words: list[str]):
    if len(words) == 0:
        return []

    return [words[0].capitalize()] + capitalizeFirst(words[1:])


myDict = {
    "Hello": {"Hello2": {"num": 3}},
    "Hello1": {"num": 3},
    "Hello4": {"num": 4},
    "Hello5": 4,
}

obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"},
    },
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}


def nestedEvenSum(mydict: dict):
    if len(mydict) == 0:
        return 0

    currentValue = list(mydict.values())[0]
    restValues = dict(list(mydict.items())[1:])

    if isinstance(currentValue, int) and not isinstance(currentValue, bool):
        if currentValue % 2 == 0:
            return currentValue + nestedEvenSum(restValues)
        else:
            return nestedEvenSum(restValues)

    elif isinstance(currentValue, dict):
        return nestedEvenSum(currentValue) + nestedEvenSum(restValues)

    return nestedEvenSum(restValues)


def capitalizeWords(arr):
    if len(arr) == 0:
        return []

    return [f"{arr[0].upper()}"] + capitalizeWords(arr[1:])


myWords = ["i", "am", "learning", "recursion"]
# print(capitalizeWords(myWords))


def reverseList(myList: list[int]):
    if len(myList) == 0:
        return []

    return reverseList(myList[1:]) + [myList[0]]


customList = [1, 2, 3, 4, 5]
# print(reverseList(customList))


# def isPalindrome(word):
#     actualWord = re.sub(r'[^a-zA-Z0-9]','',word).lower()
#     if len(actualWord) <= 1:
#         return True

#     if actualWord[0] != actualWord[-1]:
#         return False

#     return isPalindrome(actualWord[1:-1])

# print(isPalindrome('A man, a plan, a canal: Panama'))


# def fib(n):
#     if n < 1:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# print(fib(3))

def isPalindrome(word:str):
    if len(word) <= 1:
        return True
