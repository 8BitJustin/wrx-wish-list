season_one = [
    {"Description": "JDMS Front and Rear Carbon Fiber Frameless Emblem Set - "
                    "2015-2020 WRX / STI (black)",
     "Distributor": "Subispeed",
     "Price": 95,
     "Website": "https://www.subispeed.com/2015-subaru-wrx/vinyl/emblems"
                "/jdms-front-and-rear-carbon-fiber-emblem-set-frameless-2015"
                "-2018-wrx-sti#.XoDx_5llCUk"},
    {"Description": "OLM 2018 JDM OE Style Grille",
     "Distributor": "Subispeed",
     "Price": 160,
     "Website": "https://www.subispeed.com/2015-subaru-wrx/exterior/grilles"
                "/olm-2018-jdm-oe-style-grille-2018-wrx-sti#.XjxaXGhKiUn"},
    {"Description": "Subispeed Hella Supertone Horn Kit with Bracket and "
                    "Wiring",
     "Distributor": "Subispeed",
     "Price": 88,
     "Website":
         "https://www.subispeed.com/2015-subaru-wrx/exterior/horns/subispeed"
         "-hella-supertone-horn-kit-with-bracket-and-wiring-2015-wrx-2015"
         "-sti#.XjxafGhKiUm"},
    {"Description": "WRX FA20DIT Emblem - 2015+ WRX",
     "Distributor": "Subispeed",
     "Price": 40,
     "Website": "https://www.subispeed.com/2015-subaru-wrx/vinyl/emblems/wrx"
                "-fa20dit-emblem-2015-wrx#.XoDydZllCUk"},
    {"Description": "OLM NB+R Rear Brake Light / F1 Style Reverse w/ PnP "
                    "Adapter - 15+ WRX / STI ",
     "Distributor": "Subispeed",
     "Price": 126,
     "Website":
         "https://www.subispeed.com/2015-subaru-wrx/lighting/tail-lights/olm"
         "-nb-r-rear-brake-light-f1-style-reverse-w-pnp-adapter-15-wrx-sti"
         "#.XoH6xJllCUk"}
]

item_number = 1
total_price = 0

# loops through list which contains five dictionaries
for item in season_one:

    """
    for loop that runs through each dictionary displaying information on 
    each line by line. also adds the list item number for each item. enumerate
    is used to take advantage of the index to make such possible.
    """
    for i, (k, v) in enumerate(item.items()):

        """this makes sure that if the value is an integer, it turns into a 
        string"""
        if v == isinstance(v, int):
            print(str(v))

        """
        if the index is zero, then the item number is placed in front. will 
        only happen with the first index
        """
        if i == 0:
            print(str(item_number) + ': ' + '\t' + k + ": " + str(v))
        elif i == 3:
            print('\t' + k + ": " + str(v) + '\n')
        else:
            print('\t' + k + ": " + str(v))

        """
        if the key is Price, then that integer is added to the total price 
        variable
        """
        if k == 'Price':
            total_price += v

    """for each item looped, the item number is increased by 1"""
    item_number += 1

"""prints total price once added up"""
print(total_price)