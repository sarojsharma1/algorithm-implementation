import numpy as np

class perceptron(object):

    def __init__(self):

        self.weight = np.random.randn(2,1)                              #(2,1)
        self.bias = ([[1]])                                #(1,1)
        
        


    def train(self,X,Y):
        
        iteration = 0
        lr_rate = 0.1
        while iteration < len(X):
                
            x = X[iteration:iteration+1]                           #(1,2)
            target = Y[iteration:iteration+1]                      #(1,1)
            self.weight = self.weight + lr_rate*(np.dot(x.T,target))         #(2,1)+(2,1).(1,1)=(2,1)
            self.bias = self.bias + lr_rate*target                         #(1,1)+(1,1)=(1,1)
            iteration += 1

        
        
    def check(self,X,Y):
        
        self.a = None
        self.output = []
        iteration = 0
        while iteration < len(X):
             x = X[iteration:iteration+1] 
             summation = np.sum(np.dot(self.weight,x))+self.bias                     #(2,1).(1,2)
             #print(summation)
             if(summation >= 0 ):
                 t = 1
                 #print("\ntrue")
                 
             else:
                 t = -1
                 #print("false")
                 
             self.output.append(t)    
             iteration +=1
        self.output = np.reshape(self.output,(4,1))
        #print("\ntarget",Y)
        #print("output",self.output)
        self.a = np.array_equal(self.output,Y)
       
        
        

if __name__=="__main__":

    net = perceptron()
    print("SAROJ SHARMA 73071 ((WELCOME)) ")
    print("\nImplementing OR Gate")
    print("\nsynaptic weights before training",net.weight);
    print("synaptic bias before training",net.bias);
    
    x_train = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
    y_train = np.array([[1],[1],[1],[-1]])

    while True:
        #print("hello")
        net.train(x_train,y_train)
        net.check(x_train,y_train)
        if(net.a == True):
            break

    print("\ninput is",x_train)
    print("\nrequried output",y_train)
    print("\n output is ",net.output)
    print("\nsynaptic weights after training",net.weight);
    print("\nsynaptic bias after training",net.bias);
    print("https://github.com/sarojsharma")
  
