class Students:

    def __init__(self, age, classname,name="student"):
        self.age = age
        self.classname = classname
        self.name = name

    def calcavgscore(self,score1:int ,score2:int ,score3:int):
        avgscore = (score1 + score2 + score3)/3
        return avgscore

FreakMama = Students(55, "Biden",[5,5,5])
EvilPapa = Students(66, "Russia")
SecretSquirrel = Students(103, "Ukraine")

print( "FreakMama: ", FreakMama.calcavgscore(56, 5, 56))
print( "EvilPapa: ", EvilPapa.calcavgscore(105, 5, 77))
print( "SecretSquirrel: ", SecretSquirrel.calcavgscore(20, 10, 70))





