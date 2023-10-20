# # Exo2
# print("coffee\ncafé\ncaffè\nkaffee")


# # Exo3
# a=float(input("How much ?\n"))
# print("the number is : {}".format(a))


# # Exo4
# a=223/71
# b=(1+1/10)**10
# c=(1+1/100)**100
# d=(1+1/1000)**1000

# print(a,b,c,d)


# # Exo5
# print('sparrow'>'eagle')
# print('dog'>'cat' or 45%3==0)
# print(60-45/5+10==1)


# entrainement
# a=2
# b=3
# area=a*b
# print("The area {} and {} is {} ".format(a,b, area))



# import math
# r=float(input("enter r : "))
# h=float(input("Enter h : "))
# v=(1/3)*math.pi*r*r*h
# print("The volume is {}".format(v))


# degre=float(input("Enter a temperature in degrees Celsius : "))
# kelv=degre+273.15
# print("The temperature in kelvin is {}".format(kelv))


# num1=float(input("Enter a numeric value: "))
# num2=float(input("Enter another numeric value: "))
# sum=num1+num2
# product=num1*num2
# print("The sum of {} and {} is {}".format(num1, num2, sum))
# print("The product of {} and {} is {}".format(num1, num2, product))



############
# size=float(input("Enter the size of the cube"))
# aera=size*6*size

# volume=size**3

# print("The aera is : {} cm^2 and the volume : {} cm^3".format(aera,volume))


# b10=int(input("How much banknotes of 10 u have ? "))*10
# b20=int(input("How much banknotes of 20 u have ? "))*20
# b50=int(input("How much banknotes of 50 u have ? "))*50

# sum=b10+b20+b50

# print("you have {} €".format(sum))

# import math
# r=float(input("radius :"))
# l=2*math.pi*r
# a=math.pi*(r**2)
# print("the aera : {} and the circumference : {}".format(a,l))

# import math
# # A=input("enter A")
# # Ea=input("enter Ea")
# # T=input("Enter")
# # k=A*math.exp(-Ea/(R*T))

# a=float(input("Enter a : "))
# b=float(input("Enter b : "))
# deg=float(input("Enter degree : "))

# c=math.sqrt(a*a+b*b-2*a*b*math.cos(deg*math.pi/180))
# print("c equal {}".format(c))

# size = float(input("Enter ur size (meter plz) : "))
# weight=float(input("Enter ur weight : "))
# bmi = weight/(size*size)
# if bmi<18.32 :
#     print("underweight")
# elif bmi>=18.32 and bmi < 23.63 :
#     print("Normal")
# elif bmi>=23.63 and bmi < 25.26 :
#     print("overweight")
# else :
#     print("OBESITY, do sport u're too fat")


# #Division

# num1= int(input("enter the first number : "))
# num2= int(input("enter the second number : "))
# q=num1//num2
# re=num1%num2
# if(re==0):
#     print("{} is divisible by {}".format(num1,num2))
#     print("The quotient is {}".format(q))
# else :
#     print("{} is not divisible by {}".format(num1,num2))
#     print("The quotient is {} and the remainder is {}".format(q, re))

# #maximum, minimum

# num1= float(input("enter the first number : "))
# num2= float(input("enter the second number : "))
# if num1>=num2 :
#     print("The maximum is {} and the minimum is {}".format(num1,num2))
# else :
#     print("The maximum is {} and the minimum is {}".format(num2,num1))


# #unit electricity
# num1= float(input("enter the units : "))
# if num1<=100:
#     print("No charge")
# elif num1<=200 and num1>100:
#     print("Charge : ", (num1-100)*5)
# elif num1>200:
#     print("Charge : ", ((100*5)+(num1-200)*10))


# num=int(input("enter"))

# while num>0:
#     res=num//3
#     print("Divion of {} by 3 : {}".format(num,res))
#     num=int(input("enter"))
# print("Done")


# num=int(input("enter"))
# ndiv=1
# while ndiv<num :
#     res=num//ndiv
#     print("Divion of {} by {} : {}".format(num,ndiv,res))
#     ndiv=ndiv+1
# print("done")
# print("total : {}".format(ndiv))

# num=int(input("enter"))
# ndiv=0

