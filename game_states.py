from pathlib import Path 
import json

class GameSate:
    def __init__(self,ai_game):
        self.settings=ai_game.settings
        path=Path("high_score.json")
        A=json.loads(path.read_text())
        self.high_score=A["high_score"]
        self.reset_stats()#初始化统计信息
    
    def reset_stats(self):
        self.ship_left=self.settings.ship_limit
        self.score=0

