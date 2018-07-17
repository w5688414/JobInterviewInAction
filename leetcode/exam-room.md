# problem
>In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:
```
Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student​​​​​​​ sits at the last seat number 5.
```
Note:

1. 1 <= N <= 10^9
2. ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
3. Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

# codes
```
class ExamRoom {
private:
    set<int> s;
    int n;
public:
    ExamRoom(int N) {
        n=N;
    }
    
    int seat() {
        int in_idx=0;
        if(s.size()==0){
            s.insert(0);
            return 0;
        }
        if(s.size()){
            int maxLen=0;
            if(!s.count(0)){ //0 没有被占用
                maxLen=*s.begin();
                in_idx=0;
            }
            int idx=0;
            auto begin=s.begin();
            auto end=s.end();
            while(begin!=end){  //记录上一个人的位置
                int len=(*begin-idx)/2;
                if(len>maxLen){
                    maxLen=len;
                    in_idx=(*begin+idx)/2;
                }
                idx=*begin;
                begin++;
            }
            //最后的位置没有被占
            if(!s.count(n-1)){
                int len=n-1-*s.rbegin();
                if(len>maxLen){
                    maxLen=len;
                    in_idx=n-1;
                }
            }
        }
        s.insert(in_idx);
        return in_idx;
    }
    
    void leave(int p) {
        s.erase(s.find(p));
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
```

# analysis
>
# reference
[855. Exam Room][1]

[1]: https://leetcode.com/problems/exam-room/discuss/148769/C++-solutions-Easy-to-understandbeat-98.90