# while num>0:
#     res=num//3
#     print("Divion of {} by 3 : {}".format(num,res))
#     ndiv=ndiv+1
#     print("Nb of divions so far : {}".format(ndiv))
#     num=int(input("enter"))
# print("Done")


# a=0
# for i in range (1,212):
#     if(i%3==0): a+=1
# print(a)

# sum=0
# for i in range (10): sum+=i
# print(sum)

# stop=0
# sum=0
# while(stop<10):
#     stop+=1
#     sum+=int(input("enter the number {} : ".format(stop)))

# print(sum/10)
# tot=1
# num=int(input("enter : "))
# while(num>1):
#     tot*=num
#     num=num-1
# print("Facto : {}".format(tot))

# name ="Jessa45roy"
# size=len(name)
# i=-1
# while i < size-1:
#     i+=1
#     if not name[i].isalpha():
#         continue
#     print(name[i], end =' ')

# n=int(input("Enter the value of n : "))
# for i in range (n):
#     q_i =i**2
#     print(q_i)

# sum=0
# n=int(input("enter a integer : "))
# for i in range (1,n+1) :
#     sum+=i
# print("The sum is : {}".format(sum))

# sum=0
# n=int(input("enter a integer : "))
# for i in range (1,n+1) :
#     sum+=((i+1)/i**2)
# print("The sum is : {: .2f}".format(sum))


# sum=1
# n=int(input("enter a integer : "))
# for i in range (1,n+1) :
#     sum*=i
# print("The sum is : {}".format(sum))



# for i in range (11,100) :
#     if(i%10!=0):
#         print("{}".format(i))


# for i in range (1,10) :
#     for j in range (1,10) :
#         print("{}{}".format(i,j))

# for i in range (1,10) :
#     for j in range (1,10) :
#         if(i!=j):
#             print("{}{}".format(i,j))
 
# for i in range (0,10) :
#     for j in range (0,10) :
#         for k in range(0,10):
#             if((i**3+j**3+k**3)==(i*100+j*10+k)):
#                 print("{}{}{}".format(i,j,k))
 



# n=int(input("enter a integer : "))
# for i in range (1,n+1) :
#     if(n%i==0):
#         print("{}".format(i))


# for j in range (984378325,1000000000):
#     #n=int(input("enter a integer : "))
#     n=j
#     a=0
#     for i in range (1,int(n/2)+1) :
#         if(n%i==0):
#             a+=1
#     if(a==1):
#         print("{} is prime".format(n))

# n=int(input("enter a integer : "))
# sum=2
# for i in range (0,n+1) :
#         sum+=(sum-1)+(sum-2)
#         print("{}".format(sum))

# thelist = ['Virgil','Mehdi','Stepane','JB','Martin','Tiago']
# print(thelist[2])
# thelist.append("Bruno")
# thelist.remove('Bruno')
# print(len(thelist))

# integer=[1,2,3,4]
# print(integer)
# smooth=[3.14,-7,3j,'water',False,[1,2]]
# print(smooth[3][4])

# n=int(input('enter a number : '))
# sum=0
# thelist=[]
# for i in range (1,n+1):
#     thelist.append(i)
#     sum+=(1/thelist[i-1])
# print("{: .2f}".format(sum))




# a=[1,3,5,7,11]
# b=[13,17]
# c=a+b
# print(c)
# b[0]=-1
# d=[]
# for e in a:
#     d.append(e+1)

# print(d)
# d.append(b[0]+1)
# d.append(b[-1]+1)
# print(d)
# print(d[-2:])
# print(d[:-1])
# print(d[1:4])

# n=int(input('enter a number : '))
# thelist=[]
# for i in range (0,n+1):
#     thelist.append(i)
#     thelist[i]=thelist[i]**2
# print(thelist)

# name="."
# names=[]
# grades=[]
# while (name!=""):
#         name=input("name : ")
#         names.append(name)
#         if(name!=""):
#                 grades.append(int(input("grade : ")))



# for i in range (0,len(names)-1):
#         print(names[i], grades[i])

# sum=0
# for i in range (0,len(names)-1):
#         sum+=grades[i]
# print("The average grade is {}".format(sum/len(grades)))
    

# numb=0
# numbers=[]
# while (type(numb)==int):
#         numb=input("number : ")
#         if(numb!=""):
#                 numb=int(numb)
#                 numbers.append(numb)
# sum=0
# for i in range (0,len(numbers)):
#         sum+=numbers[i]
# print("The MEAN is {}".format(sum/len(numbers)))


