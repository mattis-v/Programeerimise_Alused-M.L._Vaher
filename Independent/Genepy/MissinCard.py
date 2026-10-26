
cards = "S6 DK H3 CK C3 HA S10 H2 C7 S2 CQ S9 H5 D7 CA D8 C2 C9 C4 HK D10 H4 S8 H7 H9 SQ DA CJ D9 C6 D2 HQ D5 SJ C8 S5 D6 HJ H8 H10 DJ S3 D3 C5 DQ D4 H6 S7 SA SK C10"

def missing_card(cards):
    cc = ["S","H","D","C"]
    cn = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    ncards = cards.split()
    print(ncards)
    for i in cc:
        for n in cn:
            for x in ncards:
                if x == i+n:
                    break
                elif x != i+n:
                    continue
            if x != i+n:
                return i+n








print(missing_card(cards))