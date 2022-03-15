class Customer:
    def __init__(self,customerId,fName,lName,ph):
        self.customerId=customerId
        self.fName=fName
        self.lName=lName
        self.ph=ph
        
    def customerId(self):
        return self.customerId
    
    def fName(self):
        return self.fName
    
    def lName(self):
        return self.lName
    
    def ph(self):
        return self.ph
    
class Flight():
    def __init__(self,flightNo,orig,dest,nSeats=50):#nSeat default to 50 if they havent entered a number
        self.flightNo=flightNo
        self.orig=orig
        self.dest=dest
        self.nSeats=nSeats
        self.numPass=0
    
    def getFlightNo(self):
        return self.flightNo
    
    def getOrig(self):
        return self.orig
    
    def getDest(self):
        return self.dest
    
    def getNSeats(self):
        return self.nSeats
    
    def getNumPass(self):
        return self.numPass
        
    def __str__(self):
        return "Flight Number: {}\nOrigin: {}\nDestination: {}\nNumber of Seats: {}\nNumber of Passengers: {}".format(self.flightNo,self.orig,self.dest,self.nSeats,self.numPass)
        
 
def menu():

    print("  Welcome to GBC Airlines")
    print("  1. Add Customer ")
    print("  2. Add Flight ")
    print("  3. Add Booking ")
    print("  4. View Flights ")
    print("  5. View Customer ")
    print("  6. View Flight ")
    print("  7. Exit ")
    
def main():
    menu()
    customerList=[]
    flightList=[]
    loop=True
    while loop:
        
        user=int(input("Please enter the following options: "))
        
        if user==1:
            print("Adding customer...")
            customerId=int(input("Please enter your customer Id: "))
            fName=input("Please enter your first name: ")
            lName=input("Please enter your last name: ")
            ph=input("Please enter your phone number: ")
            
            customerList.append(Customer(customerId,fName,lName,ph))    
            
            print("You have been added...\n")
            
            
        elif user==2:
            print("Adding Flight...")
            flightNo=int(input("Please enter the flight number: "))
            orig=input("Please enter the origin: ")
            dest=input("Pleas enter the destination: ")
            nSeat=int(input("Please enter the number of seats: "))
            
            flightList.append(Flight(flightNo,orig,dest,nSeat))
            
            print("Flight added...\n")
                
        elif user==3:
            print("Add Booking...\n")
            print("List of Flights")
            for obj in flightList:
                print("\nFlight Number: {}\nOrigin: {}\nDestination: {}\nNumber of Seats: {}\n".format(obj.flightNo,obj.orig,obj.dest,obj.nSeats))
                print("----")
            
            print("List of Customers")
            for obj in customerList:    
                print("\nCustomer ID:{}\nFirst Name: {}\nLast Name: {}\nPhone Number: {}\n".format(obj.customerId,obj.fName,obj.lName,obj.ph))
                print("----")
                
            userId=int(input("Please enter your customer ID: "))
            flightId=int(input("Please enter the flight ID: "))
            for obj in customerList:       
            
                if userId==obj.customerId:
                     print("\nCustomer Id Found\n")
                     
                else:
                    print("\nCustomer Id not found\n")
            
            for obj in flightList:
                if flightId==obj.flightNo:
                     print("Flight Id found\n")
                     
                else:
                    print("Flight Id not found\n")
                
            if obj.nSeats>0:
                print("\nCustomer has been Added\n")
                obj.nSeats+=1
            else:
                print("All flight seats are taken\n")
            
                    
                
                
        elif user==4:
            if len(flightList) > 0:
                print("View flights...")
                for obj in flightList:
                    print("\nFlight Number: {}\nOrigin: {}\nDestination: {}\nNumber of Seats: {}\n".format(obj.flightNo,obj.orig,obj.dest,obj.nSeats))
                    print("----")
            else:
                print("No flights found...")
        elif user==5:
            if len(customerList) > 0:
                print("View customers...")
                for obj in customerList:    
                    print("\nCustomer ID:{}\nFirst Name: {}\nLast Name: {}\nPhone Number: {}\n".format(obj.customerId,obj.fName,obj.lName,obj.ph))
                    print("----")
            else:
                print("No customers found...")
        elif user==6:
            if len(flightList) > 0:
                
                flightId=int(input("Please enter flight Id: "))
              
                for obj in flightList:
                    #print("Flight Number: {}\n".format(obj.flightNo))
                    
                    if flightId==obj.flightNo:
                        print("\nFlight Number: {}\nOrigin: {}\nDestination: {}\nNumber of Seats: {}\n".format(obj.flightNo,obj.orig,obj.dest,obj.nSeats))
                    else:
                        print("Flight Number not found\n")
            else:
                print("No flights found... Please book one")
            
        elif user==7:
            print("Now exiting...")
            loop=False
            break
        
        else:
            print("Please enter a valid option")
            break
        
        
        menu()

    """
    TESTING OBJECT!!!
    
    f1=Flight(1234,"Point A","Point b")
    print (f1)
    """
if __name__=='__main__':
    main()


