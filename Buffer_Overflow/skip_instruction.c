#include<stdio.h>

void skip_function(int a, int b, int c)
{
	int *ret=NULL;
	char buffer[16];
	ret=(int *)(buffer+24);
	// (*ret)+=8;
}
void main()
{
	int x;
	x=0;
	skip_function(1,2,3);
	x=1;
	printf("value of x is %d\n",x);
}
