from math import sqrt
a = int(input())
b = int(input())
c = int(input())
if __name__ == '__main__':
    if a != 0 and b != 0 and c != 0:
        D = b ^ 2 - 4 * a * c
        if D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print (x1, x2)
        elif D == 0:
            x = -b / 2 * a
            print (x)
        else: print ("Корней нет")
    else: print ("Это не квадратное уравнение")
