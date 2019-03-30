
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

def LeiterProblem(n): 
    global xLength
    global yLength
    # Lineares Gleichungssystem das unsere Leiter darstellt bzw. den Ansatz Punkt an der Wand
    a,b,z = var('a,b,z')
    z=n
    loesung = solve([0*a+b==z,1.6*a+b==1.6], a,b)
    a = loesung[0][0].right()
    b = loesung[0][1].right()
    f(x) = a*x+b
    a(x) = 1*x+0
    # Dieses Gleichungssystem wird gelöst und somit können wir feststellen ob die Leiter für die Gegeben Körpergröße 
    # langgenug wäre oder nicht
    xLength=solve([(loesung[0][0].right())*x+loesung[0][1].right()==0],x)
    yLength=f(0)-f((456/205))
    print "Leiterlänge {} momentan".format(sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2)) 
    # Prüfen wo sich momentan die Länge unsere Leiter befindet bzw. wie lang die gerade wäre
    if (6.5 > sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2)):
        print "Die Leiter an einem Höhrenen Punkt ansetzten damit die Länge von 6.5m funktioniert!"
        return 0
    elif (6.5 == sqrt(((xLength[0].right()^2)+(yLength^2))).n(digits=2)):
        print("Die Leiter muss bei der Höhe {}m angesetzt werden".format(n.n(digits=2)))
        # sollte eine Lösung möglich sein wird diese geplottet.
        # Hierbei stellt die Blaue Linie unsere Leiter da und die grüne Linie ist eine Diagonale die von (0,0) bis mindestens (1.6,1.6)
        # geht --> Sie ist die Diagonalle des Hindernisses das vo uns steht.
        # Deshalb trifft sie auch die Leitergerade im punkt (1.6,1.6)
        plot([f(x),a(x)],0,3).show()
        return 1
    else:
        print "Der Putz kann nicht abgtragen werden.\nFolgerung: Es muss eine längere Leiter beschafft werden!"
        return 1
    
    

    
def main():
    # Hauptprogramm 
    # Hier wird per Usereingabe die größe der Person festgelegt
    # Diese Größe wird dann an unsere Funktion übergeben und Berechnet ob die Leiter für die Körper Größe langgenug ist
    global xLength
    global yLength
    print("Wie groß bist du? ")
    counter = 7.8 - float(input())
    while(LeiterProblem(counter)==0):
        counter = counter + 0.1  
            
  
if __name__ == "__main__":
    #Programm Startpunkt --> Einsprungstelle 
    main()
    
    

