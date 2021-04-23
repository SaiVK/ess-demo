#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int process(){
    char input[16];
    
    printf("\nEnter input:\n");
    gets(input);
    printf("Hello %s\n", input);
    printf("Today's date is : \n");
    system("date");
    return 0;
}

int main(){
    process();
    return 0;
}