import math

def isPalindrome(x: int) -> bool:
    reverseNum = 0
    copy = x
    while copy>=1:
        reverseNum = reverseNum*10 + copy%10
        copy = math.floor(copy/10)
    print(x, reverseNum) 
    return reverseNum == x


if __name__ == "__main__":
    test = 1234443 
    print(isPalindrome(test))