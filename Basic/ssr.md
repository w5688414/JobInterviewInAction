#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    cin>>n;
    int num;
    vector<int> s1;
    for(int i=0;i<n;i++){
    	cin>>num;
        s1.push_back(num);
    }  
    for(int i=0;i<s1.size();i++){
    	int count=0;
        int temp=10;
        for(int j=1;j<=s1[i];j++){
            int t=j;
        	while(t/temp!=0){
             count++;
                t=t/temp;
            }
            count++;
        }
        cout<<count<<endl;
    }
    return 0;
   
}