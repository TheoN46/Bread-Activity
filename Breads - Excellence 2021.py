import datetime
today=datetime.datetime.now()

def force_name(message,lower,upper):
    while True: #infinite loop that will keep repeating until the if statement is met
        name=str(input(message)).title() #personalised input message which is passed as a parameter
        if len(name)>=lower and len(name)<=upper and name.isalpha():  #ensures name 2-20 characters and A-Z
            break
        else:
            print("ERROR,{}, please enter text only".format(message))
    return name #this returns a valid name that is 2-20 charcters and A-Z

def get_phone_number(message):  #Runs a message through this program
    while True: #While true loop to filter bad data
        try:
            phone_number = str(input(message))  #Asks for phone number or 0 to quit. Replace there to rid of all
            if len(phone_number) >= 9 and len(phone_number) <=12 and phone_number.isnumeric(): #If the length of phone
                break #breaks function if specifications are met
            else:   #If specs aren't met will run this
                print("Cellphone numbers only contain numbers and are between 9 and 12 digits") #Tells user to enter
        except:
                print("Please enter a valid phone number")  #Tells user to enter correct phone number
    return phone_number #Will return value to variable that called the function

#Create a subroutine for breadtype
def breads ():
    global breadtype,breadlist
    breadlist = ["White","Brown","Italian","Granary"]
    breadcount = 0
    print ("We have the following breads")
    while breadcount < 4:
        print (breadcount,"    ",breadlist[breadcount])
        breadcount = breadcount + 1
    breadtype = int(input("What number bread do you want? "))

def meats():
    global meattype,meatlist
    meatlist=["Chicken","Turkey","Tuna","Bacon"]
    meatcount= 0
    print("We have the following meats")
    while meatcount < 4:
        print(meatcount," ", meatlist[meatcount])
        meatcount += 1
    meattype = int(input("What number meat do you want"))

def cheeses():
    global cheesetype,cheeselist
    cheeselist=["Swiss", "Feta", "Brie", "Tasty"]
    cheesecount= 0
    print("We have the following chesses")
    while cheesecount < 4:
        print(cheesecount," ", cheeselist[cheesecount])
        cheesecount += 1
    cheesetype = int(input("What number cheese do you want"))

def salads ():
    global saladtype,saladlist,saladswanted
    saladlist = ["Lettuce","Tomato","Carrot","Cucumber","Onions"]
    saladcount= 0
    print("We have the following salads, you can have as many as you want")
    while saladcount < 5:
        print (saladcount," ",saladlist[saladcount])
        saladcount = saladcount + 1
    print("Press ENTER when you have finished chosing your salads")
    saladswanted = ""
    saladtype = " "
    while saladtype != "":
        saladtype = input("What number salad do you want? ")
        if saladtype != "":
            saladtype = int(saladtype)
            saladswanted = saladswanted + " " + saladlist[saladtype]

def dressings():
    global dressingstype,dressingslist
    dressingslist=["BBQ Sauce", "Ranch Dressing", "Mayo", "No Sauce"]
    dressingscount= 0
    print("We have the following dressings")
    while dressingscount < 4:
        print(dressingscount," ", dressingslist[dressingscount])
        dressingscount += 1
    dressingstype = int(input("What number dressings do you want"))

def output_order():
    breadorder=[]      #empty list
    #this adds the persons entire order details to the list
    breadorder.append(first_name)
    breadorder.append(cellphone)
    breadorder.append(breadlist[breadtype])
    breadorder.append(meatlist[meattype])
    breadorder.append(cheeselist[cheesetype])
    breadorder.append(saladswanted)
    breadorder.append(dressingslist[dressingstype])
    breadorder.append(today)
    outputFile = open("students.txt", "a") #opens the text file
    print("*********** Order for {} - {} *******".format(first_name,cellphone))     #test print to pyscipter
    outputFile.write("*********** Order for {} - {} *******".format(first_name,cellphone))
    for order in breadorder:
        print (order)       # test print to pyscripter
        outputFile.write("{}\n".format(order))
    outputFile.write("*********** End of Order: {}. *******".format(today) )
    print ("*********** End of Order: {}. *******".format(today))       #test print to pyscripter
    outputFile.close()  #closes the text file

#This is temporary code to test that the bread subroutine is working
first_name = force_name("Please enter in your name",2,20)
cellphone = get_phone_number("Please enter your cellphone")
breads()    #calling the bread function
meats()
cheeses()
salads()
dressings()
output_order()
