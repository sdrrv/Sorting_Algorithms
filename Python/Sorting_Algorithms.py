class SortingAlgorithms:
    def __init__(self):
        pass

    def bubble_sort(self,list_to_order):
        count = 0
        while True:
            count+=1
            sorting= False
            for i in range(len(list_to_order) - count):
                if list_to_order[i+1] < list_to_order[i]:
                    x=list_to_order[i]
                    list_to_order[i]=list_to_order[i+1]
                    list_to_order[i+1]=x
                    sorting=True
            if not sorting:
                return list_to_order
    
    def insertion_sort(self,list_to_order):
        if len(list_to_order)<=1:
            return list_to_order
        else:
            for i in range(1,len(list_to_order)):
                k=i
                element = list_to_order[i]
                while k>0 and element < list_to_order[k-1]:
                    list_to_order[k]=list_to_order[k-1]
                    list_to_order[k-1]= element
                    k-=1
            return list_to_order

    def selection_sort(self, list_to_order):
        if len(list_to_order)<=1:
            return list_to_order
        for i in range(len(list_to_order)):
            high = list_to_order[i]
            order = i
            for j in range(i,len(list_to_order)):
                if high > list_to_order[j]:
                    high = list_to_order[j]
                    order = j
            list_to_order[order] = list_to_order[i]
            list_to_order[i] = high
        return list_to_order

    def quick_sort(self,list_to_order):
        pass

















    