import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}
        time = 0

        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 0
            task_dict[task] += 1

        queue = deque([])           # to enforce cooldown
        counts = [-c for task, c in task_dict.items()]
        heapq.heapify(counts)

        while counts or queue:
            time += 1

            print(queue, counts)

            while queue and queue[0][1] < time:
                new_cnt, _ = queue.popleft()
                heapq.heappush(counts, -new_cnt)

            if len(counts):
                cnt = abs(heapq.heappop(counts))
                cnt -= 1
                if cnt > 0:
                    queue.append((cnt, time + n))

        return time