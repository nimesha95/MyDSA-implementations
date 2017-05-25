#include <iostream>
using namespace std;
int arr[128];

void calc_last(string pattern);
int last(char ltr);

void calc_last(string pattern){
	for(int i=0;i<128;i++){
		arr[i]=-1;
	}
	for(int i=pattern.length()-1;i>=0;i--){
		if(arr[(int)pattern[i]]==-1){
			arr[(int)pattern[i]]=i;
		}
	}
}

int last(char ltr){
	int num=(int) ltr;
	return arr[num];
}
