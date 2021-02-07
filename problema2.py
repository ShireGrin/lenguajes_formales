import re

n = int(input())
for i in range(n):
    line = input()
    is_invalid = False
    
    invalid = re.sub(r'[0-9\-]+', '', line)
    if len(invalid) > 0:
        is_invalid = True

    card = re.sub(r'[^0-9\-]+', '', line)
    if(len(card) == 19):
        for s in card.split("-"):
            if (len(s) != 4):
                is_invalid = True
                break
    elif(len(card) > 19):
        is_invalid = True

    card = re.sub(r'[^0-9]+', '', line)
    if((card[0] == '4') or (card[0] == '5') or (card[0] == '6')) and (not is_invalid) and (len(card) == 16):
        counter = 0; character = ''
        for c in card:
            if c == character:
                counter += 1
                if counter > 3:
                    is_invalid = True
                    break
            else:
                counter = 1
                character = c
    else:
        is_invalid = True                
        
    if(is_invalid):
        print("Invalid")
    else:
        print("Valid")
