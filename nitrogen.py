from base64 import urlsafe_b64decode
from optparse import check_builtin
import random
import string


def gen():
    import random

    upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letter = "abcdefghijklmnopqrstuvwxyz"
    digits = "012345689"

    numbtogen = input("Wie vile soll ich generieren?")
    upper, lower, nums, = True, True, True,
    all = ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums:
        all += digits

        lenght = 23
        amount = numbtogen

        for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all, lenght))
            print("discord.gift/" + nitro)
            
gen()
gen()
gen()