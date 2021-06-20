import random
import string
from resources import card as cr

def make_card(name):
    card_list = []
    digits = string.digits
    code = ''.join(random.choice(digits) for i in range(16))
    sec_code = ''.join(random.choice(digits) for i in range(3))
    new_card = cr.credit_card(name, sec_code, code)
    return new_card

def find_card(card_list, card_code):
    if card_code == "all":
        return card_list
    else:
        for card in card_list:
            if str(card.code) == str(card_code):
                return card


def delete_card(card_list, card_code):
    tb_dell = find_card(card_list, card_code)
    old_card = tb_dell
    try:
        card_list.remove(tb_dell)
        return old_card
    except:
        print("account does not exist")
        return "no"



