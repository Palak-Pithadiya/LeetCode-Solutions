#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
}Node;

Node* createNode(int data1) {
  Node* newNode = (Node*)malloc(sizeof(Node));
  
  if (newNode == NULL) return NULL;
  newNode->data = data1;
  newNode->next = NULL;
  return newNode;
}

Node* convertAll2LL(int arr[], int size) {
  if (size == 0) return NULL;

  Node* head = createNode(arr[0]);
  Node* mover = head;

  for(int i = 1; i < size; i++) {
    Node* temp = createNode(arr[i]);
    mover->next = temp;
    mover = temp;
  }
  return head;
}

int print(Node* head){
  while(head != NULL) {
    printf("%d ", head->data);
    head = head->next;
  }
  return 0;
}

Node* removeHead(Node* head){
  if(head == NULL) return head;
  Node* temp = head;
  head = head->next;
  free(temp);
  return head;
}

int main() {
  int arr[] = {2, 3, 4, 5, 6};
  int size = sizeof(arr) / sizeof(arr[0]);
  Node* head = convertAll2LL(arr, size);
  head = removeHead(head);
  print(head);  
  return 0;
}
