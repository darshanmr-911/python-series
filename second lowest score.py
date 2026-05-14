if __name__ == '__main__':
    record=[]
    s=set()
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        record.append([name,score])
        s.add(score)
    second_low_score=sorted(s)[1]
    second_low_names=[]
    for name,score in record:
        if score==second_low_score:
            second_low_names.append(name)
    for name in sorted(second_low_names):
        print(name)