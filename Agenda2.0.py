
Agenda = []
Numbers = []
elem = Agenda


Archives = open('Register.txt', 'w')

print ('Contacts: ')

for elem in Agenda:
    print ('- ' + elem)
res0 = input('What mode do you want to use? Normal, Number or Eliminate?')



def Normal():
        res = input('Do you want to add any contact?')
        while True: #here is where I wanna start again
                if res == ('yes') or res == ('Yes'):
                    print('What contact do you wanna add? Say stop when you finish or press enter')
                    newnames = input()
                    
                    Agenda.extend([newnames])
                    print(Agenda)
                    Archives.write(newnames)
                    Archives.write(', ')
                    if newnames == ('stop') or newnames == ('Stop') or newnames == (''):
                        Archives.write('\n')
                        Archives.close()

                        break
            
                else:
                    res1 = input('¿Are you sure you dont want to add any contact ?')
                    if res1 == ('No') or res1 == ('no'): #the continue returns me to this line and I wanna start again the while sentence
                        print('Ok')
                        res = "yes"
                    else:
                        
                        quit()
def Number():
    while True:
        print('What contact do you want to add?')
        newnames = input()
        print('What is the number of the contact?')
        newnumbers = input()
        if newnumbers == str:
            break
        
        Agenda.extend([newnames])
        Numbers.extend([newnumbers])
        
        
        Archives.write(newnames)
        Archives.write(', ')
        Archives.write(newnumbers)
        Archives.write('\n')
        
        
        
        print(Agenda)
        print(Numbers)
        if newnames == ('stop') or newnames == ('Stop') or newnames == (''):
            Archives.close()

            break






if res0 == ('Normal'):
    print('Normal mode selected')
    Normal()
if res0 ==  ('Number'):
    print('Number mode selected, now you can add the number phone to the names')
    Number()


if res0 == ('Eliminate') or res0 == ('eliminate'):
    print('Eliminando archivos...')
    Archives.truncate()
    print('Se ha eliminado todo correctamente')
    Archives.close()


Archives.close()