#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
}Node;

Node* createNode(int data1) {
  Node* newNode = (Node*)malloc(sizeof(Node));
  if (newNode == NULL) {
    return NULL;
  }
  newNode->data = data1;
  newNode->next = NULL;
  return newNode;
}

Node* convertArr2LL(int arr[], int size) {
  if(size == 0) return NULL;
  
  Node* head = createNode(arr[0]);
  Node* mover = head;
  
  for(int i = 1; i < size; i++) {
    Node* temp = createNode(arr[i]);
    mover->next = temp;
    mover = temp;
  }
  return head;
}

int main() {
  int arr[] = {2, 3, 4, 7, 8};
  int size = sizeof(arr) / sizeof(arr[0]);
  
  Node* head = convertArr2LL(arr, size);
  Node* temp = head;
  
  while(temp) {
    printf("%d ", temp->data);
    temp = temp->next;
  }
  return 0;
}
