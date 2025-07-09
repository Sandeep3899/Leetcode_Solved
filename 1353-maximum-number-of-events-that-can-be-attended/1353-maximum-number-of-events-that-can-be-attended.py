class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])  # Sort by end day
        max_day = max(end for _, end in events)
        
        # parent[i] tells us the next available day >= i
        parent = list(range(max_day + 2))  # Extra space to handle edge cases

        def find(day):
            # Path compression: points directly to the next available day
            if parent[day] != day:
                parent[day] = find(parent[day])
            return parent[day]

        count = 0
        for start, end in events:
            available_day = find(start)
            if available_day <= end:
                count += 1
                # Mark this day as used by pointing to the next available one
                parent[available_day] = find(available_day + 1)

        return count
