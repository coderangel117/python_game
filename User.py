class User:

    def __init__(self, username: str, greatest_score=None, nbfail: int = 0, nbwin: int = 0) -> None:
        if greatest_score is None:
            greatest_score = []
        self.username = username
        self.greatest_score = greatest_score
        self.nbfail = nbfail
        self.nbwin = nbwin

    def tostring(self):
        return f" User {self.username} has {self.nbfail} fails et {self.nbwin} wons"

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