# names=input("Enter the names : \n")
# for i in range (0,len(names.split(" "))):
#         print("hi",names.split(" ")[i])
# print("The number of people is {}".format(len(names.split())))

# thelist1=["H","C","N","O","S","Cl"]
# thelist2=[1.008,12.011,14.007,15.999,32.065,35.453]
# sum=0
# for i in range (0,len(thelist1)):
#                 number=int(input("How much {} do you have ? : ".format(thelist1[i])))
#                 sum+=thelist2[i]*number
# print("The molecular mass is : {}".format(sum))


# thelist=[]
# n=int(input("Enter the max degree of the polynopmial : "))
# for i in range(0,n+1):
#     thelist.append(float(input("What is the coefficient at the degree {}".format(i))))

# x=float(input("Enter a value of x : "))

# calcul=thelist[0]
# for i in range(1,n+1):
#         calcul+=thelist[i]*(x**i)

# print(calcul)



#keys()
#values

# cc={"USA":"Washington DC","France":"Paris","Portugal":"Lisboa"}
# print(cc["USA"])


# myl={1:"Hello","Hi":25,"Howdy":100}

# print(1 in myl)

# print("Howdy" not in myl)
# print("Hello" in myl)

# cities={'Paris','Athens'}
# continent='Europe'
# mydict=dict.fromkeys(cities,continent)

# print(mydict)

# keys=['Ten','Twenty','Thirty']
# values=[10,20,30]

# dict=dict.fromkeys(keys,values)
# print(dict)



# sampledict={"class":{"name":"Mike","marks"}}

# employees=['Kelly','Emma']
# defaults={"designation":'Developer',}

# dicto = {
#     "H": ["Hydrogen", 1, 14, 20],
#     "He": ["Helium", 2, 1, 4],
#     "Li": ["Lithium", 3, 453, 1603],
#     "Be": ["Beryllium", 4, 1560, 2742],
#     "B": ["Boron", 5, 2349, 4200],
#     "C": ["Carbon", 6, 3915, 3915],
#     "N": ["Nitrogen", 7, 63, 77],
#     "O": ["Oxygen", 8, 54, 90],
#     "F": ["Fluorine", 9, 53, 85],
#     "Ne": ["Neon", 10, 25, 27]
# }


# def solidliquidgas(dicto):
#     state=""
#     symbol=""
#     while(symbol not in dicto):
#         symbol=input("Enter the symbol : ")
#     temperature=int(input("Enter the temperature (kelvin): "))
#     if(temperature<dicto[symbol][2]):
#         state="solid"
#     elif(temperature>dicto[symbol][3]):
#         state="gas"
#     else:
#         state="liquid"

#     return(state)

# print("The element is actually : {}".format(solidliquidgas(dicto)))
    

# bankdicto={"ANZ":[2.3,4.1],
#            "Bank of Australia":[0.1,5],
#            "Commonnwealth Bank":[3.5,3.8],
#            "Westpac":[3.7,3.7]
#            }

# def bank(dicto):
#     bank=""
#     while(bank not in dicto):
#         bank=input("Enter the name of the bank : ")
#     amount=float(input("Enter the amount (€): "))
#     years=int(input("Enter years : "))
#     interest=0
#     if(years<=2):
#         interest=amount*dicto[bank][0]/100
#     else:
#         interest=amount*dicto[bank][1]/100

#     print("amount each month : {}".format((interest+amount)/(12*years))) 
#     return()
    
# bank(bankdicto)



# def big(a,b):
#     if(a>=b):
#         return(a)
#     else:
#         return(b)
    
# print(big(6,9))



# def numbers():
#     thelist=[]
#     for i in range (5): thelist.append(float(input("Enter a number : ")))
#     print("Minimum : {}\nMaximum : {}".format(min(thelist),max(thelist)))
    
# numbers()


# try :
#     #some code
# except:
#     #optional block
#     #handinf or exception

# else:
#     #always
# finally:
#     #pass



# num=0
# while True :
#     try: 
#         num=int(input("enter the number : "))
#         if(num%2)==0: print("{} is Even".format(num))
#         else:print("{} is Odd".format(num))
#     except ValueError as e: print(e)
    


