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
    printf("\n");
}

// insertionSort
// as per Kormen text inspiration except they index at 1 ... why?
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

// mergeSort(low, end, length)
// merge(array, right, left, length)
// merge() makes copy of the left and right arrays
// O(n lg n)
void merge(int* A, int low, int middle, int high){
    return "now implemented";
}

void mergeSort(int* A, int low, int high){
    if(low < high){
        int middle = (low + high)/2;
        mergeSort(A, low, middle);
        mergeSort(A, middle + 1, high);
        merge(A, low, middle, high);
    } else {
        return;
    }
}

int main(){
    int A[] = {5, 2, 9, 7, 1, 3, 2, 6,};
    int B[] = {9, 7, 6, 5, 3, 2, 2, 1}; // insertion sort worst case

    /* int C[] = {} */
    /* int D[] = {} */
    
    /* insertionSort(A, 8); */
    /* insertionSort(B, 8); */
    mergeSort(A, 0, 8); 
    printArray(A, 8);
    /* printArray(B, 8); */
    
}
