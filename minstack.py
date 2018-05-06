class MinStack(object):
    
    
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append((x,min(self.getmin(),x)))
    
    