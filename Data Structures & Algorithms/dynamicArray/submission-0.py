class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dy_arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.dy_arr[i]

    def set(self, i: int, n: int) -> None:
        self.dy_arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.dy_arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dy_arr[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_dy_arr = [0] * self.capacity

        for i in range(self.length):
            new_dy_arr[i] = self.dy_arr[i]
        self.dy_arr = new_dy_arr
    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity