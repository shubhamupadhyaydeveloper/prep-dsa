# def reverseNum(number: int):
#     INT_MAX = 2**31 - 1
#     INT_MIN = -(2**31)

#     isNegative = number < 0
#     originalNum = abs(number)
#     reverseNum = 0

#     while originalNum != 0:
#         currentNum = originalNum % 10
#         originalNum = originalNum // 10
#         reverseNum = reverseNum * 10 + currentNum

#     if reverseNum >= INT_MAX or reverseNum <= INT_MIN:
#         return 0

#     return -reverseNum if isNegative else reverseNum


def isPalindrome(num: int):
    if num < 0:
        return False
    
    actualNum = str(num)
    if len(actualNum) <= 1:
        return True

    startIndex = 0
    endIndex = len(actualNum) - 1

    while startIndex <= endIndex:
        if actualNum[startIndex] != actualNum[endIndex]:
            return False

        startIndex += 1
        endIndex -= 1

    return True


print(isPalindrome(1211))
