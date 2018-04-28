#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
    int M,N;
    cin>>M>>N;
    string s;
    vector<vector<int>> matrix;
    bool 
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            cin>>s;
            int num=0;
            vector<int> ans;
            for(int i=0;i<s.size();i++){
                if(s[i]>='0'&&s[i]<='9'){
                    int temp=s[i]-'0';
                    num=num*10+temp;
                }else if(s[i]==' '){
                    ans.push_back(num);
                    num=0;
                }else if(s[i]=='-'||s[i]=='+'){
                    flag=true;
                }
            }
        }
    }
    return 0;
}