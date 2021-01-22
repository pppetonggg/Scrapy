import string
import itertools


class genList():
    url = []

    def methodA(self):
        letters = list(string.ascii_lowercase + string.digits)
        com = itertools.combinations_with_replacement(letters, 5)
        for c in com:
            link = ''.join(c)
            self.url.append(link)
            # print(''.join(c))
            # print (link)
        return self.url