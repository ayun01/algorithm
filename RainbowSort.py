#http://www.jiuzhang.com/qa/4289/
def rainbowSort(left, right, colorFrom, colorTo, colors):
    print "[{}:{}],[{}:{}],{}".format(left,right,colorFrom,colorTo,colors)

    if colorFrom == colorTo:
        return

    if left >= right:
        return

    colorMid = colorFrom + int((colorTo - colorFrom) / 2)
    #print 'mid={}'.format(colorMid)

    l = left
    r = right

    while l <= r:
        while l <= r and colors[l] <= colorMid:
            l += 1
        while l <= r and colors[r] > colorMid:
            r -= 1
        if l <= r:
            temp = colors[l]
            colors[l] = colors[r]
            colors[r] = temp
            l += 1
            r -= 1
    #print 'left'
    rainbowSort(left, r, colorFrom, colorMid, colors)
    #print 'right'
    rainbowSort(l, right, colorMid + 1, colorTo, colors)

colors = [3, 2, 2, 1, 4]
k = 4

rainbowSort(0,4,1,4,colors)
#print colors
