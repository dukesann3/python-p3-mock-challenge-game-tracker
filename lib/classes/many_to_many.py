class Game:

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, 'title'):
            if isinstance(title, str) and len(title) > 0:
                self._title = title
            else:
                #raise ValueError("Title must be a String")
                print("Title must be a String")

    def results(self):
        results = [result for result in Result.all if result.game == self]
        return results

    def players(self):
        players = [result.player for result in Result.all if result.game == self]
        unique_players = []
        for player in players:
            if player not in unique_players:
                unique_players.append(player)
        
        return unique_players

    def average_score(self, player):
        results = [result.score for result in Result.all if result.player == player]
        average_score = sum(results) / len(results)
        return average_score

class Player:
    
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            #raise ValueError("Username must be a string and between 2 to 16 characters")
            print("Username must be a string and between 2 to 16 characters")

    def results(self):
        results = [result for result in Result.all if result.player == self]
        return results

    def games_played(self):
        games = [result.game for result in Result.all if result.player == self]
        unique_games = []
        for game in games:
            if game not in unique_games:
                unique_games.append(game)
        return unique_games

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        games = [result.game for result in Result.all if result.player == self]
        return games.count(game)


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            #raise ValueError("Player must be a Player object")
            print("Player must be a Player object")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            #raise ValueError("Game must be a Game object")
            print("Game must be a Game object")

    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not hasattr(self, 'score'):
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score
            else:
                #raise ValueError("Score must be an integer and a value in between 1 and 5000")
                print("Score must be an integer and a value in between 1 and 5000")


