class Solution:
    def calPoints(self, operations: List[str]) -> int:
    #  An integer x: Record a new score of x.
    # '+': Record a new score that is the sum of the previous two scores.
    # 'D': Record a new score that is the double of the previous score.
    # 'C': Invalidate the previous score, removing it from the record.

     score = []
     for i in operations:
        if i == '+':
            result = score[-1] + score[-2]
            score.append(result)
        elif i == 'D':
            score.append(score[-1] * 2)
        elif i == 'C':
            score.pop()
        else :
            score.append(int(i))
        
     return sum(score)

