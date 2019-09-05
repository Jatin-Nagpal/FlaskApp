#include <bits/stdc++.h>
using namespace std;
#define f(i,x,n) for(int i=x;i<n;i++)

// Let Bot is 2 and User is 1
int n=8,m=8;
int la;
int a[16][16],sum=0;
array <int,8> b;
int check()
{
	if(sum==64)
		return 3;
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
	cout<<"Enter 1 if u want to play first\n";
	int turn;
	cin>>turn;
	if(turn!=1)
		turn=2;
	cout<<"Enter the difficulty level starting from 0\n";
	f(i,0,m)
		b[i]=n-1;
	cin>>la;
	while(1)
	{
		int won=check();
		if(won)
		{
			if(won==3)
				cout<<"It's a draw\n";
			else if(won==2)
				cout<<"Bot won\n";
			else
				cout<<"User won\n";
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
			int flag=0;
			if(b[ch]<0)
			{
				cout<<"Wrong Move, the column is already filled, Enter a different move\n";
				continue;
			}
			sum++;
			a[b[ch]][ch]=turn;
			b[ch]--;
		
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