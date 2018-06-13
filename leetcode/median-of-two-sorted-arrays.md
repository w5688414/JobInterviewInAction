# problem
>There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


# codes
```
class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if(m==0&&n==1){
            return B[0];
        }
        if(m==1&&n==0){
            return A[0];
        }
        if(m==0){
            return n%2==0 ? (double)(B[n/2]+B[n/2-1])/2:B[n/2];
        }
        if(n==0){
            return m%2==0 ? (double)(A[m/2]+A[m/2-1])/2:A[m/2];
        }
        int s1=0;
        int d1=n-1;
        int m1;
        int m2;
        int s2=0;
        int d2=n-1;
        while(s1!=d1||s2!=d2){
            m1=(s1+d1)/2;
            m2=(s2+d2)/2;
            if(A[m1]==B[m2]){
                if((m+n)%2==0){
                    return (double)(A[m1]+A[m1+1])/2;

                }
                return A[m1];
            }
            if(A[m1]<B[m2]){
                if((s1+d1)%2==0){
                    s1=m1;
                    d2=m2;
                }else{
                    s1=m1+1;
                    d2=m2;
                }
            }else{
                if((s2+d2)%2==0){
                    d1=m1;
                    s2=m2;
                }else{
                    d1=m1;
                    s2=m2+1;
                }
            }
        }
        return A[s1]<B[s2] ? A[s1]:B[s2];
    }
};

```

```
class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if(m==0&&n==1){
            return B[0];
        }
        if(m==1&&n==0){
            return A[0];
        }
        if(m==0){
            return n%2==0 ? (double)(B[n/2]+B[n/2-1])/2:B[n/2];
        }
        if(n==0){
            return m%2==0 ? (double)(A[m/2]+A[m/2-1])/2:A[m/2];
        }
       vector<int>a{A,A+m};
       vector<int> b {B,B+n};
       a.insert(a.begin(),b.begin(),b.end());
       sort(a.begin(),a.end());
       int size=a.size();
       return size%2==0? (double) (a[size/2]+a[size/2-1])/2 :(double) a[size/2];
    }
};
```

```
class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int total=m+n;
        if(total%2==1){
            return findKth(A,m,B,n,total/2+1);
        }else{
            return (findKth(A,m,B,n,total/2)+
                findKth(A,m,B,n,total/2+1))/2;
        }
    }
    double findKth(int A[], int m, int B[], int n,int k){
        //always assume that m is equal or smaller than n 
        if(m>n){
            return findKth(B,n,A,m,k);
        }
        if(m==0){
            return B[k-1];
        }
        if(k==1){
            return min(A[0],B[0]);
        }
        //divide k into two parts 
        int pa=min(k/2,m);
        int pb=k-pa;
        if(A[pa-1]<B[pb-1]){
            return findKth(A+pa,m-pa,B,n,k-pa);
        }else if(A[pa-1]>B[pb-1]){
            return findKth(A,m,B+pb,n-pb,k-pb);
        }else{
            return A[pa-1];
        }
    }
      
       
};
```
```
// brute force
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()==0){
            return medianArray(nums2);
        }
        if(nums2.size()==0){
            return medianArray(nums1);
        }
        vector<double> nums3;
        int m=nums1.size()+nums2.size();
        int mid=m/2;
        int flag=!(m%2);
        int n1=0;
        int n2=0;
        for(int i=0;i<m;i++){
            double a= n1<nums1.size() ? nums1[n1]:INT_MAX;
            double b=n2<nums2.size() ? nums2[n2]:INT_MAX;
            if(a<b){
                nums3.push_back(a);
                n1++;
            }else{
                nums3.push_back(b);
                n2++;
            }
            if(i==mid){
                break;
            }
        }
        return (nums3[mid]+nums3[mid-flag])/2.0;
        
    }
    double medianArray(vector<int>& nums){
        int n=nums.size();
        if(n%2==1){
            return nums[n/2];
        }else{
            return (nums[n/2]+nums[n/2-1])/2.0;
        }
    }
};
```

# analysis
>归并排序+求中位数，不过需要O(m+n)的空间复杂度。另一种方法我还是每多看明白，用了递归的思路，我也写不出来，拿出来观摩一下，这是符合条件的最优解。
对于一个长度为n的已排序数列a，若n为奇数，中位数为a[n / 2 + 1] , 
    若n为偶数，则中位数(a[n / 2] + a[n / 2 + 1]) / 2
    如果我们可以在两个数列中求出第K小的元素，便可以解决该问题
    不妨设数列A元素个数为n，数列B元素个数为m，各自升序排序，求第k小元素
    取A[k / 2] B[k / 2] 比较，
    如果 A[k / 2] > B[k / 2] 那么，所求的元素必然不在B的前k / 2个元素中(证明反证法)
    反之，必然不在A的前k / 2个元素中，于是我们可以将A或B数列的前k / 2元素删去，求剩下两个数列的
    k - k / 2小元素，于是得到了数据规模变小的同类问题，递归解决
    如果 k / 2 大于某数列个数，所求元素必然不在另一数列的前k / 2个元素中，同上操作就好。

- brute force
最后一个解法，就是常规的归并排序的变体，与归并排序不一样的是，我们只归并到mid位置，就不往下归并了，由于归并排序需要数组，因此空间复杂度为O((m+n)/2)，时间复杂度为O(m+n)

# reference
[[编程题]median-of-two-sorted-arrays][1]
[leetcode之 median of two sorted arrays][2]
[《LeetBook》leetcode题解(4): Median of Two Sorted Arrays[H]——两个有序数组中值问题][3]

[1]: https://www.nowcoder.com/questionTerminal/82c11b9392b14f3abfbf257f79a76025
[2]: https://blog.csdn.net/yutianzuijin/article/details/11499917/
[3]: https://blog.csdn.net/hk2291976/article/details/51107543
