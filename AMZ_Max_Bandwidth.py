# For n tv channels, given show start time, end time & bandwidth needed for each channels, find the maximum bandwidth required at peak. a show represented as [1,30,2] meaning [show-start-time, show-end-time, bandwidth-needed].

# e.g. n =3 channels, 
# [[1,30, 2],[31,60, 4],[61,120, 3],
# [1,20,2],[21,40,4],[41,60,5],[61,120,3],
# [1,60,4],[61,120,4]]

# Ans: 13, for time slot between 41-60 each channel need 4,5,4 bandwidth respectively. 13 is highest (peek/max) bandwidth.

# Note

# Min-size-of-show = 2 (min)
# Max-duration-for-show = 720 (min) same as 24hours
# Max-bandwidth-per-show = 100 (mbps)
# n<1000
# Some channels can decide not to broadcast any show for given time-slot, which mean there will be 0 bandwidth required for that channel for given time-slot


class Solution:
    def get_max_bandwidth(self, bandwidths: list[list[int]]):
        points = []
        for start, end, band in bandwidths:
            points.append((start, band))
            points.append((end, -1 * band))

        points.sort(key=lambda x: x[0])
        max_value = 0
        curr_value = 0
        for _, band in points:
            curr_value += band
            max_value = max(curr_value, max_value)
        
        return max_value


max_value = Solution().get_max_bandwidth([[1,30, 2],[31,60, 4],[61,120, 3],[1,20,2],[21,40,4],[41,60,5],[61,120,3],[1,60,4],[61,120,4]])

print(max_value)


class Solution2:
    def find_max_band(self, ch_list):
        max_end = max([ch[1] for ch in ch_list])
        sum = [0]*max_end
        max_band = 0
        for ch in ch_list:
            for session in range(ch[0],ch[1]):
                sum[session]+=ch[2]
                if sum[session]>max_band:
                    max_band = sum[session]
        return max_band

max_value = Solution2().find_max_band([[1,30, 2],[31,60, 4],[61,120, 3],[1,20,2],[21,40,4],[41,60,5],[61,120,3],[1,60,4],[61,120,4]])

print(max_value)
