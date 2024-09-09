import interface as i
import calc as c

i.welcome()
i.introduction()
list = []
run_program = True

while run_program == True:
    new_value = i.new_value()
    try:
        new_value = int(new_value)
        list.append(new_value)
    except:
        if(new_value == 'X'):
                media = c.calc_media(list)
                i.return_media(list, media)
                menu = i.menu()
                if(menu == 1):
                     i.introduction()
                     list = []
                elif(menu == 2):
                     run_program = False
                     i.thanks()
        else:
            print("Valor digitado incorreto")
        