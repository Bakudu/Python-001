#-------------------------------------------------------------------------------
# Name:        Tay Ting Xuan
# Purpose:
#
# Author:      Jared Tay
#
# Created:     15/08/2022
# Copyright:   (c) Jared Tay 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
#Import Math Module.

total_t_cost = 0.00
total_t_tnumber = 0
t_count = 1
#Variables

transaction_num = eval (input ('Enter the number of transaction\n') )
#The input for numbers of transaction need to make

#Apply nested while loop for single and multiple transactions.
while transaction_num > 0:

    print ('\nTransaction number ', t_count ,'\n')
    #To show the order of the transaction

    num_wall = int (input ('Enter the number of wall need to be tiled\n'))
    #The input for number of walls need to be tiled

    #The nested if-else statement for the single transaction.
    if num_wall > 4 or num_wall < 1:

        print('\nThe minimum and maximum number of wall can be tiled is up from 1 to 4, Please enter a valid number\n')
        #Max 4 and Min 1 of number of wall can be tiled

    else:

        total_cost = 0.00
        total_tnumber = 0
        w_count = 1
        #Variables

        # Aplly while loop for single and multiple walls need to be tiled
        while num_wall >= 1:

            print ('\nWall number ', w_count , '\n')

            height = eval (input ('Enter height of wall in meter\n'))
            width = eval ( input ('Enter width of wall in meter\n'))
            #Input for height and width of the wall

            wall_area = height * width
            print ('\nThe wall area is',"{:.3f}".format( wall_area),'square meters\n')
            #Processing and output of the area of the wall

            tile_number = math.ceil (wall_area)
            print ('The tile area in one box is 1')
            print ('\nThe number of box of tile used is',tile_number,'in total\n')
            #Processing and output of the number of tile for the wall.

            tile_type = ('Small black granite', 'Medium sunset yellow','Large oak wood effect','Extra-large white marble')
            print(tile_type)
            #Output of the type of wall

            chosen_tile = int (input ('Choose the tile type listed by ascending number order\n'))
            #Input for the type of wall chosen, the input is by number in integer form.

            #The nested if-else statement for cost of the wall with the chosen type of tile with valid and invalid number.
            if chosen_tile > 4 or chosen_tile < 1:

                print('\n\n!!!!!!PLEASE ENTER A VALID NUMBER!!!!!!\n')
                cost = 0
                tile_number = 0
                # The valid input number is between 1 to 4.

            else:

                tile_chosen = tile_type[ chosen_tile-1]
                print(tile_chosen)
                #List out the chosen tile.
                #The -1 in the process is to undo the different of first number recognision between human and computer.

                #The if else statement for the cost of the wall with the chosen type of tile
                if chosen_tile == 1:

                    cost = "{:.2f}".format( tile_number* 85.80)
                    print ('\nThe cost is RM',cost,'\n')

                elif chosen_tile == 2:

                    cost = "{:.2f}".format( tile_number* 55.00)
                    print ('\nThe cost is RM',cost,'\n')

                elif chosen_tile == 3:

                    cost = "{:.2f}".format( tile_number* 286.00)
                    print ('\nThe cost is RM',cost,'\n')

                elif chosen_tile == 4:

                    cost = "{:.2f}".format( tile_number* 290.00)
                    print ('\nThe cost is RM',cost,'\n')

            #The variables for calculation of the total cost for the single trnsaction
            COST = float(cost)
            total_cost += COST

            #The variables for calculation of the total number of tile used for the single transaction.
            TNUMBER = int(tile_number)
            total_tnumber += TNUMBER

            #The variable for the order of the wall
            w_count = w_count+1

            #The variable to end the loop
            num_wall = num_wall-1

        #The output of the cost and number of tile of the single transaction.
        print ('\nThe total cost for this single transaction is RM %.2f'%total_cost)
        print ('\nThe total box of tile used for this singe transaction is',total_tnumber,'\n')

    #The variables for calculation of the total cost for all trnsaction
    TOTAL_COST = float(total_cost)
    total_t_cost += TOTAL_COST

    #The variables for calculation of the total number of tile used for all transaction.
    T_TNUMBER = int(total_tnumber)
    total_t_tnumber += T_TNUMBER

    #The variable for the order of the transaction
    t_count=t_count+1

    #The variable to end the loop
    transaction_num = transaction_num-1

#The output of the cost and number of tile of all transaction.
print ('\nThe total transaction cost is RM %.2f'%total_t_cost)
print ('\nThe total box of tile used for transaction is',total_t_tnumber)


