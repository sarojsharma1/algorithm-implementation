
#Linear_Congruential_method

def randomnum():
    
    m = int(input("Enter the value of modulus, m = "))

    while True:
    
        print("Enter the seed/start value Xo, such that 'Xo' is greater or equal to zero and 'Xo' is less or equal to",m)
        Xo = int(input("Xo = "))

        if 0<=Xo<=m:

            while True:
                print("Enter the multiplier value 'a', such that 'a' is greater than zero and 'a' is less than",m)
                a = int(input("a = "))
    
                if 0<a<m:
                    while True:
                        print("Enter the increment value 'c', such that 'c' is greater or equal to zero and 'c' is less than",m)
                        c = int(input("c = "))

                        if 0<=c<m:
            
                            if c==0:
                                print("Case I: Multiplicative Congruential method")
                            elif (a==1):
                                print("Case II: Additive Congruential method")
                            elif (c!=0 & a>1):
                                print("Case III: Mixed Congruential method")
                            else:
                                print("Linear Congruential method")
                
                            n = int(input("Enter the number 'n' you want to generate sequence of pseudo random values(integer), n = "))
                            print("\n")
                            list1 = []
                            list2 = []
                            for i in range(n):
                                Xi = (a*Xo + c) % m
                                Xo = Xi
                                ri = Xi / m
                                Ri = round(ri, 3)
                                list1.append(Xi)
                                list2.append(Ri)
                                
                            print("Random integer values(Xi) = ",list1,"\n")
                            print("Random numbers(Ri) = ",list2)
                            return
                        
                        else:
                            print("Error,re-enter Again!!!")
            
                else:
                    print("Error,re-enter Again!!!")
                            
        else:
            print("Error,re-enter Again!!!")

if __name__ == "__main__":
    
    print("Saroj Sharma,BCT B 73071")
    print("\n")
    print("--------Linear Congruential method","\n",
          "--------Techniques for Generating Random Number","\n",
          "--------produce a sequence of integers x1, x2...between 0 and m-1","\n")
    randomnum()
