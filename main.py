from functions import*
from classes import* 
from tkinter import *
from numpy import*
import turtle

root = Tk()



# x1 = np.linspace(0,5,100)
# y1 = x1**2
# plt.title('Business Plan')
# plt.xlabel('Time')
# plt.ylabel('Money')  
# plt.plot(x1,y1,'r*-')
# plt.show()


# x1 = np.linspace(0,5,10)
# y1 = x1**3
# plt.subplot(1,2,1)
# plt.plot(x1,y1,'r')
# plt.subplot(1,2,2)
# plt.plot(x1,y1,'b')
# plt.show()

# x1 = np.linspace(0,5,10)
# y1 = x1**2

# Figure size is (xLength, yLength)
# fig1 = plt.figure(figsize=(5,4), dpi=100)
# axes1 = fig1.add_axes([0.1,0.1,0.9,0.9])
# axes1.set_title('Title')
# axes1.set_xlabel('Time')
# axes1.set_ylabel('Money')
# axes1.plot(x1,y1,label='Profits')
# axes1.legend(loc=0)
# plt.show()

# Creates a graph by clicking a button
def clicking():
    x1 = np.linspace(0,5,100)
    y1 = x1**2
    plt.title('Business Plan')
    plt.xlabel('Time')
    plt.ylabel('Money')  
    plt.plot(x1,y1,'r*-')
    plt.show()
    
# Creates a graph by clicking a button    
def clicking2():
    x1 = np.linspace(0,5,100)
    y1 = x1**2
    # Figure size is (xLength, yLength)
    fig1 = plt.figure(figsize=(5,4), dpi=100)
    axes1 = fig1.add_axes([0.1,0.1,0.9,0.9])
    axes1.set_title('Title')
    axes1.set_xlabel('Time')
    axes1.set_ylabel('Money')
    axes1.plot(x1,y1,label='Profits')
    axes1.legend(loc=0)
    plt.show()   

# Draws something when clicking a button    
def clicking3():
    t = turtle.Turtle()
    for _ in range(0,4):
        t.forward(30)
        t.right(90)
        
        
# Buttons          
myButton = Button(root, text="Show graph1", command=clicking)
myButton2 = Button(root, text="Show graph 2", command=clicking2)
myButton3 = Button(root, text="Cool Art", command=clicking3)
myButton.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()


















