def padel_court_cost(court_type):
    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
    else :
        return 0 
def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200
    else :
        return     
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    else:
        return 0
    
def padel_game_cost():
    court_type = input('court type : ')
    racket_brand = input( 'racket brand : ')
    ball_boxes = int(input('number of padel boxes : '))
    courtcost = padel_court_cost(court_type)
    racketcost = rackets_cost(racket_brand)
    ballscost = padel_balls_cost(ball_boxes)
    print(f'padel court cost is {padel_court_cost(court_type)}')
    print(f'racket cost is {rackets_cost(racket_brand)}')
    print(f"padel balls cost is {padel_balls_cost(ball_boxes)} ")
    fullgamecost = courtcost + racketcost + ballscost 
    return fullgamecost
 
print(f'padel game cost is {padel_game_cost()}')
