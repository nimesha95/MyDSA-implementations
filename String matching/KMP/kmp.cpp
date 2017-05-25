#include <iostream>
#include <string.h>

using namespace std;

void preprocessing(char *pat,int *prefix,int m ){
	int len=0;
	prefix[0]=0;

	int i=1;
	while(i<m){
		if(pat[i] == pat[len]){
			len++;
			prefix[i]=len;
			i++;
		}
		else{
			if(len != 0){
				len=prefix[len-1];
			}
			else{
				prefix[i]=0;
				i++;
			}
		}
	}
}

void kmp(char *pat,char *txt){
	int m=strlen(pat);
	int prefix[m];
	int cur=0;

	preprocessing(pat,prefix,m);

	while(cur<m){
		
	}
}

int main(int args,char** argv){
	char pat[]="ababababca";
	char txt[]="affababa";
	return 0;
}
