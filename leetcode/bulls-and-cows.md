# problem
>You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.
Example 1:
```
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
```
Example 2:
```
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
```
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# codes
```
class Solution {
public:
    string getHint(string secret, string guess) {
        unordered_map<char,int> m;
        int bull=0;
        int cow=0;
        for(int i=0;i<secret.size();i++){
            if(guess[i]==secret[i]){
                bull++;
            }else{
                m[secret[i]]++;
            }
        }
        
        for(int i=0;i<guess.size();i++){
            if(m[guess[i]]&&guess[i]!=secret[i]){
                m[guess[i]]--;
                cow++;
            }
        }
        return to_string(bull)+"A"+to_string(cow)+"B";
    }
};
```

# analysis
>这道题用hash表，但hash表应该存secret和guess相应位置不等的数量。然后再遍历一遍统计cow的数量，然后输出。想明白了就很简单。


# reference
[[LeetCode] Bulls and Cows 公母牛游戏][1]

[1]: http://www.cnblogs.com/grandyang/p/4929139.html