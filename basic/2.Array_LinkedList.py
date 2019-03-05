# -*- coding: utf-8 -*-

# Python에서는 List가 Array처럼 쓰인다.
list_a = [1,2,3,4,5]

# 리스트 삽입
# 삽입시 해당 요소에 삽입 후 뒤에있는 리스트는 한칸씩 밀려, O(N)시간이 걸린다
list_a.insert(2, 11) # 2번째 요소에 11 삽입
list_a.append(1000) # 맨 마지막 원소 뒤에 새 요소 추가

#리스트 삭제
list_a.pop(0) # 0번째 인덱스 제거 후 앞으로 한칸씩 이동 O(N)시간
list_a.pop() # 인자값을 넣지 않으면 맨 마지막 요소 제거

# 리스트 크기 확인
print(len(list_a)) # 리스트 크기는 O(1)시간 복잡도

# 예제 알파벳 갯수(icpc.me/10808)
S = input('알파벳 입력:') # 통과하고싶으면 input안에들어있는 string값 제거 후 제출
voca = [chr(i) for i in range(ord('a'), ord('z') + 1)]
count = 0
count_list = []

for i in voca:
    count_list.append(S.count(i))
for i in count_list:
    print(i, end=' ')
    
    
"""
연결 리스트(Linked Lists)

Linked List를 알기전에 추상적 자료구조(Abstract Data Structures)를 먼저 살펴보고 진행하자.
추상적 자료구조라는것은, 내부구현에 대해서는 크게 신경을 쓰지않고, 밖에서 보이는 자료구조를 말하는데
대표적으로 
Data -> 정수, 문자열, 레코드 etc...
A set of operations -> 삽입, 삭제, 순회, 정렬, 탐색 etc... 이 제공될 수 있다.
즉! 데이터 set들에 대해서 가해질 수 있는 일련의 연산을 추상적으로 밖에 보여주는것을 추상적 자료구조라고 한다.
Single Linked List -> 자신의 다음 원소의 위치만 가지고 있는 연결리스트
Doubly Linked List -> 자신의 이전/다음 원소를 모두 가지고 있는 연결리스트
Circular Linked List -> 마지막 원소가 처음 원소의 위치를 가지고 있는 연결리스트
Python에서 클래스로 만들어서 해야되고, 사실상 구현해서 쓸일은 많진 않을꺼같다..(알고리즘의 기본이 되는것이므로 알아보자)
그렇다면 이제 Linked List를 추상적 자료구조형태로 구현을 해보자.
"""

# Node는 데이터(문자열, 레코드 등등)를 담고 다음 데이터에 링크를 가지고있다.
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None # 현재 다음 데이터를 담고있는게 없으므로, None을 대입



# LinkedList에서는 현재 비어 있는 연결 리스트를 만들어서 구성을 했다.
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
    
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : empty'
        
        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
        
    def getAt(self, pos): #특정 원소 참조
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i = i + 1
        return curr
    
    def traverse(self): # 리스트 순회
        result = []
        
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
    
    def getLength(self): # 리스트 길이 얻어내기
        return self.nodeCount
    
    def insertAt(self, pos, newNode): # 리스트 원소의 삽입
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True
    
    def popAt(self, pos): # 리스트 원소 삭제
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        pop = self.getAt(pos)
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        else:
            if pos == 1:
                self.head = pop.next
            else:
                if pos == self.nodeCount:
                    prev = self.getAt(pos - 1)
                    self.tail = prev
                    prev.next = None
                else:
                    prev = self.getAt(pos - 1)
                    prev.next = pop.next
                    
    
    def concat(self, L):# 두 리스트 연결
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount = self.nodeCount + L.nodeCount
#ex
        
a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L) # empty
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
print(L)
L.popAt(3)
print(L)

# 손코딩에서 물어볼 수 있는 2문제가 있는데
# 궁금하면 https://blog.encrypted.gg/725?category=773649 들어가서 참고해보면 좋을꺼같다.