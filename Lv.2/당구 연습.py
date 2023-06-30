def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        temp = []
        if startX != x or startY > y:
            temp.append(abs(startX-x)**2+abs(2*n-startY-y)**2)
        if startX != x or startY < y:
            temp.append(abs(startX-x)**2+abs(startY+y)**2)
        if startY != y or startX < x:
            temp.append(abs(startX+x)**2+abs(startY-y)**2)
        if startY != y or startX > x:
            temp.append(abs(2*m-startX-x)**2+abs(startY-y)**2)
        answer.append(min(temp))
    return answer