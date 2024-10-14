class MinStack:
    def __init__(self):
        self.__stack = []
        self.__min = []

    def __push_min(self, val):
        if len(self.__min) > 0:
            if val <= self.__min[-1]:
                self.__min.append(val)
        else:
            self.__min.append(val)

    def __pop_min(self, val):
        if len(self.__min) > 0 and val == self.__min[-1]:
            self.__min.pop()

    def push(self, val: int) -> None:
        self.__stack.append(val)
        self.__push_min(val)

    def pop(self) -> None:
        return_element = self.__stack.pop()
        self.__pop_min(return_element)
        return return_element

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[-1]

    # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()