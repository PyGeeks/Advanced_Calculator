import math
class Normal_calsi:
    def add(self):
        a = int(input('enter a value'))
        b = int((input('enter b value')))
        print(f"sum of {a}+{b} is", a + b)

    def sub_(self):
        a = int(input('enter a value'))
        b = int((input('enter b value')))
        print(f"substraction  of {a}-{b} is", a - b)

    def mul_(self):
        a = int(input('enter a value'))
        b = int((input('enter b value')))
        print(f"multiplication of {a}*{b} is", a * b)

    def div_(self):
        a = int(input('enter a value'))
        b = int((input('enter b value')))
        print(f"division of {a}/{b} is", a / b)

class Trignometric:
    def acos(self,x):
        k=math.acos(x)
        print(k)

    def asin(self, x):
        k = math.asin(x)
        print(k)
    def atan(self, x):
        k = math.atan(x)
        print(k)

    def atan2(self,x,y):
        k = math.atan2(x,y)
        print(k)

    def cos(self, x):
        k = math.cos(x)
        print(k)

    def sin(self, x):

        k = math.sin(x)

        print(k)

    def tan(self, x):
        k = math.tan(x)
        print(k)



    class Hyperbolic:
        def cosh(self, x):
            k = math.cosh(x)
            print(k)

        def sinh(self, x):
            k = math.sinh(x)
            print(k)

        def tanh(self, x):
            k = math.tanh(x)
            print(k)

        def asinh(self, x):
            k = math.asinh(x)
            print(k)

        def acosh(self, x):
            k = math.acosh(x)
            print(k)

        def atanh(self, x):
            k = math.atanh(x)
            print(k)
class Hyperbolic:
    def cosh(self,x):
        k=math.cosh(x)
        print(k)

    def sinh(self, x):
        k = math.sinh(x)
        print(k)
    def tanh(self, x):
        k = math.tanh(x)
        print(k)

    def asinh(self,x):
        k = math.asinh(x)
        print(k)

    def acosh(self, x):
        k = math.acosh(x)
        print(k)

    def atanh(self,x):
        k = math.atanh(x)
        print(k)

