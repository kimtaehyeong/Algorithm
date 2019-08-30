class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items) == 0:
            return False
        else:
            return True
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        element = self.items.pop()
        if element is not None:
            return element
        else:
            print('Stack is empty.')
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
stack = Stack()
print('스택 비어있는지 확인 : ', stack.isEmpty()) # False면 비어 있고 아니면 True 반환
stack.push(10)
stack.push(20)
stack.push(40)
stack.push(60)
print(stack.pop()) # 마지막 원소인 60을 꺼내서 [10,20,40] 이 된다.
print('스택 비어있는지 확인 : ', stack.isEmpty())
print('마지막 원소 확인 : ', stack.peek()) # 40