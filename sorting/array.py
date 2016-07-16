class Solution(object):
    def  __init__(self):
        pass
    def swap(self, data, x,y ):
        temp=data[x]
        data[x]=data[y]
        data[y]=temp

class Bobble(Solution):
    def sort(self, data):
        ### error start
        for i in range(len(data)-1,-1,-1):
            for  j in range(1,i+1):
                 ### error end
                if data[j-1] > data [j]:
                    self.swap(data,j-1,j)

class Insert(Solution):
    def sort(self, data,step=1):
        for i in range(0,len(data),step):
            ### error start
            for j in range(i,0,-1*step):
                ### error end
                if data[j-step] > data [j]:
                    self.swap(data,j-step,j)

class Selection(Solution):
    def sort(self,data):
         for i in range(0,len(data)):
            min=i
            for j in range(i,len(data)):
                if  data[j]<data[min]:
                    min=j
            self.swap(data,min,i)

class Shell(Insert):
    def sort(self,data):
        for step in range(int(len(data)/2),0,-1):
            super(Shell,self).sort(data,step=step)

class Heap(Solution):
    # for a node i, its root is int((i-1)/2)
    # its children are 2i+1 and 2i+2
    def sort(self,data):
        # build heap
        for loc in range(len(data)-1,int((len(data)-1)/2),-1):
            self.head_adjust(data,loc)
        print data
        for loc in range(len(data)-1,0,-1):
            self.swap(data,0,loc)
            print data
            self.head_adjust(data,loc-1)
            print data,loc-1


            # self.swap(data,0,loc)
    def  head_adjust(self,data,loc):
        # adjust a tree so that the root is always the largest element
        cur=loc
        # left_child=2*cur+1
        # while left_child<len(data):
        #     max_child=left_child
        #     if left_child+1 < len(data): 
        #          if data[left_child]<data[left_child+1] :
        #             max_child=left_child+1
        #     if data[cur]<data[max_child]:
        #         self.swap(data,cur,max_child)
        #     else:
        #         break
        #     cur=left_child
        #     left_child=2*cur+1
        print data[cur]
        parent=int((cur-1)/2)
        while parent >= 0:
            # error start
            max_child=2*parent+1
            if 2*parent+2 < len(data): 
                 if data[2*parent+1]<data[2*parent+2] and cur==2*parent+2:
                    max_child=2*parent+2
            if data[parent]<data[max_child]:
                self.swap(data,parent,max_child)
            # error end
            cur = parent
            parent=int((cur-1)/2)


class Quick(Solution):
    def sort(self,data):
        self.quick_sort(data,0,len(data)-1)

    def quick_sort(self,data,start,end):
        ### error start
        if not start<end:
            return
         ### error end
        loc= self.partition(data,start,end)
        self.quick_sort(data,start,loc-1)
        self.quick_sort(data,loc+1,end)
    
    def partition(self,data,start,end):
        value=data[start]
        i,j=start,end
        while i<j:
            while i<j and data[j]>=value:
                j=j-1
            if i< j:
                data[i]=data[j]
                i=i+1
            while i<j and data[i]<value:
                i=i+1
            if i<j:
                data[j]=data[i]
                j=j-1
        data[i]=value
        return i

class Merge(Solution):
    def merge(self,data, start,end):
        ### error start
        if end - start <0:
            return []
        elif end-start ==0:
            return [data[start]]
        mid=int((end-start)/2)+start
        ### error end
        front=self.merge(data,start,mid)
        back=self.merge(data,mid+1,end)
        i,j,k=0,0,0
        merged=[]
        while i!=len(front) or j!=len(back):
            if  i==len(front):
                while j!=len(back):
                    merged.append(back[j])
                    j=j+1
                    k=k+1
            elif j==len(back):
                while i!=len(front):
                    merged.append(front[i])
                    i=i+1
                    k=k+1
            else:
                if front[i] > back[j]:
                    merged.append( back[j])
                    j=j+1
                else:
                    merged.append(front[i])
                    i=i+1
                k=k+1
        return merged

    def sort(self,data):
        result=self.merge(data,0,len(data)-1)
        for i in range(len(data)):
            data[i]=result[i]

data=[3,7,6,4,2,1,-1,3]
solution=Heap()
solution.sort(data)
print(data)