#include <bits/stdc++.h>

using namespace std;

long long A,B;
long long Min;
long long Max;
void init(){
	cin >> A >> B;
	Min = min(A,B);
	Max = max(A,B);

	//cout << Min << " " << Max << endl;
}
void solution(){
	while(Min != 0){
		long long tmp = Min;
		Min = Max % Min;
		Max = tmp;
	}

	cout << Max*(A/Max)*(B/Max) << endl;
	
}
int main(){
	init();
	solution();

	return 0;
}
