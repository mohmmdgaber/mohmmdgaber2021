import io
def checkdoctor(x,y,z):
    file=open("doctors/doctorslist.txt",'r')
    for c in file:
        d=c.strip().split(",")
        if d[0]==x and d[1]==y and d[2]==z:
            file.close()
            return True
    file.close()
    return False
def getname(id):
        file=open("doctors/doctorslist.txt",'r')
        for c in file:
            d=c.strip().split(",")
            if d[0]==id:
                file.close()
                return d[1]
        file.close()
        return "None"

def checkname(x):
    if(sum(c.isspace() for c in x)>0):
        return "There can't be spaces for the user name"
    numbers = sum(c.isdigit() for c in x)
    letters = sum(c.isalpha() for c in x)
    if(len(x)>8):
        return "The name length is too long"
    if (len(x)<6):
        return "The name length is too short"
    if (numbers>2):
       return "the number count should be less than 2"
    if ((numbers+letters)!=len(x)):
        return "the name shouldn't have special charcters or spaces"

    return "valid"

def checkpsw(x):

    numbers = sum(c.isdigit() for c in x)
    letters = sum(c.isalpha() for c in x)
    spaces  = sum(c.isspace() for c in x)
    others  = len(x) - numbers - letters - spaces
    lenx=len(x)
    if(lenx<8):
        return "the password is too small"
    if lenx>10:
        return "the password is too short"
    if letters<1:
         return "there need to be at least one english letter"
    if numbers<1:
         return "there need to be at least one number"
    if others<1:
        return "there need to be at least one special charcters"

    return "valid"
