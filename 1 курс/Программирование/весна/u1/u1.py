class Progression:
    def arithmetic(num1, ln, step):
        a=[num1]
        numx=num1
        for i in range(2,ln+1):
            numx = numx + step
            a.append(numx)
        return a
    def geometric(num1, ln, step):
        a=[num1]
        numx=num1
        for i in range(2,ln+1):
            numx = numx * step
            a.append(numx)
        return a
num1, ln, step = map(int, input().split())
print(Progression.arithmetic(num1, ln, step), Progression.geometric(num1, ln, step))