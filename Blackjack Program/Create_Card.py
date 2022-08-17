# Creates a card object
#https://stackoverflow.com/questions/46088655/manipulating-the-value-of-ace-in-blackjack-python
class create_card():
    valuetable = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    valuetable.update({str(i): i for i in range(2, 10)})
    
    def __init__(self, value, suit):
        
        self.value = value
        self.suit = suit
        self.total = self.valuetable[self.value]
        
       
 
        
    
    
       