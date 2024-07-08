class SearchAlgorithms:
    def sequentialSearchUnordered(self,list,value):
        found = False
        ix = 0
        while ix < len(list) and not found:
            if list[ix] == value:
                found = True
            else:
                ix += 1
        return found

    def sequentialSearchOrdered(self,list,value):
        found = False
        ix = 0
        while ix < len(list) and not found:
            if list[ix] == value:
                found = True
            else:
                if list[ix] > value:
                    return False
                ix += 1
        return found

    def binarySearch(self,list,value):
        x = 0
        y = len(list) - 1

        while x <= y:
            midPoint = (x+y) // 2
            if list[midPoint] == value:
                return True
            else:
                if value < list[midPoint]:
                    y = midPoint - 1
                else:
                    x = midPoint + 1

        return False