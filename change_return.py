from decimal import Decimal

coins = [1, .50, .20, .10, .05, .02, .01]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}


def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change
 
 
if __name__ == '__main__':
    while True:
        prompt = 'choose item: %s' % available_items
        chosen_item = raw_input(prompt)
        if chosen_item not in available_items:
            print "that item isn't available"
            continue
 
        amount = raw_input('enter amount in pounds:')
        cost = available_items[chosen_item]
        if amount < cost:
            print 'not enough money'
        else:
            change_to_return = float(amount) - cost
            coins = give_change(change_to_return)
            print "here's your change: %s" % coins
