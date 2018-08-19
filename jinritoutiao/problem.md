#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

vector<vector<int>> dirs={{-1,0},{1,0},{0,-1},{0,1},{-1,1},{1,-1},{1,1},{-1,-1}};
int res=0;

void solve(vector<vector<int>>& mat,int& count,int i,int j){
    int m=mat.size();
    int n=mat[0].size();
    if(mat[i][j]==0){
        return ;
    }
    count++;
    mat[i][j]=0;
    for(auto dir:dirs){
        int x=i+dir[0];
        int y=j+dir[1];
        if(x<=0||x>=m||y<0||y>=n){
            continue;
        }
        solve(mat,count,x,y);
    }
}

int main(){
    vector<int> v1;
    string s;
    cin>>s;
    stringstream sstr(s);
    string a;
    int M,N;
    getline(sstr,a,',');
    M=stoi(a);
    getline(sstr,a,',');
    N=stoi(a);
//    cout<<M<<N<<endl;
    vector<vector<int>> mat(M,vector<int>(N,0));
    for(int i=0;i<M;i++){
        cin>>s;
        stringstream t(s);
        int j=0;
        while(getline(t, a, ',')){
            mat[i][j]=stoi(a);
            j++;
        }
    }
    int t=0;
    
    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(mat[i][j]==1){
                int count=0;
                t++;
                solve(mat,count,i,j);
                res=max(res,count);
            }
        }
    }
    cout<<t<<","<<res<<endl;
    return 0;
}