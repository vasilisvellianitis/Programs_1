#to kalesma ths synarthshs ginetai me monh agkilh
#px sumIntervals( [1,2], [6, 10], [11, 15] )
def sumIntervals(*intervals) :
    interval = [intervals]
    a = len(intervals)
    #taxinomw ta intervals se auxousa seira
    #me vash to prwto stoixeio kathe interval
    for x in range(0,a-1):
        for y in range(a-1,x,-1):
            if intervals[y-1][0] > intervals[y][0]:
                temp = intervals[y-1][0]
                intervals[y-1][0] = intervals[y][0]
                intervals[y][0] = temp
                temp2 = intervals[y-1][1]
                intervals[y-1][1] = intervals[y][1]
                intervals[y][1] = temp2
    total = 0
    #to prwto interval den xreiazetai kapoion elegxo
    total = total + intervals[0][1] - intervals[0][0]
    voithitiko = intervals[0][1]
    #xekinaw  na elegxw apo to deytero
    #me vash to telos tou prwtou
    #kai tropopoiw to voithiko analoga 
    for x in range (1,a):
        if intervals[x][0] < voithitiko:
            if intervals[x][1] > voithitiko: 
                total = total + intervals[x][1] - voithitiko
                voithitiko = intervals[x][1]
        elif intervals[x][0] > voithitiko:
            total = total + intervals[x][1] - intervals[x][0]
            voithitiko = intervals[x][1]
        elif intervals[x][0] ==  voithitiko:
            total = total + intervals[x][1] - voithitiko
            voithitiko = intervals[x][1]
    print (total)
    return





