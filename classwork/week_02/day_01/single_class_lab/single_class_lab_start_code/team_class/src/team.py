class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, name):
        return self.players.append(name)

    def has_player(self, player_name):
        for player in self.players:
            if player_name == player:
                return True
        else:
            return False

    def play_game(self, result):
        if result == True: 
            self.points += 3
        elif result == False:
            self.points = self.points

    
       
        
                        