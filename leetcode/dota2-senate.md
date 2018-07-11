# problem
>In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

1. Ban one senator's right: 
A senator can make another senator lose all his rights in this and all the following rounds.
2. Announce the victory: 
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:
```
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
```
Example 2:
```
Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
```

# codes

```
class Solution {
public:
    string predictPartyVictory(string senate) {
        int n=senate.size();
        int cntR=0;
        int cntD=0;
        for(char c:senate){
            c=='R' ? cntR++:cntD++;
        }
        if(cntR==0) return "Dire";
        if(cntD==0) return "Radiant";
        while(cntR>0&&cntD>0){
            for(int i=0;i<n;i++){
                if(senate[i]=='R'){
                    for(int j=i+1;j<i+n;j++){
                        if(senate[j%n]=='D'){
                            senate[j%n]='B';
                            --cntD;
                            break;
                        }
                    }
                }else if(senate[i]=='D'){
                    for(int j=i+1;j<i+n;j++){
                        if(senate[j%n]=='R'){
                            senate[j%n]='B';
                            --cntR;
                            break;
                        }
                    }
                }
            }
        }
        return cntR !=0 ? "Radiant":"Dire";
    }
};
```

# analysis
>dota没有玩过，所以这个有点难办。不过仔细看了一下解法，发现并不难，如果能想到
用(i+n)%j的方式处理循环的话，就不是难题了。


# reference

[[LeetCode] Dota2 Senate 刀塔二参议院][1]

[1]: http://www.cnblogs.com/grandyang/p/7439222.html