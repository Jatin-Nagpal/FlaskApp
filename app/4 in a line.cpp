#include <bits/stdc++.h>
using namespace std;
#define f(i,x,n) for(int i=x;i<n;i++)

// Let Bot is 2 and User is 1
int n=8,m=8;
int a[16][16],sum=0;
int check()
{
	if(sum==64)
		return 1;
	f(i,0,n)
		f(j,0,m)
		{
			if(a[i][j]!=0&&a[i][j]==a[i][j+1]&&a[i][j+1]==a[i][j+2]&&a[i][j+2]==a[i][j+3])
				return a[i][j];
			if(a[i][j]!=0&&a[i][j]==a[i+1][j]&&a[i+1][j]==a[i+2][j]&&a[i+2][j]==a[i+3][j])
				return a[i][j];
			if(a[i][j]!=0&&a[i][j]==a[i+1][j+1]&&a[i+1][j+1]==a[i+2][j+2]&&a[i+2][j+2]==a[i+3][j+3])
				return a[i][j];
			if(a[i][j]!=0&&i-3>=0&&a[i][j]==a[i-1][j+1]&&a[i-1][j+1]==a[i-2][j+2]&&a[i-2][j+2]==a[i-3][j+3])
				return a[i][j];
		}
	return 0;
}
int32_t main()
{
	
	int turn=1;
	while(1)
	{
		if(check())
		{
			break;
		}
		f(i,0,n)
		{
			f(j,0,m)
			{
				cout<<a[i][j]<<" ";
			}
			cout<<'\n';
		}
		int ch;
		cin>>ch;
		ch--;
		int i=n-1;
		while(a[i][ch]!=0)
		{
			i--;
		}
		sum++;
		a[i][ch]=turn;
		turn =3-turn;
	}
	f(i,0,n)
	{
		f(j,0,m)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<'\n';
	}
	return 0;
}