class MyObject:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[index] if self.list != None else None

assert len([1,2,3]) == 3
assert [1,2,3][0] == 1
assert len(MyObject([1,2,3,4,5])) == 5
assert MyObject([1,2,3,4,5])[0] == 1