# def prime(value):
#     for i in range(1,value+1)

# num=0
# while True :
#     try: 
#         num=int(input("enter the number : "))
#         if(num%2)==0: print("{} is Even".format(num))
#         else:print("{} is Odd".format(num))
#     except ValueError as e: print(e)
#     except 
    

# import numpy as np


# f=np.random.randint(-10,10,size=(4,4))
# print(f)
# g=np.random.randint(-4,10,size=(3,3))
# print(g)

# print(np.linalg.det(f))
# print(np.linalg.det(g))

# stats=np.array([[1,2,3],[4,5,6]])
# print(stats)

# np.min(stats)
# print(np.min(stats,axis=0))
# print(np.min(stats,axis=1))


# matr=np.arange(10,31)

# matr[4]=1

# print("the result :",matr)
















# import numpy as np
# import matplotlib.pyplot as plt

# #%matplotlib inline

# x=np.linspace(-2,2,101)
# y=x**2
# print(x)

# plt.plot(x,y)
# plt.show()

# x=np.linspace(0,3*np.pi,500)

# plt.plot(x,np.sin(x**2))
# plt.title('chirp')
# plt.show()


# x=np.linspace(-2,2,101)
# y=x**2
# y2=x**4
# y3=x**3


# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("title")
# # plt.xlim(-1.5,1.5)
# # plt.ylim(-0.5,2.5)

# plt.plot(x,y, 'g',label="y=x^2")
# plt.plot(x,y3,'ro',label="y=x^3")
# plt.plot(x,y2,'b',label="y=x^4")
# plt.legend()
# plt.show()

# numb=int(input("number of points ?"))
# x=np.linspace(-1,1,numb)
# y=np.cos(2*np.pi*x)
# y2=np.sin(2*np.pi*x)
# plt.title("2pix")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x,y,'r',label='cos(2pix)',color='pink')
# plt.plot(x,y2,'r',label='sin(2pix)',color='magenta')
# plt.legend()
# plt.show()
# plt.savefig("trigonometric.png")



# while True :
#     try: 
#         numb=int(input("number of points ?"))
#         if(numb>0):break
#     except:
#         print("error")

# x=np.linspace(0,4,numb)
# y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
# plt.title("The fuction")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x,y,'r',label='function',color='magenta')
# plt.legend()
# plt.show()
# plt.savefig("trigonometric1.png")

# while True :
#     try: 
#         numb=int(input("number of points ?"))
#         if(numb>0):break
#     except:
#         print("error")

# while True :
#     try: 
#         temp=int(input("the temperature ?"))
#         if(temp>0):break
#     except:
#         print("error")
# x=np.linspace(2,10,numb)
# y=(0.08206*temp)/x
# plt.title("Isotherm ideal gas")
# plt.xlabel("Vm in L/mol")
# plt.ylabel("p in atm")
# plt.plot(x,y,'r',label='p',color='magenta')
# plt.legend()
# plt.show()
# plt.savefig("isotherm.jpg")

#S10_5
# import numpy as np
# import matplotlib.pyplot as plt

# n = int(input("What is the number of points: "))
# z = int(input("What is the number of isotherms: "))
# temperature = []

# for i in range(z):
#     temp = int(input("What is the value of temperature? "))
#     temperature.append(temp)

# x = np.linspace(2, 10, n)
# plt.xlabel("Vm")
# plt.ylabel("p")
# plt.title("Isotherm (ideal gas)")

# for i in range(z):
#     y = (0.08206 * temperature[i]) / x
#     plt.plot(x, y, label=("T = " + str(temperature[i]) + " K"))

# plt.legend()
# plt.show()
# # plt.savefig("isotherm.png")

# import matplotlib.pyplot as plt
# import numpy as np

# def f(x, xo, s):
#     return (1 / (np.sqrt(2 * np.pi) * s)) * np.exp(-(x - xo)**2 / (2 * s**2))

# x0 = float(input("Entrez la valeur de x0 : "))
# xn = float(input("Entrez la valeur de xn : "))
# xo = float(input("Entrez la valeur de xo : "))
# s = float(input("Entrez la valeur de s : "))
# n = int(input("Entrez le nombre de points : "))

# x = np.linspace(x0, xn, n)
# y = f(x, xo, s)

# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Fonction gaussienne")
# plt.show()