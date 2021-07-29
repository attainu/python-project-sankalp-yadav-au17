class Ladders:
    # ladder
    def ladder(x,con1):
        if x == 1:
            return 38 , True
        elif x == 4:
            return 14 , True
        elif x == 9: 
            return 31 , True
        elif x == 21:
            return 42 , True
        elif x == 28:
            return 84 , True
        elif x == 72:
            return 91 , True
        elif x == 51:
            return 67 , True
        elif x == 80:
            return 99 , True
        else:
            return x , False