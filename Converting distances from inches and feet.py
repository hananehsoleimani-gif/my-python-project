#create variable named inch
#create variable named foot
#set both of them 0
inch = foot = 0
foot_to_meter = foot_to_centimeter = inch_to_meter = inch_to_centimeter = 0

#getting user input
def read():
    #use the global variable named foot and inch
    global foot, inch
    foot= int(input("Enter foot number: "))
    inch=int(input("Enter inch number: "))
#calculated user input(foot and inch) all 4 conversions
def calculated():
    global foot, inch
    global foot_to_meter, inch_to_meter, inch_to_centimeter , foot_to_centimeter
    foot_to_meter = foot * 0.3048
    foot_to_centimeter = 100 * foot_to_meter
    inch_to_meter = (1.0/12)*0.3048*inch
    inch_to_centimeter = 100*inch_to_meter
#printing the result of calculated
def write():
    print("the",foot, "foot is",foot_to_meter ,"meter")
    print("the",foot,"foot is" , foot_to_centimeter , "cm")
    print("the", inch,"inch is" , inch_to_meter , "meter")
    print("the" , inch , "inch is", inch_to_centimeter , "cm" )

def main():
    read()
    calculated()
    write()



