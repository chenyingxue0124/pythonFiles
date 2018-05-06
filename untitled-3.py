class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self,item):
        return self.items.pop()
    
    def clear(self):
        del self.items[:]
        
    def empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[self.size() -1]
    
    def get(self):
        return self.items
    
if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('a')
    print(my_stack.get())
    print(my_stack.size())
    print(my_stack.top())