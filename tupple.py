clubs = ("MAN UNITED","MAN CITY","PSG",'REAL MADRID','BARCA','BRYEAN','LIVERPOOL','CHEALSEA',"SPURS",'ATLETICO')

#print(len(clubs))
# Remember this exceptional condition
#print(clubs[0:])
#if 'PSG' in clubs:
    #print('V')
#teams = list(clubs)
#teams.insert(1,7)
#teams.append(24)
#clubs = tuple(teams)    
#print(clubs)
#teams = clubs
#print(teams)
#del clubs
def Reverse(clubs):
    teams = clubs[::-1]
    return teams
print(Reverse(clubs))    
#print(clubs)
#name = ('Atharva',)
#print(name)
