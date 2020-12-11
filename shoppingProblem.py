##########################################################################################
# In A store, there are some kinds of items to sell. Each item has a price.

# However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

# You are given each item's price, a set of special offers, and the number of items to buy for each item. 

# The job is to output the lowest price you have to pay for exactly the items as given, where you could make optimal use of the special offers.

# Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

# You could use any of special offers as many times as you want.

# Example:
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation: 
# There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B. 
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

##################################################################################################

#  key = needs, value = min price for those needs
min_price_by_needs = {}
def shoppingOffers(price, special, needs):

    return getMinShoppingCost(price, special, needs)
    

def getMinShoppingCost(price, special, needs):
    
    needs_tuple = tuple(needs)
    if needs_tuple in min_price_by_needs:
        return min_price_by_needs[needs_tuple]

    # returns minimum cost of buying these items
    min_price = getRegularPriceForNeeds(price, needs)
    for offer in special:
        curr_needs = needs[:]
        
        # Try to apply the current offer. If possible, update the required number of items in clone
        if canApplyOffer(offer, curr_needs):
            curr_needs = applyOffer(offer, curr_needs)
            offer_price = offer[-1]
            min_price = min(min_price, offer_price + getMinShoppingCost(price, special, curr_needs))
        
    min_price_by_needs[needs_tuple] = min_price
    return min_price
        
def applyOffer(offer, curr_needs):  
    for i in range(len(curr_needs)):
        curr_needs[i] -= offer[i]
    return curr_needs


def canApplyOffer(offer, curr_needs):
    for i in range(len(curr_needs)):
        if offer[i] > curr_needs[i]:
            return False
    return True
    
    
def getRegularPriceForNeeds(price, needs):
    
    regular_price = 0
    for i, item in enumerate(price):
        
        regular_price += item * needs[i]
    return regular_price

print(shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))

print(shoppingOffers([1,1,1],[[1,1,0,0],[2,2,1,0]],[1,1,1]))