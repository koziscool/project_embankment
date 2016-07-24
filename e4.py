
from utils import isPal

def largestPalindrome():
    largestPal = 0;
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            if isPal(k) and k > largestPal:
                largestPal = k
    return largestPal

if __name__ == '__main__':
    print largestPalindrome()

