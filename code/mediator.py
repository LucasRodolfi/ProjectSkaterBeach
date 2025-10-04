class GameMediator:
    def __init__(self, player, obstacles, score):
        self.player = player
        self.obstacles = obstacles
        self.score = score

    def notify(self, event):
        if event == "collision":
            self.player.crash()