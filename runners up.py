#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    l = map(int, input().split())
    print(sorted(list(set(l)))[-2])


#or

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=set(arr)
    l=list(s)
    l.sort()
    print(l[-2])
    