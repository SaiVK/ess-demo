#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int reveal_secret(char* name){
    printf ("\nCongratz %s\n", name);
    return 0;
}

int process(){
    char input_otp[4];
    char otp[4];
    char name[10];

	int fd = open("/dev/urandom", O_RDONLY);
	if(fd==-1) exit(-1);
	if(read(fd, &otp, 3)!=3) exit(-1);
	close(fd);

    printf("Enter username \n");
    fgets(name, sizeof(name), stdin);

    printf("Enter OTP (max:3 characters)\n");
    gets(input_otp);

    input_otp[3] = '\0';
    otp[3] = '\0';

    printf("Actual OTP : %4s\n", otp);
    printf("Input  OTP : %4s\n", input_otp);

    if(strcmp(input_otp, otp) == 0){
        reveal_secret(name);
    }
    else {
        printf("Oops!! Try again\n");
    }
    return 0;
}

int main(){
    process();
    printf("\nDone\n");
    return 0;
}