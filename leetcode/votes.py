import collections
class Solution:
    def rankTeams(self, votes) -> str:
        counts = collections.defaultdict(list)
        for vote in zip(*votes):
            print(vote)
            cntr=collections.Counter(vote)
            for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                counts[ch]+=[-1*cntr[ch]]
        print(counts)
        return "".join(sorted(votes[0],key=lambda x:counts[x]+[x]))


        

if __name__ == "__main__":
    solution=Solution()
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    ans=solution.rankTeams(votes)
    print(ans)
