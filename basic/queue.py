class Queue():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        if len(self.items) == 0:
            return False
        else:
            return True
        
    def enqueue(self, element):
        self.items.insert(0, element) # 첫번째 인덱스에 값 삽입
    
    def dequeue(self):
        element = self.items.pop()
        if element is not None: # None값이 아니면
            return element
        else:
            print('Queue is empty') # 비어 있다면 메시지 출력
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            print('Queue is empty')
    
    def state(self):
        return self.items
    
    
queue = Queue()
print('큐 비어있는지 확인 : ', queue.isEmpty()) # False면 비어 있고 아니면 True 반환
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(40)
queue.enqueue(60)
print(queue.dequeue()) # 첫번째 원소인 10을 꺼내서 [60,40,20] 이 된다.
print(queue.state()) # [60,40,20]
print('스택 비어있는지 확인 : ', queue.isEmpty())
print('마지막 원소 확인 : ', queue.peek()) # 40
            