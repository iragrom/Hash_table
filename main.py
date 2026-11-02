import sys

class HashTable:
    def __init__(self):
        self.cap = 8
        self.table = [[] for _ in range(self.cap)]
        self.size = 0

    def _hash(self, key):
        h = 0
        for char in key:
            h = (h * 31 + ord(char)) % self.cap
        return h

    def _resize(self):
        old_table = self.table
        self.cap *= 2
        self.table = [[] for _ in range(self.cap)]
        self.size = 0
        for bucket in old_table:
            for k, v in bucket:
                self.put(k, v)

    def put(self, key, val):
        if self.size / self.cap > 0.75:
            self._resize()
            
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, val)
                return
        self.table[idx].append((key, val))
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return "Error"

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                self.size -= 1
                return v
        return "Error"

    def get_size(self):
        return self.size

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    q = int(input_data[0])
    ht = HashTable()
    
    for i in range(1, q + 1):
        parts = input_data[i].split()
        cmd = parts[0]
        
        if cmd == "put":
            ht.put(parts[1], int(parts[2]))
        elif cmd == "get":
            print(ht.get(parts[1]))
        elif cmd == "del":
            print(ht.delete(parts[1]))
        elif cmd == "size":
            print(ht.get_size())

if __name__ == "__main__":
    main()
