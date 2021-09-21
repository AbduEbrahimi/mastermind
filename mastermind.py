import random

"""Mastermind game in the terminal
The computer has seven colors and selects five without duplication.
Now you have to guess these colors in 12 steps.
For each color that you choose correctly and in the right place,
you get a white bead, and for each color that was there but its place was incorrect,
you get a black bead.
At the end you will see the score.
"""

def cpu_choise():
    """This function randomly selects five of the seven
    colors and returns them as a list."""
    all_color = ("green","red","blue","pink","yellow","orange","gray")
    chois_color = random.sample(all_color,5)    
    return chois_color

def player_choise():
    """Enter five colors that may be correct.
    A comma should be used between each color and
    there should be no space. Example:
    yellow,red,blue,green,pink
    If you use only q, you will be out of the game."""
    global dour
    your_chois = input(str(dour)+":")
    if your_chois == "q":
        quit()
    else:    
        your_list = your_chois.split(',')    
        return your_list

def check(cpu,you):
    """This function requires two arguments:
    The colors you have to guess and the main colors that were chosen.
    Compares them. If the name of the color and its place are correct,
    it adds the point of correctness of the color and its place.
    If the name of the color is correct but the place is wrong,
    the point is added to the wrong place.
    At the end, the two points return.
    If you select less or more than five colors, you will receive an error."""
    global jay_dorost,jay_eshtebah,score
    if len(you) == 5:
        for x in range(0,5):
            if you[x] in cpu:
                if you[x] == cpu[x]:
                    jay_dorost += 1
                else:
                    jay_eshtebah += 1
        return jay_dorost,jay_eshtebah
    else:
        print("Difficulty receiving from input.")
        return None        

jay_dorost = 0
jay_eshtebah = 0
score = 10
dour = 12 
sharp = "#"
def run():
    """Selects a list of computer colors and compares them with
    our colors in terms of location and selection, returns their points.
    Up to twelve rounds are allowed to enter colors,
    and if all colors and their place is not equal, the game ends with a message."""
    global score,dour,jay_dorost,jay_eshtebah
    print("Welcome to Mastermind\nVersion: 0.9.7")
    print("Choose five of these colors: green, red, blue, pink, yellow, orange, gray")
    print("or enter q to exit")
    print("--------------------------------------------------------------------------")
    _cpu = cpu_choise()
    while True:
        if dour == 0 :
            print("! game is over !")
            print("Right color and place: ",_cpu)
            break
        else:
            _player = player_choise()
            _check = check(_cpu,_player)
            if _check != None:
                if _check[0] == 5:
                    score *= dour
                    print("yeahhh you win your score ",score)
                    break
                else:
                    print(sharp*40)
                    print("white key pegs = ",jay_dorost," , black key pegs = ",jay_eshtebah)
                    print(sharp*40)
                    jay_dorost = 0
                    jay_eshtebah = 0
                    dour -= 1
            else:
                continue

run()