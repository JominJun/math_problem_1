from socket import *
from sympy import Symbol, solve, diff
import time
import math

# p(x) =a*x**2 + b*x + c
# q(x) = d*x**2 + e*x + f
# p(x)q(x) = a*d*x**4 + (a*e + b*d)*x**3 + (a*f + b*e + c*d)*x**2 + (b*f + c*e)*x + c*f

"""
계수가 정수인 두 이차다항식 , P(x), Q(x)이 다음 두 조건을 모두 만족한다고 하자.

 가)  P(x)Q(x)=ax^4+bx^3+cx^2+dx+e는 x의 항등식이다.

 나) a,b,c,d,e는 각각 서로 다른 이하의 자연수

가능한 P(x)와 Q(x)의 예시 3가지(3쌍)을 구하시오.

 (예시 각각에 대한 a,b,c,d,e의 값도 표현하시오.)  
"""

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
i = 0
check1 = ""
check2 = ""
check3 = ""
check4 = ""
check5 = ""
check6 = ""

for a in range(5):
    for d in range(5):
        for b in range(5):
            for e in range(5):
                for c in range(5):
                    for f in range(5):
                        if(a*d<=5 and (a*e)+(b*d)<=5 and (a*f + b*e + c*d)<=5 and (b*f + c*e)<=5 and c*f<=5):
                            if(a*d!=(a*e)+(b*d) and (a*e)+(b*d)!=(a*f + b*e + c*d) and (a*f + b*e + c*d)!=(b*f + c*e) and (b*f + c*e)!=c*f and a*d!=c*f and a*d!=(a*f + b*e + c*d) and (a*e)+(b*d)!=(b*f + c*e) and (a*f + b*e + c*d)!=c*f and a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0):
                                if(str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check1 and str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check2 and str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check3 and str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check4 and str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check5 and str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f) != check6):

                                    i = i+1

                                    if(check1 == ""):
                                        check1 = str(a*d)+str((a*e)+(b*d))+str((a*f + b*e + c*d))+str((b*f + c*e))+str(c*f)
                                    elif(check2 == ""):
                                        check2 = str(a * d) + str((a * e) + (b * d)) + str((a * f + b * e + c * d)) + str((b * f + c * e)) + str(c * f)
                                    elif(check3 == ""):
                                        check3 = str(a * d) + str((a * e) + (b * d)) + str((a * f + b * e + c * d)) + str((b * f + c * e)) + str(c * f)
                                    elif(check4 == ""):
                                        check4 = str(a * d) + str((a * e) + (b * d)) + str((a * f + b * e + c * d)) + str((b * f + c * e)) + str(c * f)
                                    elif (check5 == ""):
                                        check5 = str(a * d) + str((a * e) + (b * d)) + str((a * f + b * e + c * d)) + str((b * f + c * e)) + str(c * f)
                                    elif(check6 == ""):
                                        check6 = str(a * d) + str((a * e) + (b * d)) + str(
                                            (a * f + b * e + c * d)) + str((b * f + c * e)) + str(c * f)

                                    print("==========[CASE "+str(i)+"]==========")
                                    print("P(x) = "+str(a)+"x^2+"+str(b)+"x+"+str(c))
                                    print("Q(x) = " + str(d) + "x^2+" + str(e) + "x+" + str(f))
                                    print("============================\n")
