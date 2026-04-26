# 10. Sports Tournament Points Table

points = [10, -5, 15, 20, -2, 18]

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)
#Output
"""Leaderboard: [20, 18, 15, 10, 0, 0]
Winner Points: 20
Runner-up Points: 18"""