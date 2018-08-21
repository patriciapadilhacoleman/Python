#alien_color = ["green","yellow","red"]

alien = {'color':'green', 'points' : 5}
alien['x-position'] = 0
alien['y-position'] = 25

print(alien['color'])
print(alien['points'])
alien['color'] = 'yellow'
del alien['points']
print(alien)
# if alien == "green":

# 	points = 5

# elif alien == "yellow":
# 	points = 7

# else :
# 	points = 10

# print("Your score is " + str(points) + " points!!!!")