class k(Normal_calsi,Trignometric,Hyperbolic):
    def main(self):
        while True:
            print('choose u r option:')
            print('1.Simple_Calculator\n2.Scientific_calculator')
            choice=input('enter u r choice:')
            if choice == '1':
                print('choose u r option')
                print('1.add()\n2.sub()\n3.mul()\n4.div()')
                choice=input('enter u r choice:')
                if choice=='1':
                    self.add()
                elif choice == '2':
                    self.sub_()
                elif choice == '3':
                    self.mul_()
                elif choice == '4':
                   try:
                       self.div_()
                   except:
                       print('zero s are not accepter')
                elif choice not in ['1', '2', '3', '4']:

                    print('Not a Valid choice')

                user_nput = input('Do You want to continue [y/n] : ')
                if user_nput in ['Y', 'y']:
                    continue
                else:
                    break
            elif choice=='2':
                print('choose u r option')
                print('1.Trignometric\n2.Hyperbolic')
                choice = input('enter u r choice:')
                if choice =='1':
                    print('choose u r option')
                    print('1.Radians\n2.degrees')
                    choice = input('enter u r choice:')
                    if choice == '1':
                        print('enter choice')
                        print('1.acos()\n2.asin()\n3.atan()\n4.atan2()\n5.cos()\n6.sin()\n7.tan()')
                        choice = input('enter u r choice:')
                        if choice=='1':
                            t=int(input('enter value'))
                            try:
                                self.acos(t)
                            except:print('please check:Given value is out of range ')
                        elif choice=='2':
                            t=int(input('enter value'))
                            try:
                                self.asin(t)
                            except:print('please check: Given value is out of range ')
                        elif choice == '3':
                            t = int(input('enter value'))
                            self.atan(t)
                        elif choice == '4':
                            o = int(input('enter value'))
                            t = int(input('enter value'))
                            self.atan2(o,t)
                        elif choice == '5':
                            t = int(input('enter value'))
                            self.cos(t)
                        elif choice == '6':
                            t = int(input('enter value'))
                            self.sin(t)
                        elif choice == '7':
                            t = int(input('enter value'))
                            self.tan(t)
                        elif choice not in ['1', '2', '3', '4', '5', '6','7']:
                            print('Not a Valid Number')

                        user_nput = input('Do You want to continue [y/n] : ')
                        if user_nput in ['Y', 'y']:
                            continue
                        else:
                            break
                    elif choice == '2':
                        print('enter choice')
                        print('1.acos()\n2.asin()\n3.atan()\n4.cos()\n5.sin()\n6.tan()')
                        choice = input('enter u r choice:')
                        if choice == '1':
                            t = int(input('enter value'))
                            self.acos(math.radians(t))
                        elif choice == '2':
                            t = int(input('enter value'))
                            self.asin(math.radians(t))
                        elif choice == '3':
                            t = int(input('enter value'))
                            self.atan(math.radians(t))

                        elif choice == '4':
                            t = int(input('enter value'))
                            self.cos(math.radians(t))
                        elif choice == '5':
                            t = int(input('enter value'))
                            self.sin(math.radians(t))
                        elif choice == '6':
                            t = int(input('enter value'))
                            self.tan(math.radians(t))
                        elif choice not in ['1', '2', '3', '4', '5', '6']:
                            print('Not a Valid Number')

                        user_nput = input('Do You want to continue [y/n] : ')
                        if user_nput in ['Y', 'y']:continue
                        else:
                            break
                elif choice =='2':
                    print('choose u r option')
                    print('1.Radians\n2.degrees')
                    choice = input('enter u r choice:')
                    if choice == '1':
                        print('enter choice')
                        print('1.cosh()\n2.sinh()\n3.tanh()\n4.asinh()\n5.acosh()\n6.atanh()')
                        choice = input('enter u r choice:')
                        if choice=='1':
                            t=int(input('enter value'))
                            self.cosh(t)
                        elif choice=='2':
                            t=int(input('enter value'))
                            self.sinh(t)
                        elif choice == '3':
                            t = int(input('enter value'))
                            self.tanh(t)
                        elif choice == '4':
                            t = int(input('enter value'))
                            o = int(input('enter value'))
                            k = t / o
                            self.asinh(k)
                        elif choice == '5':
                            t = int(input('enter value'))
                            self.acosh(t)
                        elif choice == '6':
                            t = int(input('enter value'))
                            self.atanh(t)
                        elif choice not in ['1', '2','3','4','5','6']:

                            print('Not a Valid Number')

                        user_nput = input('Do You want to continue [y/n] : ')
                        if user_nput in ['Y', 'y']:
                            continue
                        else:
                            break

                    elif choice == '2':
                        print('enter choice')
                        print('1.cosh()\n2.sinh()\n3.tanh()\n4.asinh()\n5.acosh()\n6.atanh()')
                        choice = input('enter u r choice:')
                        if choice == '1':
                            t = int(input('enter value'))
                            self.cosh(math.radians(t))
                        elif choice == '2':
                            t = int(input('enter value'))
                            self.sinh(math.radians(t))
                        elif choice == '3':
                            t = int(input('enter value'))
                            self.tanh(math.radians(t))
                        elif choice == '4':
                            t = int(input('enter value'))
                            o = int(input('enter value'))
                            k = t / o
                            self.asinh(math.radians(k))
                        elif choice == '5':
                            t = int(input('enter value'))
                            self.acosh(math.radians(t))
                        elif choice == '6':
                            t = int(input('enter value'))
                            self.atanh(math.radians(t))
                        elif choice not in ['1', '2', '3', '4', '5', '6']:
                            print('Not a Valid Number')
                        user_nput = input('Do You want to continue [y/n] : ')
                        if user_nput in ['Y', 'y']:continue
                        else:
                            break
            elif choice not in ['1', '2']:
                print('Not a Valid Number')
            user_nput = input('Do You want to continue [y/n] : ')
            if user_nput in ['Y','y']: continue
            else: break

f=k()
f.main()

