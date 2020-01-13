class BubbleSort:

    @staticmethod
    def sort(arr):
        if type(arr) is int or type(arr) is float:
            return arr
        if type(arr) is str and len(arr) == 1:
            return arr
        try:
            arr = list(arr)
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
      
        except TypeError:
            return 'Invalid Input'