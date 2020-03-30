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
    {"Description": "Raceseng Scepter Translucent Shift Knob - 2015+ WRX / "
                    "STI / 2013+ BRZ",
     "Distributor": "Subispeed",
     "Price": 115,
     "Website":
         "https://www.subispeed.com/2015-subaru-wrx/interior/shift-knobs"
         "/raceseng-scepter-translucent-shift-knob-2015-wrx-sti-2013-ft86"
         "#.XoDyzpllCUk"}
]

item_number = 1
total_price = 0

for item in season_one:

    for i, (k, v) in enumerate(item.items()):

        if v == isinstance(v, int):
            print(str(v))

        if i == 0:
            print(str(item_number) + ': ' + '\t' + k + ": " + str(v))
        elif i == 3:
            print('\t' + k + ": " + str(v) + '\n')
        else:
            print('\t' + k + ": " + str(v))

        if k == 'Price':
            total_price += v

    item_number += 1


print(total_price)