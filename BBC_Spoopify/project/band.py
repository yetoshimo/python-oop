from project.album import Album
# from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            _album_name = next(filter(lambda n: n.name == album_name, self.albums))
            if _album_name.published:
                return f"Album has been published. It cannot be removed."
            else:
                self.albums.remove(next(filter(lambda n: n.name == album_name, self.albums)))
                return f"Album {album_name} has been removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        _band_data = f"Band {self.name}\n"
        for s in self.albums:
            _band_data += f"{s.details()}\n"
        return _band_data


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
