class BubbleSort:
    def __init__(self):
        pass

    def srt(self,list_to_order):
        while True:
            sorting= False
            for i in range(len(list_to_order)-1):
                if list_to_order[i+1] < list_to_order[i]:
                    x=list_to_order[i]
                    list_to_order[i]=list_to_order[i+1]
                    list_to_order[i+1]=x
                    sorting=True
            if not sorting:
                return list_to_order

x= BubbleSort()

print(x.srt([5,6,4,2,1,8,3]))
    