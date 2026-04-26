# 9. Movie Rating System

ratings = [5, 4, 3, 6, 2, 1, 5, 0]

# Remove invalid ratings
ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings)
five_star = ratings.count(5)

ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", average)
print("5-Star Ratings:", five_star)
#Output
"""Valid Ratings: [1, 2, 3, 4, 5, 5]
Average Rating: 3.3333333333333335
5-Star Ratings: 2"""