#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int H[1501 * 1501]={0};
int n;

void upHeap(int index) {
    int temp = H[index];
    // 부모가 자식보다 큰 경우 계속 교체 (최소 힙 유지)
    while (index > 1 && temp < H[index / 2]) {
        H[index] = H[index / 2];
        index /= 2;
    }
    H[index] = temp;
}

void downHeap(int index) {
    int temp = H[index];
    int i = index;
    // 자식이 부모보다 작은 경우 교체
    while (i <= n / 2) {
        
        int j = i * 2;
        // 오른쪽 자식이 더 작으면 오른쪽 자식을 선택
        if (j + 1 <= n && H[j] < H[j + 1]) {
            j++;
        }
        // 부모가 자식보다 작으면 종료
        if (temp > H[j]) {
            break;
        }
        H[i] = H[j];
        i = j;
    }
    H[i] = temp;
}
int removeMax() {
	int max = H[1];
	H[1] = H[n];
	n--;
	downHeap(1);
	return max;
}

void buildHeap() {
    // 부모 노드들에 대해 downHeap 호출 (최소 힙으로 변환)
    for (int i = n / 2; i >= 1; i--) {
        downHeap(i);
    }
}

void rbuildHeap(int index) {
    if (index > n) {
        return;
    }
    // 왼쪽, 오른쪽 자식에 대해 먼저 재귀적으로 호출
    rbuildHeap(2 * index);
    rbuildHeap(2 * index + 1);
    // 현재 노드를 최소 힙으로 정렬
    downHeap(index);
}

void printHeap() {
    for (int i = 1; i <= n; i++) {
        printf(" %d", H[i]);
    }
    printf("\n");
}

int main() {
    int cnt;
    scanf("%d", &cnt);
    for (int i = 1; i <= cnt*cnt; i++) {
        scanf("%d", &H[i]);
        n++;
        
    }
    rbuildHeap(1);
    int res = 0;
    for (int i = 1; i <= cnt; i++) {
        res = removeMax();
        
    }
    printf("%d", res);

    return 0;
}