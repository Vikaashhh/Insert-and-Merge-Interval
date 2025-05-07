class Solution:
    def insertInterval(self, intervals, newInterval):
        merged = []  # Final answer store karne ke liye
        i = 0
        n = len(intervals)

        # Step 1: Pehle un intervals ko add karo jo newInterval se pehle aate hain (overlap nahi karte)
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Step 2: Ab un intervals ko merge karo jo newInterval ke saath overlap karte hain
        while i < n and intervals[i][0] <= newInterval[1]:
            # Start aur end ko update karo taki pura overlap cover ho jaye
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Merge hone ke baad final interval add karo
        merged.append(newInterval)

        # Step 3: Ab bache hue intervals ko add kar do (jo newInterval ke baad aate hain)
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
