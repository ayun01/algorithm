def rainbowSort(self, left, right, colorFrom, colorTo, colors):
        if colorFrom == colorTo:
            return
        
        if left >= right:
            return
        
        colorMid = colorFrom + int((colorTo - colorFrom) / 2)
        
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
                r  -= 1
                
        self.rainbowSort(left, r, colorFrom, colorMid, colors)
        self.rainbowSort(l, right, colorMid + 1, colorTo, colors)
