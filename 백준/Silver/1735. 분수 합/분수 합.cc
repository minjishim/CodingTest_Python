#include <bits/stdc++.h>

using namespace std;

int A,B,C,D;
int Min=21e8;
int Max=0;
void init(){
	cin >> A >> B >> C >> D;
}
void solution(){
	int a = A*D + C*B;
	int b = B*D;

	Min = min(a,b);
	Max = max(a,b);

	while(Min != 0){
		int tmp = Min;
		Min = Max % Min;
		Max = tmp;
	}
	cout << a/Max << " " << b/Max << endl;
	
}
int main(){
	init();
	solution();

	return 0;
}
