"""
from queue import Queue

class Deque(Queue): # 큐 상속
    def enqueue_back(self, element):
        self.items.append(element)
    
    def dequeue_front(self):
        element = self.items.pop(0) # 첫번째 인덱스 뽑기
        if element is not None:
            return element
        else:
            print('Deque is empty.')
            

deque = Deque()
print('데크 비어있는지 확인 : ', deque.isEmpty())
deque.enqueue(10)
"""

from collections import deque

deque = deque(['삼성','LG','카카오'])
print(deque) # deque(['삼성', 'LG', '카카오'])
deque.append('네이버')
print(deque) # deque(['삼성', 'LG', '카카오', '네이버'])
deque.popleft() #삼성이 꺼내진다.
print(deque) # deque(['LG', '카카오', '네이버'])
deque.pop() # 제일 오른쪽인 네이버가 꺼내진다.
print(deque) # deque(['LG', '카카오'])
deque.appendleft('삼성')
deque.append('네이버')
print(deque) # deque(['삼성', 'LG', '카카오', '네이버'])