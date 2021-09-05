class Queue:
    def __init__(self, stack1, stack2):
        self.s1 = stack1
        self.s2 = stack2

    def enqueue(self, e):
        return self.s1.append(e)

    def is_empty(self, s):
        return len(s) == 0

    def front(self):
        if not self.is_empty(self.s2):
            return self.s2[-1]
        else:
            while not self.is_empty(self.s1):
                popped_element = self.s1.pop()
                self.s2.append(popped_element)
            return self.s2[-1]

    def dequeue(self):
        if not self.is_empty(self.s2):
            return self.s2.pop()
        else:
            while not self.is_empty(self.s1):
                popped_element = self.s1.pop()
                self.s2.append(popped_element)
            return self.s2.pop()

if __name__ == '__main__':
    n = int(input())
    stack1 = []
    stack2 = []
    queue_obj = Queue(stack1, stack2)
    for query in range(n):
        current_query = input()
        if current_query[0] == '1':
            queue_obj.enqueue(int(current_query.split(' ')[1]))
        elif current_query == '2':
            queue_obj.dequeue()
        else:
            print(queue_obj.front())
