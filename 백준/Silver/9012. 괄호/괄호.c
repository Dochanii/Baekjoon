#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)
int top = -1;

void push(char stack[], char data) {

	if (top >= 1000) {
		printf("Stack FULL\n");
	}
	else {
		
		stack[++top] = data;
	}
}

char pop(char stack[]) {
	char temp;
	if (top == -1) {
		printf("Stack Empty\n");
	}
	else {
		temp = stack[top];
		top--;
		return temp;
	}

}



int main() {

	int n;

	char stack[1000];
	char inputString[1000];
	char ans[4];
	int flag = 0;

	scanf("%d", &n);
	//getchar();
	for (int i = 0; i < n; i++) {
		scanf("%s", inputString);
		getchar();
		flag = 0;
		
		for (int j = 0; j < strlen(inputString); j++) {
			
			if (inputString[j] == '(') {
				push(stack, inputString[j]);
			}
			else if (inputString[j] == ')') {
				if (top == -1) {
					strcpy(ans, "NO");
					flag = 1;
					break;
				}
				else {
					pop(stack);
				}
			}

		}
		if (top != -1) {
			strcpy(ans, "NO");
		}
		
		else if(flag == 0) {
			strcpy(ans, "YES");
		}
		printf("%s\n", ans);	
		
		top = -1;

	}


	return 0;
}



//6
//(())())
//(((()())()
//(()())((()))
//((()()(()))(((())))()
//()()()()(()()())()
//(()((())()(
	