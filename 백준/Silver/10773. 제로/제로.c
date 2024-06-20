#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)
int top = -1;

void push(int stack[], int data) {

	if (top >= 1000000) {
		return;
	}
	else {

		stack[++top] = data;
	}
}

int pop(int stack[]) {
	int temp;
	if (top == -1) {
		return;
	}
	else {
		temp = stack[top];
		top--;
		return temp;
	}

}

int main() {
	int n;
	scanf("%d", &n);
	int* stack = (int*)malloc(sizeof(int) * n);
	int num;
	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		if (num == 0) {
			pop(stack);
		}
		else
		push(stack, num);

		
	}
	
	int sum = 0;
	for (int i = 0; i <= top; i++) {
		sum += stack[i];
	}
	printf("%d", sum);
	free(stack);



	return 0;
}