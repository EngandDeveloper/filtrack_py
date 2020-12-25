class BoyerMoore:

    def __init__(self, pat):
        self.right = []
        self.pat = pat
        M = len(self.pat)
        R = 256
        for c in range(R):
            self.right.append(-1)
        
        for j in range(M):
            self.right[self.pat[j]] = j

    
    def search(self,txt):
        N = len(txt)
        M = len(self.pat)
        skip = 0
        for i in range(0, N-M, i+skip):
            for j in range(M-1, 0, -1):
                if self.pat[j] != txt[i+j]:
                    skip = j - self.right[txt[i+j]]
                    if skip < 1:
                        skip = 1
                    break
            if skip == 0:
                return i
        return -1 #-1 == not found