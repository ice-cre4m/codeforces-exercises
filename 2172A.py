"""If the maximum score and the minimum score differ by at least 
10 points, print check again (the judging seems inconsistent, 
so the panel must re-evaluate).


Otherwise, print final X, where X is the median of the three scores
(the score that would be in the middle if all three were sorted 
in non-decreasing order)."""



def main():
    scores = list(map(int, input().split()))
    scores.sort()
    if(scores[2]-scores[0] >= 10):
        print("check again")
    else:
        print("final ",scores[1])
    

if __name__ == "__main__":
    main()