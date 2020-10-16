text = "Ahmed@KSU.edu.sa Ali@imamu.edu.sa salem@KAU.edu.sa Bandar@ksu.edu.sa"

class count:
    domins = {}

    def get_domin(self, txt: str):
        print(txt)
        read = False
        domin = ""
        for i in txt:
            if i.upper(): i = i.lower()
            if i == "@": read = True
            if read: domin += i
            if i == " ":
                break
        return domin


    def counter(self, domin: str):
        if domin in self.domins:
            self.domins[domin] += 1
        else:
            self.domins[domin] = 1

    def __init__(self, txt: str):
        read = ""
        for i in txt:

            if not i == " ":
                read += i
            else:
                self.counter(self.get_domin(read))
                read = ""

            #print(read)
        self.counter(self.get_domin(read))


print(count(text).domins)

#it's took aroud 3h
