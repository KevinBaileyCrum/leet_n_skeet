#include <stdbool.h>
#include <stdio.h>

/* Definition for singly-linked list. */
typedef struct ListNode {
   int val;
   struct ListNode *next;
} ListNode;

bool hasCycle(ListNode head) {
   return false;
}

void createList(ListNode* head, int* array, int length){
   printf("in funct\n");
   for(int i=0; i<length; i++){
      printf("i: %d\n", i);
      printf("head->val: %d", head->val);
      /* head->val = array[i]; */
      /* head->next = NULL; */ 
      /* head = head->next; */ 
   }
}

int main() {
   int arr1[] = {3,2,0,-4,1};
   int arr2[] = {1,2,0};
   ListNode* L1 = NULL;
   ListNode* L2 = NULL;

   createList(L1, arr1, 5);
   createList(L2, arr2, 3);
}
