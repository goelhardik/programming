def min_candies(ratings):
    n = len(ratings)
    candies = [1 for i in range(n)]
    # go forward, set candy for next as previous + 1, if required
    for i in range(1, n):
        if (ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]):
            candies[i] = candies[i - 1] + 1
    # go backward, set candy for next as previous + 1, if required
    for i in range(n - 2, -1, -1):
        if (ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]):
            candies[i] = candies[i + 1] + 1
                    
    return sum(candies)
    

# driver code
n = int(input())
ratings = []
for i in range(n):
    r = int(input())
    ratings.append(r)
print(min_candies(ratings))
