import numpy as np
import pickle
import time


class Neuralnet(object):
    
    def __init__(self):
        
        self.inputsize = 2
        self.hiddensize = 3
        self.outputsize = 1

        self.weight1 = np.random.randn(self.inputsize,self.hiddensize)                 #(2,3)
        self.weight2 = np.random.randn(self.hiddensize,self.outputsize)                #(3,1)
        self.bias1 = np.zeros((1,self.hiddensize))                                     #(1,3)
        self.bias2 = np.zeros((1,self.outputsize))                                     #(1,1)
        
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def train(self,X,Y):
        
       for epoch in range(8000):
            iteration = 0
            while iteration < len(X):

                #batch inputs
                x = X[iteration:iteration+1]                                            #(1,2)
                target = Y[iteration:iteration+1]                                       #(1,1)
            
                #feedforward
                z1 = np.dot(x,self.weight1) + self.bias1                                #(1,2).(2,3)+(1,3)=(1,3)
                a1 = self.sigmoid(z1)                                                   #(1,3)
                a2 = np.array([1,1,1])
                sub = np.subtract(a2,a1)
                z2 = np.dot(a1,self.weight2) + self.bias2                               #(1,3).(3,1)+(1,1)=(1,1)
                output = self.sigmoid(z2)                                               #(1,1)
               
                #error calculation
                Ek = output*(1-output)*(target-output)
                cal = a1*sub*Ek                                                         #cal=(1,3) and weight2= (3,1)
                Ej = np.multiply(cal,self.weight2.T)                                    #(1,3)*(1,3)=(1,3)
               
                learning_rate = 0.1
                
                #update weight and bias
                del_w1 = learning_rate*np.dot(x.T,Ej)           #(2,1).(1,3)==(2,3)
                self.weight1 += del_w1
                
                del_b1 = learning_rate*Ej
                self.bias1 += del_b1
                
                del_w2 = learning_rate*np.dot(a1.T,Ek)          #(1,1).(1,3)==(3,1)
                self.weight2 += del_w2

                del_b2 = learning_rate*Ek
                self.bias2 += del_b2
                
                iteration += 1

            #storing values of weight and bias in value.pkl 
            obj = [self.weight1, self.bias1, self.weight2, self.bias2]
            with open('value.pkl', 'wb') as handle:
                pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def test(self,x_test, y_test):
        with open('value.pkl', 'rb') as handle:
            b = pickle.load(handle)

        self.weight1 = b[0]
        self.bias1 = b[1]
        self.weight2 = b[2]
        self.bias2 = b[3]
        z1 = np.dot(x_test,self.weight1) + self.bias1
        a1 = self.sigmoid(z1)
        z2 = np.dot(a1,self.weight2) + self.bias2
        Y = self.sigmoid(z2)
        print("\nrequired output")
        print(y_test)
        print("\npredicted output")
        print(Y)

        
    def countdown(self,n):
        while(n>0):
            print(n)
            time.sleep(1)
            n = n-1
            if(n==0):
                print("\nTraining is COMPLETED!!!")
             

if __name__=="__main__":
    
    net = Neuralnet()

    print("\nSAROJ SHARMA 73071 ....(( WELCOME!!! ))....") 
    
    #XOR gate
    print("Implementation of AND gate")
    x_train = np.array([[0,0],[0,1],[1,0],[1,1]])
    y_train = np.array([[0],[0],[0],[1]])
    print("\nTraining...PLEASE WAIT IT MAY TAKE SEVERAL MINUTES!!!")
    net.train(x_train, y_train)                    #------->>> after training net.train(x_train, y_train) function call can be changed into comment

    #net.countdown(50)
               
    x_test = np.array([[0,0],[0,1],[1,0],[1,1]])
    y_test = np.array([[0],[0],[0],[1]])
    print("\nTesting...")
    print("\ninput is",x_train)
    net.test(x_test, y_test)
    print("\nafter training net.train(x_train, y_train) function call can be changed into comment")
    print("\nhttps://github.com/sarojsharma")


    

    

        
