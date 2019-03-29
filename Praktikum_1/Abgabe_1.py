
# coding: utf-8

# In[1]:


# print out each line in the input cell not only the last one
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# expand the cell width to 100% of t 
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[2]:


xLength = 0
yLength = 0

def lol(n): 
    global xLength
    global yLength
    a,b,z = var('a,b,z')
    z=n
    loesung = solve([0*a+b==z,1.6*a+b==1.6], a,b)
    a = loesung[0][0].right()
    b = loesung[0][1].right()
    f(x) = a*x+b
    a(x) = 1*x+0
    xLength=solve([(loesung[0][0].right())*x+loesung[0][1].right()==0],x)
    yLength=f(0)-f((456/205))
    print "die Leiter länge wäre:" 
    print(sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2))
    if (6.5 > sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2)):
        print "also noch nicht 6,5m und daher können wir die Angenommene höhe erhöhen"
        return 0
    elif (6.5 == sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2)):
        print("Die Leiter muss bei der Höhe {} angesetzt werden".format(n.n(digits=2)))
        l = plot([f(x),a(x)],0,3)
        l.show()
        return 1
    else:
        print "Der Putz kann nicht abgtragen werden"
        return 1
    
    

    
def main():
    global xLength
    global yLength
    print("Wie groß bist du? ")
    counter = 7.8 - float(input())
    while(lol(counter)==0):
        counter = counter + 0.1  
            
  
if __name__ == "__main__":
    main()
    
    

