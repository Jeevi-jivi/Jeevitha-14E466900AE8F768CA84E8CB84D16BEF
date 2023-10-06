class Player:

    def play(self):

        print("the player is playing cricket.")

# Define the batsman class,derived from player

class Batsman(Player):

    def play(self):

        print("the batsman is batting.")

  #Define the bowler class,derived from player

class Bowler(Player):

    def play(self):

        print("the bowler is bowling.")

  #create objects of Batsman and Bowler classes

batsman = Batsman()

bowler = Bowler()

# call the play() method for each object

batsman.play()

bowler.play()
