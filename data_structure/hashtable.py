# Hash Table


class HashTable:
    def __init__(self,size):
        self.size = size
        self.hashTable = [0 for i in range(self.size)]
    
    def hashFunction(self,key): # 키값을 해시테이블의 크기로 나눈 division h.f. 사용
        return key % self.size 
    
    # Open Addressing - Linear probing 에서의 삽입/탐색/삭제 연산

    # 가장 기본적으로, 키값을 인덱스로 변환하여 슬롯을 찾고, 슬롯에 key값이 없으면 key가 삽입될 슬롯 return 혹은
    # Linear probing으로 슬롯 한칸씩 내려가면서 key값이 있으면 그 슬롯을 return  
    def findSlot(self,key): # 키값을 h.f.에 입력해 해시테이블에 저장될 인덱스를 출력하는 함수
        i = self.hashFunction(key)
        start = i
        while (self.hashTable[i] != 0) and (self.hashTable[i][0] != key):
            i = (i+1) % self.size # 한 슬롯씩 내려가다 끝 슬롯 다음이 첫 슬롯이 될 수 있게 나머지 연산을 돌림 
            if i == start : # 테이블을 돌아 원래 슬롯에 돌아왔다는 것은, 테이블이 꽉 찼다는 뜻
                i = None 
                return i
        return i
    
    def set(self,key,value=None):
        i = self.findSlot(key)
        if i == None:
            print("Hash Table is full! Expand table size!")
            return None
        if self.hashTable[i] != 0: # key가 들어간 슬롯이 이미 있어 value값만 업데이트될 때,
            self.hashTable[i] = (key,value)
        else:                      # 아예 빈 슬롯에 key와 value를 추가하는 케이스
            self.hashTable[i] = (key,value)
            return key

    def search(self,key):
        i = self.findSlot(key)
        if i == None:
            print("Hash Table is full! Could not find key!")
            return None
        if self.hashTable[i] == 0:
            print("Could not find key!")
            return None
        else:
            return self.hashTable[i][1] # key값이 들어있는 슬롯의 데이터 읽기

    # collision 발생해서 슬롯이 밀렸던 경우를 고려해서 나머지 슬롯에 있는 값들을 이동시켜야 한다
    def remove(self,key):
        i = self.findSlot(key)
        if self.hashTable[i] == 0 : return None
        j = i
        while True: 
            self.hashTable[i] = 0 # 슬롯 내 데이터를 삭제
            while True: # 밀려서 set된 슬롯들을 찾고, 이동시키는 과정
                j = (j+1) % self.size
                if self.hashTable[j] == 0: # 삭제한 i 슬롯 다음 슬롯이 비었다면, 적어도 i 슬롯의 데이터로 인해 collision이 발생하지 않았다는 뜻. 옮길 게 없다
                    return print('Remove Complete!')
                k = self.hashFunction(self.hashTable[j][0]) # 테이블이 비었다면 j에 있는 데이터가 원래 들어갈 슬롯은 k
                if (k<=i<=j) or (j<k<i) or (i<j<k) : # k 슬롯에 갔어야할 데이터가 밀려 i를 넘어 j 슬롯에 들어간 모든 경우
                    self.hashTable[i] = self.hashTable[j] # 빈 슬롯이 된 i 슬롯에 j 슬롯 데이터를 이동
                    break
            i = j # i를 j로 바꿔 j 슬롯을 비우고 다음 슬롯을 확인하는 while 반복

hT = HashTable(10)
hT.set(3,'aaaa')
hT.set(5,'bbbb')
hT.set(13,'cccc')
print(hT.hashTable)
print(hT.search(5))
hT.remove(3)
print(hT.hashTable)
print(hT.search(13))
