class BubbleSort:
    def __init__(self,list_to_order):
        return self.sort(list_to_order)

    def sort(self,list_to_order):
        while True:
            sorting= False
            for i in range(len(list_to_order)-1):
                if list_to_order[i+1] < list_to_order[i]:
                    x=list_to_order[i]
                    list_to_order[i]=list_to_order[i+1]
                    list_to_order[i+1]=x
                    sorting=True
            if sorting:
                break

        return list_to_order

    