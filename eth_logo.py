"""
Print next ascii art using only `loop` statements (size: 38x37):
                  #
                 ###
                #####
               #######
              #########
             ###########
            #############
           ###############
          #################
         ###################
        #####################
       #######################
      #########################
     ###########################
    #############################
   ###############################
  #################################
 ###################################
#####################################
  #################################
#    ###########################    #
 ###    #####################    ###
  #####    ###############    #####
   #######    #########    #######
    #########     #     #########
     ############   ############
      #########################
       #######################
        #####################
         ###################
          #################
           ###############
            #############
             ###########
              #########
               #######
                #####
                 ###
                  #
"""
SIZE = 38
HASH = '#'
SPACE = ' '
GAP = '+'

# Calculate sizes (applying min resolution limit and rounding)
height = max((SIZE // 3) * 3, 15)  # Size: 15 is the smallest
height = height + 2 if height % 2 == 0 else height - 1
width = height - 1
top = height // 2
bottom = height // 3
middle = height - top - bottom
print(f'height: {height}, top: {top}, middle: {middle}\n')  # Only for debug

for i in range(0, top):
    hashes = HASH * (2 * i + 1)
    spaces = SPACE * (top - i - 1)
    # print(spaces + hashes + spaces)
    print(spaces + hashes + spaces, f' | i: {i}, end: {top}')  # Only for debug

for i in range(top, top + middle):
    x = i - top
    # side_hashes = HASH * (x * 2 - 1) if x < middle - 1 else HASH * (x * 2)
    if x == 0:
        side_hashes = HASH * 0
        gap = GAP * 2
        mid_hashes = HASH * (2 * i - 5)
    elif x < middle - 2:
        side_hashes = HASH * (x * 2 - 1)
        gap = GAP * 4
        mid_hashes = HASH * ((2 * i - 5) - (8 * x))
    elif x == middle - 2:
        side_hashes = HASH * (x * 2 - 1)
        gap = GAP * 5
        mid_hashes = HASH
    else:
        side_hashes = HASH * (x * 2)
        gap = GAP * 1
        mid_hashes = gap

    hashes = side_hashes + gap + mid_hashes + gap + side_hashes
    spaces = SPACE * (x - 1)
    # print(spaces + hashes + spaces)
    print(spaces + hashes + spaces, f' | i: {i}, end: {top + middle}, x: {x}')  # Only for debug

for i in range(top + middle, height + 1):
    hashes = HASH * (2 * (height - i) + 1)
    spaces = SPACE * (i - top - 1)
    # print(spaces + hashes + spaces)
    print(spaces + hashes + spaces, f' | i: {i}, end: {height + 1}')  # Only for debug
