class DfsSong:

    def __init__(self):
        self.stack = []
        self.song_list = []
        self.pathlist = []


    def processPath(self):
        for x in self.song_list:
            self.pathlist.append(x.getName())
        return self.pathlist

    def dfs(self, start, end):
        start.marked = True
        self.song_list.append(start)
        if start == end:
            self.pathlist = processPath()
            return self.pathlist
        else:
            for x in start.returnAdj():
                if x.marked == False and x != null:
                    dfs(x,end)
        self.song_list.pop()
        return self.pathlist    