class Solution:
    def JobScheduling(self, jobs):
        # Sort by profit (index 2) in descending order
        jobs.sort(key=lambda x: x[2], reverse=True)

        max_deadline = 0
        for job in jobs:
            if job[1] > max_deadline:
                max_deadline = job[1]

        slots = [-1] * (max_deadline + 1)
        curr_jobs = total_profit = 0

        for job in jobs:
            # job[1] is the deadline, job[2] is the profit
            for j in range(job[1], 0, -1):
                if slots[j] == -1:
                    slots[j] = job[0] # job[0] is JobID
                    curr_jobs += 1
                    total_profit += job[2]
                    break
        
        return curr_jobs, total_profit
