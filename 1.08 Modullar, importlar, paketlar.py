# 1. Butun son qabul qiladigan va uning raqamlar yig’indisini qaytaradigan funksiya yarating 108 -> 9
# def getSum(n):
#     sum = 0
#     while (n != 0):
#         sum = sum + int(n % 10)
#         n = int(n / 10)
#
#     return sum
#
#
#
# if __name__ == "__main__":
#     n = 687
#
#
#     print(getSum(n))


#---------------------------------------------------------------------------
#2 Sekundlar sonini qabul qiladigan va ularni kunlarda- soatlarda-minutlarda-sekundlarda qaytaradigan funksiya yarating
import time


# def convert(seconds):
#     min, sec = divmod(seconds, 60)
#     hour, min = divmod(min, 60)
#     datetime, hour = divmod(hour, 24)
#     return '%d: %d:%02d:%02d' % (datetime, hour, min, sec)
#
#
# # Driver program
# n = 91000
# print(convert(n))