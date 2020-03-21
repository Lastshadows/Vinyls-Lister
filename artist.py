
class Artist:

    def __init__(self, artist_name, style):
        self.artist_name = artist_name
        self.vinyls = []
        self.style = style

    def addVinyl(self, vinyl_name):
        self.vinyls.append(vinyl_name)
        self.vinyls = sorted(self.vinyls)

    def nbOfAlbums(self):
        return str(len(self.vinyls))

    def nbOfAlbumsInt(self):
        return len(self.vinyls)
