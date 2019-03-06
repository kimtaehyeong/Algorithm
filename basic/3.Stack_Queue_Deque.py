# -*- coding: utf-8 -*-

# 스택(Stack) -> 한쪽 끝에서만 원소를 넣거나 뺄 수 있는 자료구조
# 프링글스 통을 생각하면 이해가 쉬울텐데, 
# 먼저 들어간 원소가 제일 나중에 나온다는 의미로 FILO(First in Last Out) 자료구조
# 앞으로 알아볼 스택(Stack), 큐(Queue), 덱(Deque) 처럼 특정 위치에서만 원소를 넣거나 뺄 수 있고 이러한 구조들을 Restricted Structure라고 부른다.
# Python에서는 List를 이용하여 구현할 수 있다.
"""
(원소 추가)  [3, 17, 11] [5] 추가 -> [3, 17, 11, 5]    - O(1)
(원소 제거)  [3, 17, 11] -> [3, 17]                   - O(1)
"""

# 원소를 추가하는 연산을 push, 꺼내는(삭제) 연산을 pop
# 수식의 괄호 쌍, DFS, Flood Fill등이 나오는데, DFS는 코딩테스트 단골 문제이므로 익숙해져야된다!
stack = [3, 17, 11]
stack.append(5) # [3, 17, 11, 5]  push 원소 추가
#stack.insert(len(list_a), 5) # stack.append(5) 와 동등
stack.pop() # 마지막 원소인 5 삭제 [3, 17, 11] (중간에 인덱스를 지정할 수도 있지만 default면 마지막 원소 삭제)
#stack.remove(list_a[-1]) # stack.pop() 와 동등하게 작동
stack[-1] # 제일 꼭대기의 원소 확인 top연산과 같은 역할
# 그 외에도 정렬하는 stack.sort(), stack.reverse() 많이 사용된다.


# 스택문제 https://www.acmicpc.net/problem/10828 풀이
N = int(input())
stack = []
def push(n):
    stack.append(n)
def pop():
    try:
        print(stack.pop())
    except:
        print(-1)
def size():
    return len(stack)
def empty():
    a = 1 if size() == 0 else 0
    print(a)
def top():
    try:
        print(stack[-1])
    except:
        print(-1)
    
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'top':
        top()




# 큐(Queue) -> 큐는 한쪽 끝에서 원소를 넣고 반대쪽 끝에서 원소를 뺄 수 있는 자료구조
# 공항에서 줄을 서는 과정을 생각해보면 먼저 들어간 원소가 제일 먼저 나온다는 의미로 FIFO(First In First Out) 자료구조라고 한다.
# 큐 형식도 BFS, Flood Fill에서 많이 사용된다.
# python에서 List형식을 큐로 사용할 수 있지만, push하거나 pop하는것은 빠르지만 다른 요소들을 모두 한 칸씩 이동시켜야 해서 효율이 떨어진다
# 그래서 collections.deque 모듈을 이용하자
"""
(원소 추가)  [3, 17, 11] [5] 추가 -> [3, 17, 11, 5]    - O(1)
(원소 제거)  [3, 17, 11] -> [17, 11]                   - O(1)
"""


from collections import deque
queue = deque([3, 17, 15])
queue.append(5) # [3,17,15,5]
queue.popleft() # 첫번째 원소인 3 꺼내기 -> [17,15,5]


# 큐(Queue) 문제 -> https://www.acmicpc.net/problem/10845
N = int(input())
from collections import deque
queue = deque()
def push(n):
    queue.append(n)
def pop():
    try:
        print(queue.popleft())
    except:
        print(-1)
def size():
    return len(queue)
def empty():
    a = 1 if size() == 0 else 0
    print(a)
def front():
    try:
        print(queue[0])
    except:
        print(-1)
def back():
    try:
        print(queue[-1])
    except:
        print(-1)
    
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()


# 덱(Deque) -> 양쪽 끝에서 원소를 넣고 뺄 수 있는 자료구조
# queue.pop() # 마지막 원소도 꺼낼 수 있다.
# 큐와 스택의 성질을 모두 가지고 있어서, 양쪽에서 삽입/삭제가 일어나는 상황을 시뮬레이션하는 느낌의 문제가 나온다.
# 마찬가지로 python에서 List형식을 덱으로 사용할 수 있지만, push하거나 pop하는것은 빠르지만 다른 요소들을 모두 한 칸씩 이동시켜야 해서 효율이 떨어진다
# 그래서 collections.deque 모듈을 이용하자
"""
(원소 추가)  [3, 17, 11] [5] 추가(왼쪽 오른쪽 둘 다 추가 가능) -> [3, 17, 11, 5] or [5, 3, 17, 11]    - O(1)
(원소 제거)  [3, 17, 11] (왼쪽 오른쪽 둘 다 삭제)-> [17, 11] or [3, 17]                 - O(1)
"""
from collections import deque
queue = deque([3, 17, 15])
queue.append(5) # [3,17,15,5]
queue.appendleft(5) # [5, 3, 17, 15, 5]
queue.popleft() # 첫번째 원소인 5 꺼내기 -> [3, 17, 15, 5]
queue.pop() # 마지막 원소인 5 꺼내기 -> [3, 17, 15]




# 덱(Dequeue) 문제 -> https://www.acmicpc.net/problem/10866
N = int(input())
from collections import deque
dequeue = deque()
def push_front(n):
    dequeue.appendleft(n)
def push_back(n):
    dequeue.append(n)
def pop_front():
    try:
        print(dequeue.popleft())
    except:
        print(-1)
def pop_back():
    try:
        print(dequeue.pop())
    except:
        print(-1)
def size():
    return len(dequeue)
def empty():
    a = 1 if size() == 0 else 0
    print(a)
def front():
    try:
        print(dequeue[0])
    except:
        print(-1)
def back():
    try:
        print(dequeue[-1])
    except:
        print(-1)
    
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    elif cmd[0] == 'push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()