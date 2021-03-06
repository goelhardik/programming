Jack has just moved to a new city called Rapture. However, he is confused by Rapture's public transport system. The rules of the public transport are as follows:

Every pair of connected stations has a fare assigned to it.

If a passenger travels from station A to station B, he only has to pay the difference between the fare from A to B and the cumulative fare that he has paid to reach station A [fare(A,B) - total fare to reach station A]. If the difference is negative, he can travel free of cost from A to B.

Since Jack is new to the city, he is unemployed and low on cash. He needs your help to figure out the most cost efficient way to go from the first station to the last station. You are given the number of stations N, and the fare between the E pair of stations that are connected.

Input Format 
The first line contains two integers, N and E, followed by E lines containing three integers each: the two stations that are connected to each other and the fare between them (C).

Output Format 
The minimum fare to be paid to reach station N from station 1. If the station N cannot be reached from station 1, print "NO PATH EXISTS" (without quotes).

Constraints 
1<=N<=50000
1<=E<=500000
1<=C<=10^7

Sample Input 
5 5
1 2 60
3 5 70 
1 4 120
4 5 150
2 3 80

Sample Output 
80

Explanation

door

There are two ways to go from first station to last station.

1 -> 2 -> 3-> 5
1 -> 4 -> 5
For the first path, Jack first pays 60 units of fare to go from station 1 to 2. Next, Jack has to pay 80-60 = 20 units to go from 2 to 3. Now, to go from 3 to 5, Jack has to pay 70-(60+20) = -10 units, but since this is a negative value, Jack pays 0 units to go from 3 to 5. Thus the total cost of this path is (60+20) = 80 units.

For the second path, Jack pays 120 units to reach station 4 from station 1. To go from station 4 to 5, Jack has to pay 150-120 = 30 units. Thus the total cost becomes (120+30) = 150 units. So, the first path is the most cost efficient, with a cost of 80.
