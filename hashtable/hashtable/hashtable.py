class hash_table():
    def __init__(self, size=1024):
        self.size = size
        self.data = [None]*self.size

    def __str__(self):
        return str(self.__dict__)


    def get(self, key):
      
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None

    def set(self, key, value):
       
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        print(self.data)

    def keys(self):
       
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
       
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array

    def contains(self, key):
       
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return True
        return False

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash    

if __name__ == '__main__':
   pass
