#include <iostream>
#include <cmath>
#include <string.h>
using namespace std;

#define d = 256;

int robin(char pat[],char txt[],int q);

int robin(char pat[],char txt[],int q){
	int h=0;	
	int cur=0;
	int blast=0;
	int temp=0;
	
	int pat_len=strlen(pat);
	int txt_len=strlen(txt);
	
	for(int i=0;i<pat_len;i++){
		h += pat[i]*pow(q,i) ;
	}

	while(cur<txt_len){
		if(cur==0 || cur==txt_len-pat_len){
			for(int i=0;i<pat_len;i++){
				blast += txt[i+cur]*pow(q,i);
			}
		}
		else{
			blast=(temp-txt[cur-1])/q;
			blast= blast + (txt[cur+pat_len-1]*pow(q,(pat_len-1)));
		}		
		if(blast==h){
			cout<<"pattern exists in: "<<cur<<endl;
			break;
		}
		else{
			temp=blast;
			blast=0;
			cur +=1;
		}
	}
	if(cur==txt_len)
		cout<<"Pattern does not exist"<<endl;	
	return 0;
}

int main(int args,char** argv){
	char a[]="efx";
	char b[]="abcedef";
	robin(a,b,101);
	
}
