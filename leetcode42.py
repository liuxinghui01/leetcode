class Solution:
    def trap(self, height):
        s = 0
        i = 0
        j = len(height)-1
        left_hight_cmp = 0
        right_hight_cmp = 0
        while(i<j):
            if height[i]<height[j]:
                if height[i]<left_hight_cmp:
                    s += (left_hight_cmp-height[i])
                else:
                    left_hight_cmp = height[i]
                i+=1
            else:
                if height[j]<right_hight_cmp:
                    s += (right_hight_cmp-height[j])
                else:
                    right_hight_cmp = height[j]
                j-=1
        return s

if __name__ =='__main__':
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    entity = Solution()
    print(entity.trap(input))
