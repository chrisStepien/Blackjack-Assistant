# https://www.codegrepper.com/code-examples/python/two+dimensional+array+python+w3
# https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
import Functions
import Basic_Blackjack_Logic

ACE = 'A'
SPLIT_CHECK = False
count = 0


# Use dealer and player hand to decide basic blackjack
# Card counting
# History to excel
# Sidebet tracking

#DAS button to toggle 

# Initial DEAL

dealer_hand = Functions.function.dealer_starting_hand()
player_hand = Functions.function.player_starting_hand()

# Decide on Basic Blackjack Rules
#if(dealer_hand == ACE):

    

#else:
    
decision = Basic_Blackjack_Logic.logic_handler.get_decision(dealer_hand, player_hand, SPLIT_CHECK, count)


player_result = Basic_Blackjack_Logic.logic_handler.decision(decision[0], decision[1], decision[2], decision[3], decision[4], decision[5], decision[6], decision[7], decision[8], decision[9], decision[10], decision[11], dealer_hand, player_hand)

    
# if bust then stop if not keep going but need to pick card first (might want to remove bust and put it in another function)



#Loop for hit, split, double ,etc



