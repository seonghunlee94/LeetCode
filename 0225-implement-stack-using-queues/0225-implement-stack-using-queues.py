class MyStack:

    def __init__(self):
        self.queue = collections.deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
    
    # def change_index(self): 
    # 함수로 top()이나 pop()할 때 지속적인 변경을 주고 싶지만, 결국에는 pop() top() 순서를 정하지 않으면 구현할 수 없는 것 같다. 결국 지금은 일회성으로 stack 느낌을 주는게 최선인 것 같다.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()