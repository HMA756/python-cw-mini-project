def padel_court_cost (court_type):
     if court_type == ('Indoor'):
          return 30
     elif court_type == ('outdoor'): 
          return 20
     else:
          print('Error')

def rackets_cost (racket_brand):
     if rackets_cost == ('bullpadel'):
          return 100
     elif rackets_cost ==('nox'):
          return 140
     elif rackets_cost == ('siux'):
          return 200
     else:
          print('error')
     
     
def padel_balls_cost (ball_boxes):
     if padel_balls_cost == 1:
          return 2
     elif padel_balls_cost == 2:
          return 3.5
     elif padel_balls_cost == 3:
          return 5 
     else:
          print('you cant get more than three boxes in one purchase')

def padel_game_cost():
     court = input ('would you like the court indoors or outdoors?')
     brand = input ('select a padel brand between bullpadel, nox, suix')
     balls = int (input('would you like 1,2 or 3 boxes of balls'))
     result = padel_court_cost (court) + rackets_cost (brand) + padel_balls_cost (balls)

     print(padel_game_cost)
