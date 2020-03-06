import random

class Link:

    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def insert(self, value):
        if self.head == None:
            newhead = Link(value, None, None)
            self.tail = newhead
        else:
            oldhead = self.head
            newhead = Link(value, None, oldhead)
            oldhead.next = newhead
        self.head = newhead

    def reset(self):
        self.current = None

    def next(self):
        if self.current == None:
            if self.tail == None:
                return False
            self.current = self.tail
            return True
        self.current = self.current.next
        return self.current != None

    def sort(self):
        self.__sort(self.tail, self.head)

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

if __name__ == '__main__':
    sample = random.sample(range(1000), 10)
    print 'sample {}\n'.format(sample)

    list = LinkedList()
    for i in sample:
        list.insert(i)

    list.sort()

    current = list.tail
    while True:
        print 'Value {}'.format(current.value)
        if current == list.head:
            break
        current = current.next
