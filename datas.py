class Data:

    def __init___(self, dd, mm, aaaa):
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa

    def formatada(self):
        print("{}/{}/{}".format(self.dd, self.mm, self.aaaa))