import random

from automate.xl_automate import correct_prices_in_the_sheet
from lcode.RomanToInteger import RomanToInteger
from ecom.shipping import calc_shipping
from getstart.utils import find_max

print(RomanToInteger.convertRomanToInteger_1("CM"))
max = find_max([4,29,47,9,6,14])
print(max)

calc_shipping()


#print(round(random()*10000,0))
#print(choice(['Arun','Arunkumar','Arun Kumar', 'Arun kumar','arun','arunkumar','arun kumar','ArunKumar','arunKumar']))
print(random.randint(1,6))
print(random.randrange(5,50,5))
print(random.randbytes(8))
print(random.getrandbits(4))

print("##########################Excel sheet##########################################")
correct_prices_in_the_sheet('./datadocs/price_list.xlsx','./datadocs/price_list_updated_v1.xlsx')
print("##########################Excel sheet##########################################")