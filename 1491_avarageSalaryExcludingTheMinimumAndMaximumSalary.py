class Solution:
    def average(self, salary):
        salary = sorted(salary)
        salary.pop(0)
        salary.pop()
        return sum(salary)/ len(salary)
    
if "__main__":
    salary = [4000,3000,1000,2000]
    print(Solution().average(salary))