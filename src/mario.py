class Mario:
    def __init__(self) -> None:
        self.name = 'Mario'
        self.px = 0
        self.py = 0
        self.sprite_walk = '01'
        self.sprite_jump = '02'
        self.sprite_power = '03'
        self.sprite_run = '04'

    def walking(self):
        self.px += 5
        self.px -= 5     
    
    def junping(self):
        self.py += 25
        self.py -= 25
    
    def power(self):
        pass