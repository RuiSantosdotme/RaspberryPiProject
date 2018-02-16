#Part 0 - Pick a fruit
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

print('Pick a fruit:')
print('strawberry, banana, or kiwi?')
color = input ('Enter the color of the fruit you chose: ')
if (color == 'red'):
    print('Your fruit is a strawberry.')
elif (color == 'yellow'):
    print('Your fruit is a banana.')
elif (color == 'green'):
    print('Your fruit is a kiwi.')
else:
    print('Invalid input.')
