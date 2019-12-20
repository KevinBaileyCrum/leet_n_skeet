// sorting.c
// various sorting algorithms in C
//
// So what fun is doing LeetCode?  Sometimes not too much.  I thought 
// to myself, 'I want to get better at C and I want to revisit old 
// fundamentals'.  Therefore I thought, lets do some sorts in C!

#include<stdio.h>

void printArray(int* A, int length){
    for(int i=0; i<length; ++i){
        printf("%d\n", A[i]);
    }
}

// insertionSort
// as per Kormen text inspiration
// O(n^2)
void insertionSort(int* A, int length){
    for(int i=1; i<length; ++i){
        int j = i - 1;
        int key = A[i];
        while(j>=0 && (A[j] < key)){
            A[j+1] = A[j];
            --j;
        }
        A[j+1] = key; 
    }
}

int main(){
    int A[] = {5, 2, 9, 7, 1, 3, 2, 6};
    /* int B[] = { */
    insertionSort(A, 8);
    printArray(A, 8);
}
