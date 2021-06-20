from resources import card as cc
from resources import controller as c

initial_screen = """                    ######## py bank menu #######

                    what would you like to do?
                        1- create an account
                        2- delete an account
                        3- make a withdrow
                        4- make an deposit
                        5- inquire accounts
                        0- exit      
                    """
create_an_account_menu = """ please type the client name below:"""
created_menssage = "successfully created!! \n See your data below:"
continue_msg = "do you wish to continue?(y, n)"

delete_menu = " type the code and the security code of the account you would like to delete:"
cards = []

def main():
    contiue = 0
    while True:
        if contiue == "n":
            break
        else:
            print(initial_screen)
            menu_cursor = int(input())
        if menu_cursor == 1:
            print(create_an_account_menu)
            name = input()
            new_card = c.make_card(name)
            cards.append(new_card)
            print(created_menssage)
            card = c.find_card(cards, new_card.code)
            print("client name: " + str(card.name) + "\n" + "security code: " + str(card.code) + "\n" + "code: "+ str(card.sec_code))
            print(continue_msg)
            contiue = input()
        if menu_cursor == 2:
            print("############ delete an account menu##########")
            print(delete_menu)
            card_code = input()
            del_card = c.delete_card(cards, card_code)
            if del_card != 'no':
                print("account " + str(del_card.code) + " successfully deleted!!!")
            print(continue_msg)
            contiue = input()
        if menu_cursor == 3:
            print("withdrow menu")
            print(continue_msg)
            contiue = input()
        if menu_cursor == 4:
            print("make an deposit menu")
            print(continue_msg)
            contiue = input()
        if menu_cursor == 5:
            print("########### inquire menu ###########")
            print("type the code of the account you would like ot inquire case you want to see all accounts type all instead ")
            code = input()
            inquire = c.find_card(cards, code)
            if code == "all":
                for i in inquire:
                    print(i.name, i.code, i.sec_code)
            else:
                print(inquire.name, inquire.code, inquire.sec_code)
            print(continue_msg)
            contiue = input()
        elif menu_cursor == 0:
            break
        elif menu_cursor > 5:
            print("option not found. Please retype your option")    

if __name__ == "__main__":
    main()