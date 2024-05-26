def average(arr):
    len1 = len(arr)
    st = set(arr)
    # print(st)
    ln = len(st)
    if(ln==0):
        avg = 0
    else:
      avg = sum(st) / ln
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
