import Basic_Blackjack_Logic
import Create_Card

ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
TEN = '10'
ELEVEN = '11'
TWELVE = '12'
THIRTEEN = '13'
FOURTEEN = '14'
FIFTEEN = '15'
SIXTEEN = '16'
SEVENTEEN = '17'
ACE = 'A'
JACK = 'J'
QUEEN = 'Q'
KING = 'K'
HEARTS = 'H'
CLUBS = 'C'
SPADES = 'S'
DIAMONDS = 'D'

TWENTY_ONE = 21

count = 0

dealer_hand = []
player_hand = []
player_hands = []
class function():
     
    def dealer_starting_hand():
        
        VALID_DEALER_VALUE = False
        VALID_DEALER_SUIT = False
        # Check dealer's first card input
        while VALID_DEALER_VALUE == False:
            dealer_upcard_value = input("Enter dealer's first card's value: ")
            if(dealer_upcard_value != TWO and dealer_upcard_value != THREE and dealer_upcard_value!= FOUR and dealer_upcard_value!= FIVE and dealer_upcard_value!= SIX and dealer_upcard_value!= SEVEN and dealer_upcard_value != EIGHT and dealer_upcard_value != NINE and dealer_upcard_value != TEN and dealer_upcard_value != ACE and dealer_upcard_value != JACK and dealer_upcard_value != QUEEN and dealer_upcard_value != KING):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_DEALER_VALUE = True

        while VALID_DEALER_SUIT == False:
            dealer_upcard_suit = input("Enter dealer's first card's suit: ")
            if(dealer_upcard_suit != HEARTS and dealer_upcard_suit != CLUBS and dealer_upcard_suit != SPADES and dealer_upcard_suit!= DIAMONDS):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_DEALER_SUIT = True
       
        if(VALID_DEALER_VALUE == True and VALID_DEALER_SUIT == True):

            dealer_first_card = Create_Card.create_card(dealer_upcard_value, dealer_upcard_suit)
            dealer_hand.append(dealer_first_card)      
            return dealer_hand
    
        
    def player_starting_hand():
        
        VALID_PLAYER_VALUE_1 = False
        VALID_PLAYER_VALUE_2 = False
        VALID_PLAYER_SUIT_1 = False
        VALID_PLAYER_SUIT_2 = False
        # Check player's first card input
        while VALID_PLAYER_VALUE_1 == False:
            player_first_card_value = input("Enter player's first card's value: ")
            if(player_first_card_value != TWO and player_first_card_value != THREE and player_first_card_value != FOUR and player_first_card_value != FIVE and player_first_card_value != SIX and player_first_card_value != SEVEN and player_first_card_value != EIGHT and player_first_card_value != NINE and player_first_card_value != TEN and player_first_card_value != ACE and player_first_card_value != JACK and player_first_card_value != QUEEN and player_first_card_value != KING):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_PLAYER_VALUE_1 = True

        while VALID_PLAYER_SUIT_1 == False:
            player_first_card_suit = input("Enter player's first card's suit: ")
            if(player_first_card_suit != HEARTS and player_first_card_suit != CLUBS and player_first_card_suit != SPADES and  player_first_card_suit != DIAMONDS):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_PLAYER_SUIT_1 = True

        # Check player's second card input
        while VALID_PLAYER_VALUE_2 == False:
            player_second_card_value = input("Enter player's second card's value: ")
            if(player_second_card_value != TWO and player_second_card_value != THREE and player_second_card_value != FOUR and player_second_card_value != FIVE and player_second_card_value != SIX and player_second_card_value != SEVEN and player_second_card_value != EIGHT and player_second_card_value != NINE and player_second_card_value != TEN and player_second_card_value != ACE and player_second_card_value != JACK and player_second_card_value != QUEEN and player_second_card_value != KING):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_PLAYER_VALUE_2 = True

        while VALID_PLAYER_SUIT_2 == False:
            player_second_card_suit = input("Enter player's second card's suit: ")
            if(player_second_card_suit != HEARTS and player_second_card_suit != CLUBS and player_second_card_suit != SPADES and  player_second_card_suit != DIAMONDS):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_PLAYER_SUIT_2 = True
                
        if(VALID_PLAYER_VALUE_1 == True and VALID_PLAYER_VALUE_2 == True and VALID_PLAYER_SUIT_1 == True and VALID_PLAYER_SUIT_2 == True):

            player_first_card = Create_Card.create_card(player_first_card_value, player_first_card_suit)
            player_hand.append(player_first_card)      
        
            player_second_card = Create_Card.create_card(player_second_card_value, player_second_card_suit)
            player_hand.append(player_second_card)      
            return player_hand
    
    def calc_winner(dealer, player):
        
        dealer_sum = function.check_value(dealer)
        player_sum = function.check_value(player)
        #WOULD YOU LIKE TO CONTINUE?
        #ASK IF THEY WANT TO SAVE OR NOT TO CVS
        
        print(player_sum)
        if(player_sum <= TWENTY_ONE and dealer_sum <= TWENTY_ONE):
            if(player_sum > dealer_sum):
                
                print("PLAYER WINS!")
            
            if(player_sum < dealer_sum):
            
                print("DEALER WINS!")
        
            if(player_sum == dealer_sum):
                    
                print("PUSH!")
                
        if(player_sum <= TWENTY_ONE and dealer_sum > TWENTY_ONE):
            
            print("Player Wins!")         
        

    def check_value(hand):
        hand_value = sum(c.total for c in hand)

        if any(c.value == ACE for c in hand ) and hand_value <= int(ELEVEN):
            
            hand_value += int(TEN)
            
        return hand_value    

    def hit_function(dealer_hand, hand, split_check):
    
        VALID_VALUE = False
        VALID_SUIT = False
        count = 1
        print("HIT")
        while VALID_VALUE == False:
            hit_value = input("Enter player's next card's value: ")
            if(hit_value != TWO and hit_value != THREE and hit_value != FOUR and hit_value != FIVE and hit_value != SIX and hit_value != SEVEN and hit_value != EIGHT and hit_value != NINE and hit_value != TEN and hit_value != ACE and hit_value != JACK and hit_value != QUEEN and hit_value != KING):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_VALUE = True

        while VALID_SUIT == False:
            hit_suit = input("Enter player's next card's suit: ")
            if(hit_suit != HEARTS and hit_suit != CLUBS and hit_suit != SPADES and hit_suit != DIAMONDS):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_SUIT = True
                    
        if(VALID_VALUE == True and VALID_SUIT == True):
            
            new_card = Create_Card.create_card(hit_value, hit_suit)
            hand.append(new_card)      
            # DOUBLE NEEDS TO BE HIT IF SPLIT AND SeCONd CARD EXIST
            second_decision = Basic_Blackjack_Logic.logic_handler.get_decision(dealer_hand, hand, split_check, count) 
            player_result = Basic_Blackjack_Logic.logic_handler.decision(second_decision[0], second_decision[1], second_decision[2], second_decision[3], second_decision[4], second_decision[5], second_decision[6], second_decision[7], second_decision[8], second_decision[9], second_decision[10], second_decision[11], dealer_hand, hand) 
            
            return dealer_hand, hand, count
        
        
    def double_input_function(dealer_hand, hand):
        
        VALID_VALUE = False
        VALID_SUIT = False
        
        while VALID_VALUE == False:
            hit_value = input("Enter player's next card's value: ")
            if(hit_value != TWO and hit_value != THREE and hit_value != FOUR and hit_value != FIVE and hit_value != SIX and hit_value != SEVEN and hit_value != EIGHT and hit_value != NINE and hit_value != TEN and hit_value != ACE and hit_value != JACK and hit_value != QUEEN and hit_value != KING):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_VALUE = True

        while VALID_SUIT == False:
            hit_suit = input("Enter player's next card's suit: ")
            if(hit_suit != HEARTS and hit_suit != CLUBS and hit_suit != SPADES and hit_suit != DIAMONDS):
                print("*********************\n*** INVALID INPUT ***\n*********************")
            else:
                VALID_SUIT = True
                    
        if(VALID_VALUE == True and VALID_SUIT == True):

            new_card = Create_Card.create_card(hit_value, hit_suit)
            hand.append(new_card)      

            return dealer_hand, hand


    def stand_function(dealer_hand, player_hand, toggle):

        VALID_VALUE = False
        VALID_VALUE = False
        VALID_SUIT = False
        DEALER_HIT = toggle
        
        while(DEALER_HIT == True):
            while VALID_VALUE == False:
                dealer_hit_value = input("Enter dealer's next card's value: ")
                if(dealer_hit_value != TWO and dealer_hit_value != THREE and dealer_hit_value != FOUR and dealer_hit_value != FIVE and dealer_hit_value != SIX and dealer_hit_value != SEVEN and dealer_hit_value != EIGHT and dealer_hit_value != NINE and dealer_hit_value != TEN and dealer_hit_value != ACE and dealer_hit_value != JACK and dealer_hit_value != QUEEN and dealer_hit_value != KING):
                    print("*********************\n*** INVALID INPUT ***\n*********************")
                else:
                    VALID_VALUE = True

            while VALID_SUIT == False:
                dealer_hit_suit = input("Enter dealer's next card's suit: ")
                if(dealer_hit_suit != HEARTS and dealer_hit_suit != CLUBS and dealer_hit_suit != SPADES and dealer_hit_suit != DIAMONDS):
                    print("*********************\n*** INVALID INPUT ***\n*********************")
                else:
                    VALID_SUIT = True
                        
            if(VALID_VALUE == True and VALID_SUIT == True):

                dealer_new_card = Create_Card.create_card(dealer_hit_value, dealer_hit_suit)
                dealer_hand.append(dealer_new_card)
                
                dealer_sum = function.check_value(dealer_hand)
                
                if( dealer_sum > TWENTY_ONE):
                    
                    #calculate who wins based on the hands that are left
                    print("DEALER BUSTS!")
                    function.calc_winner(dealer_hand, player_hand)
                    DEALER_HIT = False
                else:    
                    if (dealer_sum <= int(SIXTEEN)):
                        
                        VALID_VALUE = False
                        VALID_SUIT = False
                        
                    if (dealer_sum >= int(SEVENTEEN)):
                        
                        DEALER_HIT = False

        

               
        # compare hands         
    def split_function(player_hand):
        w, h = int(TWO), int(ONE)
        
        split_hand = [[0 for y in range(h)] for x in range(w)]
        card_1 = player_hand[0]
        card_2 = player_hand[1]
        player_hand_1 = [card_1]
        player_hand_2 = [card_2]
        split_hand[0][0] = player_hand_1
        split_hand[1][0] = player_hand_2
        
        print("SPLIT")
        
        return split_hand
    
    def double_function(dealer, player, toggle):
        
        print("DOUBLE")
        DEALER_HIT_TOGGLE = toggle
        
        hands = function.double_input_function(dealer, player)
        dealer_hand = hands[0]
        player_hand = hands[1]
    
        player_hands.append(player_hand)
        #GET DEALER AND PLAYER HAND
        function.stand_function(dealer_hand, player_hands[0], DEALER_HIT_TOGGLE)   
        
        if(len(player_hands) == int(TWO)):
            function.calc_winner(dealer_hand, player_hands[0])
            function.calc_winner(dealer_hand, player_hands[1])
            #ADD MORE TO the calc_winner conditions
                
    def bust_function(hand):
       # hand_sum = function.check_value(hand)
        #count = int(ONE)
       
        print("BUST")
       # for c in hand:
            
          #  if(hand_sum > TWENTY_ONE):
          #      print("Dealer wins against hand " + str(count) + "!")
          #      count += int(ONE)
          #  else: count += int(ONE)    
            
    def black_jack_function():

        print("BLACKJACK")
       