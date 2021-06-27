case = int(input())

for i in range(case):
    num1, num2 = map(int, input().split())
    print("Case #%s: %s + %s = %s" % ((i+1), num1, num2, (num1+num2)))
