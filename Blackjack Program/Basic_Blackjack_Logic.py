import Functions
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
ELEVEN = 11
TWELVE = 12
THIRTEEN = 13
FOURTEEN = 14
FIFTEEN = 15
SIXTEEN = 16
SEVENTEEN = 17
EIGHTEEN = 18
NINETEEN = 19
TWENTY = 20
TWENTY_ONE = 21

ACE = 'A'
JACK = 'J'
QUEEN = 'Q'
KING = 'K'

HEARTS = 'H'
CLUBS = 'C'
SPADES = 'S'
DIAMONDS = 'D'

# Creates a card object for the specific value and suit

# Deciding on the best choice of basic Blackjack

# After hitting for the first time could be another ace


class logic_handler:
    
    def get_decision(dealer, player, split_check, count):

        HIT = False
        STAND = False
        DOUBLE = False
        SPLIT = False
        DOUBLE_STAND = False
        DOUBLE_SPLIT = False
        BLACK_JACK = False
        DEALER_BLACK_JACK = False
        BUST = False
        PUSH = False
        DEALER_HIT = False
        black_jack = 'N'
        dealer_sum = Functions.function.check_value(dealer)
        player_sum = Functions.function.check_value(player)
        #FIX FOR SPLITTING: REPEATS
        if any(c.value == ACE for c in dealer):

            if(count == 0 and len(player) == TWO):    
                
                black_jack = input("Does dealer have BJ? (Y/N)?")
                
            count += 1

            if black_jack == 'Y' and player_sum != TWENTY_ONE:

                DEALER_BLACK_JACK = True

                return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

            elif black_jack == 'Y' and player_sum == TWENTY_ONE:

                PUSH = True
                print("PUSH!")

            else:

                if(player_sum == TWENTY_ONE and len(player) == TWO and black_jack == 'N'):

                    BLACK_JACK = True

                    return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

                if any(c.value == ACE for c in player):

                    # Soft Totals
                    # if statement to check for two cards for splits. berfore every player[]
                    if(len(player) == TWO):
                        if player[0].value == ACE and player[1].value == ACE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False
                            DEALER_HIT = False

                            return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

                    if player_sum == TWENTY_ONE:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False
                        BLACK_JACK = True
                        DEALER_HIT = True

                    if player_sum >= TWENTY and player_sum < TWENTY_ONE:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DEALER_HIT = True

                    if player_sum == NINETEEN:

                        if dealer_sum == SIX:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = True

                        else:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DEALER_HIT = True

                    if player_sum == EIGHTEEN:

                        if dealer_sum <= SIX and dealer_sum >= TWO:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = True

                        if dealer_sum == SEVEN or dealer_sum == EIGHT:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DEALER_HIT = True

                        if dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == SEVENTEEN:

                        if dealer_sum == TWO or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum <= SIX and dealer_sum >= THREE:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False
                                DEALER_HIT = True

                    if player_sum == SIXTEEN:

                        if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum <= SIX and dealer_sum >= FOUR:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                    if player_sum == FIFTEEN:

                        if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum <= SIX and dealer_sum >= FOUR:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                    if player_sum == FOURTEEN:

                        if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum == SIX or dealer_sum == FIVE:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                    if player_sum == THIRTEEN:

                        if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum == SIX or dealer_sum == FIVE:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                    if(len(player) == TWO or len(player) == ONE):
                        if player_sum == ELEVEN:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                    return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

                else:

                    if player_sum == TWENTY_ONE:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False
                        BLACK_JACK = True

                    if player_sum >= SEVENTEEN and player_sum <= TWENTY:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if player_sum <= EIGHT:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if player_sum == SIXTEEN:

                        if dealer_sum <= SIX and dealer_sum >= TWO:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == FIFTEEN:

                        if dealer_sum <= SIX and dealer_sum >= TWO:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == FOURTEEN:

                        if dealer_sum <= SIX and dealer_sum >= TWO:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == THIRTEEN:

                        if dealer_sum <= SIX and dealer_sum >= TWO:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == TWELVE:

                        if dealer_sum == TWO or dealer_sum == THREE:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= SIX and dealer_sum >= FOUR:

                            HIT = False
                            STAND = True
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if(len(player) == TWO or len(player) == ONE):
                        if player_sum == ELEVEN:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                    if player_sum == TEN:

                        if(len(player) == TWO):
                            if dealer_sum <= NINE and dealer_sum >= TWO:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                        if dealer_sum == TEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum == NINE:

                        if dealer_sum == TWO:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                        if(len(player) == TWO):
                            if dealer_sum <= SIX and dealer_sum >= THREE:

                                HIT = False
                                STAND = False
                                DOUBLE = True
                                DOUBLE_STAND = False

                        if dealer_sum <= TEN and dealer_sum >= SEVEN:

                            HIT = True
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False

                    if player_sum / TWO == TEN:

                        SPLIT = False

                    if(len(player) == TWO):
                        if player[0].total == NINE and player[1].total == NINE:

                            if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == FIVE or dealer_sum == SIX or dealer_sum == EIGHT or dealer_sum == NINE:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = False
                                SPLIT = True
                                split_check = True
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player[0].total == EIGHT and player[1].total == EIGHT:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False

                        if player[0].total == SEVEN and player[1].total == SEVEN:

                            if dealer_sum <= SEVEN and dealer_sum >= TWO:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = False
                                SPLIT = True
                                split_check = True
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player[0].total == SIX and player[1].total == SIX:

                            if dealer_sum == TWO:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = True
                                SPLIT = False
                                BLACK_JACK = False

                            elif dealer_sum <= SIX and dealer_sum >= THREE:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = False
                                SPLIT = True
                                split_check = True
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player[0].total == FIVE and player[1].total == FIVE:

                            SPLIT = False

                        if player[0].total == FOUR and player[1].total == FOUR:

                            if dealer_sum == FIVE or dealer_sum == SIX:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = True
                                SPLIT = False
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player[0].total == THREE and player[1].total == THREE:

                            if dealer_sum == TWO or dealer_sum == THREE:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = True
                                SPLIT = False
                                BLACK_JACK = False

                            elif dealer_sum <= SEVEN and dealer_sum >= FOUR:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = False
                                SPLIT = True
                                split_check = True
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player[0].total == TWO and player[1].total == TWO:

                            if dealer_sum == TWO or dealer_sum == THREE:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = True
                                SPLIT = False
                                BLACK_JACK = False

                            elif dealer_sum <= SEVEN and dealer_sum >= FOUR:

                                HIT = False
                                STAND = False
                                DOUBLE = False
                                DOUBLE_STAND = False
                                DOUBLE_SPLIT = False
                                SPLIT = True
                                split_check = True
                                BLACK_JACK = False

                            else:

                                SPLIT = False

                        if player_sum > TWENTY_ONE or dealer_sum > TWENTY_ONE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = False
                            BLACK_JACK = False
                            BUST = True

                    return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

        else:

            if(player_sum == TWENTY_ONE and len(player) == TWO):

                BLACK_JACK = True

                return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

            if any(c.value == ACE for c in player):

                # Soft Totals
                # if statement to check for two cards for splits. berfore every player[]
                if(len(player) == TWO):
                    if player[0].value == ACE and player[1].value == ACE:

                        HIT = False
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DOUBLE_SPLIT = False
                        SPLIT = True
                        split_check = True
                        BLACK_JACK = False
                        DEALER_HIT = False

                        return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

                if player_sum > TWENTY:

                    BUST = True

                if player_sum == TWENTY_ONE:

                    HIT = False
                    STAND = True
                    DOUBLE = False
                    DOUBLE_STAND = False
                    BLACK_JACK = True
                    DEALER_HIT = True

                if player_sum >= TWENTY and player_sum < TWENTY_ONE:

                    HIT = False
                    STAND = True
                    DOUBLE = False
                    DOUBLE_STAND = False
                    DEALER_HIT = True

                if player_sum == NINETEEN:

                    if dealer_sum == SIX:

                        HIT = False
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = True

                    else:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DEALER_HIT = True

                if player_sum == EIGHTEEN:

                    if dealer_sum <= SIX and dealer_sum >= TWO:

                        HIT = False
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = True

                    if dealer_sum == SEVEN or dealer_sum == EIGHT:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DEALER_HIT = True

                    if dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == SEVENTEEN:

                    if dealer_sum == TWO or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum <= SIX and dealer_sum >= THREE:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False
                            DEALER_HIT = True

                if player_sum == SIXTEEN:

                    if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum <= SIX and dealer_sum >= FOUR:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                if player_sum == FIFTEEN:

                    if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum <= SIX and dealer_sum >= FOUR:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                if player_sum == FOURTEEN:

                    if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum == SIX or dealer_sum == FIVE:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                if player_sum == THIRTEEN:

                    if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == SEVEN or dealer_sum == EIGHT or dealer_sum == NINE or dealer_sum == TEN or dealer_sum == ELEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum == SIX or dealer_sum == FIVE:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                if(len(player) == TWO or len(player) == ONE):
                    if player_sum == ELEVEN:

                        HIT = False
                        STAND = False
                        DOUBLE = True
                        DOUBLE_STAND = False

                return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

            else:

                if player_sum == TWENTY_ONE:

                    HIT = False
                    STAND = True
                    DOUBLE = False
                    DOUBLE_STAND = False
                    BLACK_JACK = True

                if player_sum >= SEVENTEEN and player_sum <= TWENTY:

                    HIT = False
                    STAND = True
                    DOUBLE = False
                    DOUBLE_STAND = False

                if player_sum <= EIGHT:

                    HIT = True
                    STAND = False
                    DOUBLE = False
                    DOUBLE_STAND = False

                if player_sum == SIXTEEN:

                    if dealer_sum <= SIX and dealer_sum >= TWO:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == FIFTEEN:

                    if dealer_sum <= SIX and dealer_sum >= TWO:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == FOURTEEN:

                    if dealer_sum <= SIX and dealer_sum >= TWO:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == THIRTEEN:

                    if dealer_sum <= SIX and dealer_sum >= TWO:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == TWELVE:

                    if dealer_sum == TWO or dealer_sum == THREE:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= SIX and dealer_sum >= FOUR:

                        HIT = False
                        STAND = True
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if(len(player) == TWO or len(player) == ONE):
                    if player_sum == ELEVEN:

                        HIT = False
                        STAND = False
                        DOUBLE = True
                        DOUBLE_STAND = False

                if player_sum == TEN:

                    if(len(player) == TWO):
                        if dealer_sum <= NINE and dealer_sum >= TWO:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                    if dealer_sum == TEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum == NINE:

                    if dealer_sum == TWO:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                    if(len(player) == TWO):
                        if dealer_sum <= SIX and dealer_sum >= THREE:

                            HIT = False
                            STAND = False
                            DOUBLE = True
                            DOUBLE_STAND = False

                    if dealer_sum <= TEN and dealer_sum >= SEVEN:

                        HIT = True
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False

                if player_sum / TWO == TEN:

                    SPLIT = False

                if(len(player) == TWO):
                    if player[0].total == NINE and player[1].total == NINE:

                        if dealer_sum == TWO or dealer_sum == THREE or dealer_sum == FOUR or dealer_sum == FIVE or dealer_sum == SIX or dealer_sum == EIGHT or dealer_sum == NINE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player[0].total == EIGHT and player[1].total == EIGHT:

                        HIT = False
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DOUBLE_SPLIT = False
                        SPLIT = True
                        split_check = True
                        BLACK_JACK = False

                    if player[0].total == SEVEN and player[1].total == SEVEN:

                        if dealer_sum <= SEVEN and dealer_sum >= TWO:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player[0].total == SIX and player[1].total == SIX:

                        if dealer_sum == TWO:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = True
                            SPLIT = False
                            BLACK_JACK = False

                        elif dealer_sum <= SIX and dealer_sum >= THREE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player[0].total == FIVE and player[1].total == FIVE:

                        SPLIT = False

                    if player[0].total == FOUR and player[1].total == FOUR:

                        if dealer_sum == FIVE or dealer_sum == SIX:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = True
                            SPLIT = False
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player[0].total == THREE and player[1].total == THREE:

                        if dealer_sum == TWO or dealer_sum == THREE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = True
                            SPLIT = False
                            BLACK_JACK = False

                        elif dealer_sum <= SEVEN and dealer_sum >= FOUR:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            split_check = True
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player[0].total == TWO and player[1].total == TWO:

                        if dealer_sum == TWO or dealer_sum == THREE:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = True
                            SPLIT = False
                            BLACK_JACK = False

                        elif dealer_sum <= SEVEN and dealer_sum >= FOUR:

                            HIT = False
                            STAND = False
                            DOUBLE = False
                            DOUBLE_STAND = False
                            DOUBLE_SPLIT = False
                            SPLIT = True
                            split_check = True
                            BLACK_JACK = False

                        else:

                            SPLIT = False

                    if player_sum > TWENTY_ONE or dealer_sum > TWENTY_ONE:

                        HIT = False
                        STAND = False
                        DOUBLE = False
                        DOUBLE_STAND = False
                        DOUBLE_SPLIT = False
                        SPLIT = False
                        BLACK_JACK = False
                        BUST = True

                return HIT, STAND, DOUBLE, DOUBLE_STAND, DOUBLE_SPLIT, SPLIT, split_check, BLACK_JACK, DEALER_BLACK_JACK, BUST, PUSH, DEALER_HIT

    # Add the printing decision of what to do

    # Second Round

    def dealer_logic(hand):

        hand_value = Functions.function.check_value(hand)

       # while(hand_value <= )
        # hit until 17
        # return end value then check winners?
        # bust returns value to make player win or still maybe lose
        print(hand)

    def decision(hit, stand, double, double_stand, double_split, split, split_check, blackjack, dealer_blackjack, bust, push, dealer_hit, dealer_hand, player_hand):

        # "DAS" = Double After Split
        # "DOUBLE STAND" = Double if allowed if not Stand

        DOUBLE_HIT_TOGGLE = True
        DOUBLE_STAND_TOGGLE = True
        DAS_TOGGLE = True
        DEALER_HIT_TOGGLE = dealer_hit

        print(hit, stand, double, double_stand, double_split,
              split, split_check, blackjack, dealer_blackjack, bust, push)

        print(len(player_hand))
        if(split_check == True and len(player_hand) >= 2):

            if(bust == True):

                Functions.function.bust_function(player_hand)

            else:

                if(double == True):
                    print("HIT?")
                    double = False
                    hit = True

                    if(hit == True):

                        Functions.function.hit_function(
                            dealer_hand, player_hand, split_check)

                    if(stand == True):
                        DEALER_HIT_TOGGLE = True
                        Functions.function.stand_function(
                            dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                    if(double == True or double_stand == True or double_split == True):

                        if(double_stand == True and DOUBLE_STAND_TOGGLE == True):

                            Functions.function.double_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        elif(double_stand == True and DOUBLE_STAND_TOGGLE == False):

                            DEALER_HIT_TOGGLE = True
                            Functions.function.stand_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        if(double_split == True and DAS_TOGGLE == True):
                            # ADD DOUBLING FOR BOTH HANDS
                            both_hands = Functions.function.split_function(
                                player_hand)
                            Functions.function.double_function(
                                both_hands)  # FIX

                        if(double == True and DOUBLE_HIT_TOGGLE == True):

                            Functions.function.double_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        elif(double == True and DOUBLE_HIT_TOGGLE == False):

                            Functions.function.hit_function(
                                dealer_hand, player_hand, split_check)
                    # CHECK SPLITTING NUMBERS OTHER THAN A/11
                    if(split == True):
                        DEALER_HIT_TOGGLE = False
                        split_hand = Functions.function.split_function(
                            player_hand)
                        count = ONE
                        for hands in split_hand:

                            hands_len = len(split_hand)

                            for hand in hands:

                                if(hands_len == count):

                                    DEALER_HIT_TOGGLE = True

                                decision = logic_handler.get_decision(
                                    dealer_hand, hand, split_check, count)

                                player_result = logic_handler.decision(decision[0], decision[1], decision[2], decision[3], decision[4], decision[
                                                                       5], decision[6], decision[7], decision[8], decision[9], decision[10], DEALER_HIT_TOGGLE, dealer_hand, hand)
                        count += 1        
#FIGURE OUT COUNT & WHY ITS NOT GOING TO DOUBLE why  double 8 to 2
                    if(blackjack == True):

                        Functions.function.black_jack_function()

                else:

                    if(hit == True):

                        Functions.function.hit_function(
                            dealer_hand, player_hand, split_check)

                    if(stand == True):
                        DEALER_HIT_TOGGLE = True
                        Functions.function.stand_function(
                            dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                    if(double == True or double_stand == True or double_split == True):

                        if(double_stand == True and DOUBLE_STAND_TOGGLE == True):

                            Functions.function.double_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        elif(double_stand == True and DOUBLE_STAND_TOGGLE == False):

                            DEALER_HIT_TOGGLE = True
                            Functions.function.stand_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        if(double_split == True and DAS_TOGGLE == True):
                            # ADD DOUBLING FOR BOTH HANDS
                            both_hands = Functions.function.split_function(
                                player_hand)
                            Functions.function.double_function(
                                both_hands)  # FIX

                        if(double == True and DOUBLE_HIT_TOGGLE == True):

                            Functions.function.double_function(
                                dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                        elif(double == True and DOUBLE_HIT_TOGGLE == False):

                            Functions.function.hit_function(
                                dealer_hand, player_hand, split_check)
                    # CHECK SPLITTING NUMBERS OTHER THAN A/11
                    if(split == True):
                        DEALER_HIT_TOGGLE = False
                        split_hand = Functions.function.split_function(
                            player_hand)
                        count = ONE
                        for hands in split_hand:

                            hands_len = len(split_hand)

                            for hand in hands:

                                if(hands_len == count):

                                    DEALER_HIT_TOGGLE = True

                                decision = logic_handler.get_decision(
                                    dealer_hand, hand, split_check, count)

                                player_result = logic_handler.decision(decision[0], decision[1], decision[2], decision[3], decision[4], decision[
                                                                       5], decision[6], decision[7], decision[8], decision[9], decision[10], DEALER_HIT_TOGGLE, dealer_hand, hand)
                        count += 1
                    if(blackjack == True):

                        Functions.function.black_jack_function()
        else:
            print("hello")
            if(bust == True):

                Functions.function.bust_function(player_hand)
#DONT ALLOW FOR DOUBLE SPLIT
            else:

                if(hit == True):

                    Functions.function.hit_function(dealer_hand, player_hand, split_check)

                if(stand == True):
                    DEALER_HIT_TOGGLE = True
                    Functions.function.stand_function(
                        dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                if(double == True or double_stand == True or double_split == True):

                    if(double_stand == True and DOUBLE_STAND_TOGGLE == True):

                        Functions.function.double_function(
                            dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                    elif(double_stand == True and DOUBLE_STAND_TOGGLE == False):

                        DEALER_HIT_TOGGLE = True
                        Functions.function.stand_function(
                            dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                    if(double_split == True and DAS_TOGGLE == True):
                        # ADD DOUBLING FOR BOTH HANDS
                        both_hands = Functions.function.split_function(
                            player_hand)
                        Functions.function.double_function(both_hands)  # FIX

                    if(double == True and DOUBLE_HIT_TOGGLE == True):

                        Functions.function.double_function(
                            dealer_hand, player_hand, DEALER_HIT_TOGGLE)

                    elif(double == True and DOUBLE_HIT_TOGGLE == False):

                        Functions.function.hit_function(
                            dealer_hand, player_hand)
                  # CHECK SPLITTING NUMBERS OTHER THAN A/11
                if(split == True):
                    DEALER_HIT_TOGGLE = False
                    split_hand = Functions.function.split_function(player_hand)
                    count = ONE
                    for hands in split_hand:

                        hands_len = len(split_hand)

                        for hand in hands:

                            if(hands_len == count):

                                DEALER_HIT_TOGGLE = True

                            decision = logic_handler.get_decision(
                                dealer_hand, hand, split_check, count)

                            player_result = logic_handler.decision(decision[0], decision[1], decision[2], decision[3], decision[4], decision[
                                                                   5], decision[6], decision[7], decision[8], decision[9], decision[10], DEALER_HIT_TOGGLE, dealer_hand, hand)
                    count += 1
                if(blackjack == True):

                    Functions.function.black_jack_function()
