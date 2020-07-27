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
    
    def insertion_sort(list_to_order):
        if len(list_to_order)<=1:
            return list_to_order

        else:
            for i in range(1,len(list_to_order)):
                if list_to_order[i-1] > list_to_order[i]:
                    x=list_to_order[i]
                    list_to_order[i]=list_to_order[i-1]
                    list_to_order[i-1]=x
                    
                

    
























    