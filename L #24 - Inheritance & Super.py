## Day 24: Inheritance and Super

## Concept: Inheritance and Super

# Creating a Parent Class
class Music:
    def __init__(self,band,genre):
        self.band = band
        self.genre = genre
    
    def info(self):
        print(f"{self.band} is my favorite band & they play {self.genre} music")

# Creating a Child Class
class Band(Music):
    def __init__(self,band,genre,origin):
        super().__init__(band,genre)
        self.origin = origin
    
    def bandInfo(self):
        print(f"{self.band} is a {self.origin} band which play {self.genre} music")
"""
super() simply refers to the parent class.
super().__init__(band,genre)
This is simply calling the constructor of the parent class, in our case Music. 
This is how we inherit all of the properties and methods in our Band child class.
"""

# Creating Objects
# instantiating parent class object
band1 = Music("The Beatles","rock")
band1.info()
# output: The Beatles is my favorite band & they play rock music

# instantiating child class object
band2 = Band("Lalon","folk","Bangladeshi")
# accessing parent class method
band2.info()
# output: Artcell is my favorite band & they play folk music

# accessing child class method
band2.bandInfo()
# output: Artcell is a Bangladeshi band which play folk music

    




