class FrameCounter:
    def __init__(self,count_max):
        self.count_max = count_max
        self.count_start = 0
        self.flag = False

    def run(self):
        if self.count_start < self.count_max:
            self.count_start += 1
        else:
            self.flag = True

    def reset(self):
        self.count_start = 0
        self.flag = False
