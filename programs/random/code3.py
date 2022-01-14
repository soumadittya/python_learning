# finding the overlapping intervals

intervals = [[1, 2], [2, 5], [5, 6], [3, 7], [4,5]]
sorted_intervals = intervals.copy()


def sort_lower_limit(element):
    return element[0]

sorted_intervals.sort(key = sort_lower_limit)

overlapping_intervals = []

for i in range(1, len(sorted_intervals)):
    if(sorted_intervals[i][0] < sorted_intervals[i - 1][1]):
        if(sorted_intervals[i - 1] not in overlapping_intervals):
            overlapping_intervals.append(sorted_intervals[i - 1])
        if(sorted_intervals[i] not in overlapping_intervals):
            overlapping_intervals.append(sorted_intervals[i])

print(overlapping_intervals)