class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        _song_data = f"{self.name} - {self.length}"
        return _song_data
