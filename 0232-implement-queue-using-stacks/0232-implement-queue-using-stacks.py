class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
        

    def push(self, x: int) -> None:
        self.stack_push.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.stack_pop.pop()
        

    def peek(self) -> int:
        # self.stack_pop이 없을 때만 다시 넣어줘야 queue 형식이 유지될 수 있다.
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            
        return self.stack_pop[-1]
        

        

    def empty(self) -> bool:
        # queue 형식을 유지하기 위해 self.stack_push에 데이터를 남겨둬야 하는 경우도 있다.
        return self.stack_push == [] and self.stack_pop == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()