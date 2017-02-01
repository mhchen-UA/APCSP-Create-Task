""" 
 ___     ___   _         _  	           _____   _       ____   _       _____
|   \   /   | |_|  ___  | |      _____    |  __ | | |     |  __| | |     |  __ |  ______
| |\ \_/ /| |  _  |  _| | |___  |  _  |   |  ___| | |     | |    | |___  |  ___| \   _  |
| | \___/ | | | | | |_  |  _  | | |_| |_  | |___  | |     | |__  |  _  | | |___   | | | |
|_|       |_| |_| |___| |_| |_| |_______| |_____| |_|     |____| |_| |_| |_____|  |_| |_|     
 Fixed Input Cost Market Simulation
 Date: 1/31/17
 Period:1
 """

from graphics import *
import random
import time
class Window:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.day = 0
        self.textSize = 25
        self.e = None #Entry Object
        self.accountBalance = 0
        self.revenue = 0   #Revenue
        self.stock = 0  #Quanity owned
        self.inputCost = 0 #Input Cost
        self.profit = self.revenue - self.inputCost #Profit
        self.name = "" #User's name
        self.product = ""
        #[Title,text,demand-shift]
        self.cakeNews = [   #I placed the list of news here so that its changes can be preserved
            ["CAKES ARE UNHEALTHY","The University of Anarctica has\nfound a shocking discovery on\nthe strong correlation between cakes and\ndiabetes. \'They have too much\nsugar, the public should really refrain\nfrom eating them\' says Dr. Michael,\nthe leading scientist in this study.",-20],
            ["POLICE SHOOTING SPARKS\nPROTESTS","An amateur video shot by a\nbystander, officer Repucci fatally shot an\nunarmed 9 year old girl while she was\nmaking cake. Protesters are encouraging\neveryone to buy cakes to support their\ncampaign in prosecuting Repucci.",50],
            ["NATIONAL CAKE DAY","The President of the United States has\nofficial declared this day to be National\nCake Day. Citizens world-wide are\ncelebrating by buying more cake.",200],
            ]
        self.carNews = [
            ["MITSUBISHI OPENS UP\nSTORES","The foreign company, Mitsubishi, has\nopened their ever-popular shop at the\nother side of town. Hurry up and\nget there to get the cheapest prices!\nSorry to the other car firms that have\nto compete with Mitusbishi.\nMay you rest in peace.",-40],
            ["ECONOMY BOOST","Statisticians have estimated a\nlarge increase in the incomes of\nmany Americans. \'I am delighted\nby this shift\' says economist \nDr. David. \'I expect an increase in purchases\nof expensive products like cars.\'",20],
            ["SEVERE WEATHER\nDESTROYS PARKING LOT","Severe thunderstorms were blamed for\nthe destruction of a university's parking\nlot. Investigators say that large hail\ndamaged the cars, which leaked gasoline,\nand a struck of lightning lit the\nfloor on fire.",5], 
            ]
        self.gasNews = [
            ["BOYCOTT "+self.name.upper()+"!",self.name+"'s oil rig exploded over the Gulf\nof Mexico, prompting ocean wildlife\nprotestors to boycott their gas.",0],
            ["BP DROPS OUT","The massive company, BP, has\nofficially announced on twitter that\n they're going out of business. \'That's\none less competitor for the gas\n industry\' says economist Rempala.",20],
            ["RISE IN ELECTRIC CARS","People are starting to use\nelectric cars more than \ngas-powered cars.",-10],
            ["NEW AMUSEMENT PARK BUILT","As part of the mayor\'s\n initiative to attract more\nvisitors to town, the new amusement\n park will bring in more travelers.",20]
            ]
    def createInterface(self): #makes the window and divides the sections with lines
        self.win = GraphWin("Window",self.x,self.y)
        self.line1 = Line(Point(self.x//2,self.y),Point(self.x//2,0))
        self.line2 = Line(Point(self.x//2,self.y//2),Point(self.x,self.y//2))
        self.line3 = Line(Point(0,self.y//6),Point(self.x//2,self.y//6))
        self.line4 = Line(Point(0,self.y//3),Point(self.x//2,self.y//3))
        self.line5 = Line(Point(0,self.y//2),Point(self.x//2,self.y//2))
        self.line6 = Line(Point(0,(self.y*2)//3),Point(self.x//2,(self.y*2)//3))
        self.line7 = Line(Point(0,(self.y*5)//6),Point(self.x//2,(self.y*5)//6))
        self.line1.draw(self.win)  #Drawing the lines to organize/separate the sections
        self.line2.draw(self.win)
        self.line3.draw(self.win)
        self.line4.draw(self.win)
        self.line5.draw(self.win)
        self.line6.draw(self.win)
        self.line7.draw(self.win)
        self.textDay = Text(Point(self.x//4,self.y//12),self.name+"'s "+self.product+" shop. Day "+str(self.day)) #setting texts
        self.textDay.setSize(self.textSize)
        self.textDay.draw(self.win)
        self.e = Entry(Point((self.x//4)+30,self.y//4),20)#Setting input price box
        self.e.draw(self.win)
        self.eText = Text(Point((self.x//4)-80,self.y//4),"Price: $")
        self.eText.setSize(self.textSize)
        self.eText.draw(self.win)
        self.textRevenue = Text(Point(self.x//4,(self.y*5)//12),"Stock: "+str(self.stock))
        self.textRevenue.setSize(self.textSize)
        self.textRevenue.draw(self.win)
        self.textStock = Text(Point(self.x//4,(self.y*7)//12),"Revenue: "+str(self.revenue))
        self.textStock.setSize(self.textSize)
        self.textStock.draw(self.win)
        self.textInputCost = Text(Point(self.x//4,(self.y*3)//4),"Input Cost: "+str(self.inputCost))
        self.textInputCost.setSize(self.textSize)
        self.textInputCost.draw(self.win)
        self.textProfit = Text(Point(self.x//4,(self.y*11)//12),"Profit: "+str(self.revenue - self.inputCost))
        self.textProfit.setSize(self.textSize)
        self.textProfit.draw(self.win)
        self.newsText = Text(Point((self.x*3)//4,(self.y*9)//16),"News")
        self.newsText.setSize(26)
        self.newsText.draw(self.win)
        
    def getProduct(self): #ask the user for product to sell
        product = button("Gas, Car, or Cake?",17)
        if product.lower() == "cake" or product.lower() == "car" or product.lower() == "gas":   
            self.product = product
            return product
        return self.getProduct()
    
    def setGraph(self): #create curve based on elasticity
        self.graph = Rectangle(Point((self.x*9)//16,(self.y)//16),Point((self.x*15)//16,(self.y*7)//16))
        self.graph.draw(self.win)
        self.demandCurve = Line(Point((self.x*9)//16,self.y//8),Point((self.x*27)//32,(self.y*7)//16))
        self.demandCurve.setWidth(2)
        self.demandCurve.draw(self.win)
        
    def setAccountBalance(self,product):
        if product == "car":
            self.accountBalance = 100000
        elif product == "cake":
            self.accountBalance = 5000
        elif product == "gas":
            self.accountBalance = 20000
        
    def getNews(self, product):  #gets random news
        nonews = random.randint(0,1)
        if nonews:
            return ["","",0]
        def cakeNews():
            if len(self.cakeNews)==0:  #Returns empty if there's no more news
                return ["","",0]
            selector = random.randint(0,len(self.cakeNews)-1)
            theNews = self.cakeNews[selector] 
            self.cakeNews.remove(theNews)   #Makes sure a news doesn't repeat
            return theNews
        def carNews(): 
            if len(self.carNews)==0:  #Returns empty if there's no more news
                return ["","",0]
            selector = random.randint(0,len(self.carNews)-1)
            theNews = self.carNews[selector] 
            self.carNews.remove(theNews)   #Makes sure a news doesn't repeat
            return theNews
        def gasNews():
            if len(self.gasNews)==0:  #Returns empty if there's no more news
                return ["","",0]
            selector = random.randint(0,len(self.gasNews)-1)
            theNews = self.gasNews[selector] 
            self.gasNews.remove(theNews)   #Makes sure a news doesn't repeat
            return theNews
        newsObject = None
        if product.lower() == "cake":
            return cakeNews()
        elif product.lower() == "car":
            return carNews()
        elif product.lower() == "gas":
            return gasNews()

    def setNews(self,product):
        self.newsBox = Rectangle(Point((self.x*9)//16,(self.y*19)//32),Point((self.x*15)//16,(self.y*15)//16))
        self.newsBox.draw(self.win)
        self.newsTitle = Text(Point((self.x*3)//4,(self.y*11)//16),product[0])
        self.newsTitle.setSize(20)
        self.newsTitle.draw(self.win)
        self.newsBody = Text(Point((self.x*3)//4,(self.y*13)//16),product[1])
        self.newsBody.setSize(15)
        self.newsBody.draw(self.win)

    def setCost(self,product):
        if product.lower() == "gas":
            self.inputCost = 4
        elif product.lower() == "cake":
            self.inputCost = 3
        elif product.lower() == "car":
            self.inputCost = 5000
        self.textInputCost.undraw()
        self.textInputCost = Text(Point(self.x//4,(self.y*3)//4),"Input Cost: "+str(self.inputCost))
        self.textInputCost.setSize(self.textSize)
        self.textInputCost.draw(self.win)
        
    def start(self,product,w): #Starts from Day 1, asks for price, then calculates revenue based on graph
        news = w.getNews(product)
        w.setNews(news)
        self.win.setBackground(color_rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
        self.setCost(product)
        self.setAccountBalance(product)
        self.buy()

    def getName(self):
        self.name = button("Name")

    def buy(self):
        quantityBought = button("Input Cost is "+str(self.inputCost)+" Per Unit. How much do you want to buy?",12)

def button(text,textSize=24): #I Used ABSTRACTION to make a button with a flexible text for input
        w = GraphWin("",300,200)
        TEXT = Text(Point(150,30),text)
        TEXT.setSize(textSize)
        TEXT.draw(w)
        e = Entry(Point(150,75),20)
        e.setSize(20)
        e.draw(w)
        button = Rectangle(Point(100,110),Point(200,150))
        button.setFill("Cyan") #Making a submit button
        button.draw(w)
        textSubmit = Text(Point(150,130),"Submit")
        textSubmit.setSize(15)
        textSubmit.draw(w)
        a = True
        Input = ""
        while(a):
            b = w.getMouse() #Event for if the mouse is clicked in the rectangle
            if b.getX()<200 and b.getX()>100 and b.getY() >110 and b.getY()<150:
                a = False
                Input = e.getText()
        w.close()    
        return Input

def main():
    w = Window()
    w.getName()
    product = w.getProduct()
    w.createInterface() 
    w.setGraph()
    w.start(product,w)

main()
