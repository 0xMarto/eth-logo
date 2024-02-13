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

SIZE = 30
HASH = '#'
SPACE = ' '
PAD = ' '


def print_icon(size=SIZE, char=HASH, back=SPACE, pad=PAD):
    height = max((size // 3) * 3, 15)
    height = height + 2 if height % 2 == 0 else height - 1
    top, bottom = height // 2, height // 3
    mid = height - (top + bottom)
    for i in range(height + 1):
        if i < top:
            hashes = char * (2 * i + 1)
        elif i < top + mid:
            x = i - top
            side = char * (x * 2 - 1 if x < mid - 1 else x * 2)
            aux = 2 if x == 0 else 1 if x == mid - 1 else 5 if x == mid - 2 else 4
            gap = back * aux
            aux = 2 * i - 5 - 8 * x
            core = char * aux if x < mid - 2 else char if x == mid - 2 else back
            hashes = side + gap + core + gap + side
        else:
            hashes = char * (2 * (height - i) + 1)
        spaces = back * (abs(i - top) - 1)
        print(pad + spaces + hashes + spaces)


print_icon(size=20)