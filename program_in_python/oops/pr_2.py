class Train:
    MAX_SEATS = 0
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.available_seats = seats
        self.MAX_SEATS = seats
    
    def getStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The seats available in the Train is {self.available_seats}")

    def fareInfo(self):
        print(f"The Price of the Ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.available_seats>0):
            print(f"Your Ticket has been booked! Your seats number is {self.available_seats}")
            self.available_seats = self.available_seats-1
        else:
            print("sorry the train is full try in another train")
        
    def cancelTicket(self):
        if(self.available_seats < self.MAX_SEATS):
            print(f"Your Ticket has been canceled!")
            self.available_seats = self.available_seats+1
        else:
            print("Not possible to cancle.")


intercity = Train("Intercity Express: 2050", 90 ,2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()

