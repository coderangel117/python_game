class User:

    def __init__(self, username: str, greatest_score: int = 0, great_score=None, nbfail: int = 0, nbwin: int = 0) -> None:
        if great_score is None:
            great_score = []
        self.username = username
        self.greatest_score = greatest_score
        self.great_score = great_score
        self.nbfail = nbfail
        self.nbwin = nbwin

    def tostring(self):
        return f" le user {self.username} possède {self.nbfail} défaites et {self.nbwin} victoires son meilleur score est de {self.greatest_score}"

    def getusername(self):
        return self.username

    def getgreatestscore(self):
        return self.greatest_score

    def getnbwin(self):
        return self.nbwin

    def getnbfail(self):
        return self.nbfail

    def add_win(self):
        self.nbwin += 1

    def add_fail(self):
        self.nbfail += 1
