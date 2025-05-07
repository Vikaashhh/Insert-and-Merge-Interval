# 🧩 Day 25 - Insert Interval

**Problem Statement:**

You are given a list of non-overlapping intervals sorted in ascending order by their start times.  
You also have a new interval which you need to insert into the list, merging overlapping intervals if needed, so that the final list still contains only non-overlapping intervals sorted by start time.

---

## 🧠 Approach:
Add Intervals Before New Interval:
All intervals that end before the new interval starts can be added directly to the result.

Merge Overlapping Intervals:
While the current interval starts before or at the same point as the new interval ends, we merge them by adjusting the start and end.

Add Remaining Intervals:
Once all possible merges are done, the rest of the intervals (that start after the new interval ends) are added as-is.

---

## 📊 Complexity Analysis:
Time Complexity: O(N), where N is the number of intervals

Space Complexity: O(N), for the result array

---

## 🔍 Tags:
#Greedy #Intervals #MergeIntervals #Python #DSA #GFG160 #GeekStreak2025

Happy Coding! 🚀
