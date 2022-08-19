import random


class Hat:

    # initiating hat object, takes in any number of arguments and returns a list of them
    def __init__(self, **kwargs):
        self.contents = kwargs
        contentslist = []
        countv = 0
        for (k, v) in self.contents.items():
            while countv < v:
                contentslist.append(k)
                countv += 1
            countv = 0
        self.contents = contentslist

    # following drawn function used in the experiment function to return a random sample of balls
    def drawn(self, num):
        if num <= len(self.contents):
            return random.sample(self.contents, num)
        else:
            return self.contents

    # draw function draws num of balls at random and returns the random draw, modifying the contents list to take into account
    # the balls drawn
    def draw(self, numz):
        if numz <= len(self.contents):
            randomz = random.sample(self.contents, numz)
            for x in randomz:
                if x in self.contents:
                    self.contents.remove(x)
                else:
                    continue
            return randomz
        else:
            return self.contents


# experiment function carries out simulations to determine the chances of finding expected_balls according to num_balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_true_count = 0
    for n in range(num_experiments):
        randomdrawdic = dict()
        randomdraw = hat.drawn(num_balls_drawn)
        for x in randomdraw:
            randomdrawdic[x] = randomdrawdic.get(x, 0) + 1
        countTRUE = 0
        for k, v in expected_balls.items():
            if k in randomdrawdic:
                if randomdrawdic[k] >= v:
                    countTRUE += 1
                else:
                    continue
            else:
                continue
        if countTRUE == len(expected_balls):
            experiment_true_count += 1
        else:
            continue
    return experiment_true_count / num_experiments