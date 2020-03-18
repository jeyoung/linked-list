import random

class Link:

    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

class LinkedList:

    def __init__(self):
        self.head = Link(None, None, None)
        self.tail = self.head

    def add(self, value):
        old_head = self.head
        new_head = Link(None, None, old_head)
        old_head.value = value
        old_head.next = new_head
        self.head = new_head

    def sort(self):
        self.__sort(self.tail, self.head.previous)

    def __sort(self, tail, head):
        if tail == head:
            return
        pivot = head
        current = tail
        while True:
            if current.value > pivot.value:
                tmp = current.value
                current.value = pivot.previous.value
                pivot.previous.value = tmp

                tmp = pivot.value
                pivot.value = pivot.previous.value
                pivot.previous.value = tmp

                pivot = pivot.previous
            elif current == pivot:
                if pivot != tail:
                    self.__sort(tail, pivot.previous)
                if pivot != head:
                    self.__sort(pivot.next, head)
                break
            else:
                current = current.next

    def traverse(self, callback):
        current = self.tail
        while True:
            if current == self.head:
                break
            callback(current.value)
            current = current.next

if __name__ == '__main__':
    sample = random.sample(range(100), 25)

    list = LinkedList()
    for i in sample:
        list.add(i)

    list.sort()

    def printitem(x):
        print('{}'.format(x))

    list.traverse(printitem)
