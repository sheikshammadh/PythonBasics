# mapped object
prices=[98,198,298,398,498,598]

def addplus(prices):
    return prices+1
map_data=map(addplus,prices)
print(list(map_data))
print(list(map(lambda prices:prices+1,prices)))
