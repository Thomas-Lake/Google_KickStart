#Number of test cases.
T = int(input())
#Results.
res = []

#Loop for each test case.
for i in range(T):
    #This splits the input up into each of the required variables (changes for each question).
    N, K, S = map(int, input().split(' '))

    restart = (K-1)+N+1
    backward = (K-1)+(K-S)+(N-S)+1

    L = restart if restart < backward else backward

    res.append("Case #{}: {}".format(i+1,L))
for i in res:
    print(i)



