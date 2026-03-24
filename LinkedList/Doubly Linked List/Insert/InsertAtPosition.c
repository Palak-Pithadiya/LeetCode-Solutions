#include <stdio.h>
#include <stdlib.h>

// structure
typedef struct Node{
  int data;
  struct Node* next;
  struct Node* prev;
}Node;

Node* convertArr2DLL(int arr[], int size) {
  if(size == 0) return NULL;
  Node* head = (Node*)malloc(sizeof(Node));
  head->data = arr[0];
  head->prev = NULL;
  head->next = NULL;
  
  Node* mover = head;

  for(int i = 1; i < size; i++) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->data = arr[i];
    
    mover->next = temp;
    temp->prev = mover;
    temp->next = NULL;
    mover = temp;
  }
  return head;
}

Node* printForward(Node* head) {
  Node* temp = head;
  while(temp) {
    printf("%d ",temp->data);
    temp = temp->next;
  }
  printf("\n");
}

Node* printBackward(Node* head) {
  if(head == NULL) return NULL;

  // Go to the tail
  Node* temp = head;
  while(temp->next != NULL) {
    temp = temp->next;
  }

  // Traverse backward using 'prev'
  while(temp) {
    printf("%d ", temp->data);
    temp = temp->prev;
  }
  printf("\n");
}

Node* insertAtPos(Node* head, int k, int val) {
  if(head == NULL) {
    if(k == 1) {
      Node* newNode = (Node*)malloc(sizeof(Node));
      newNode->data = val;
      newNode->next = NULL;
      newNode->prev = NULL;
      return newNode;
    }
    return NULL;
  }

  if(k == 1) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = head;
    newNode->prev = NULL;
    head->prev = newNode;
    return newNode;
  }
  Node* temp = head;
  int cnt = 0;
  while(temp != NULL) {
    cnt++;
    if(cnt == k-1) break;
    temp = temp->next;
  }  
  if(temp == NULL) return head;
  Node* newNode = (Node*)malloc(sizeof(Node));
  newNode->data = val;
  Node* nextNode = temp->next;  
  
  newNode->next = nextNode;
  newNode->prev = temp;
  temp->next = newNode;

  if(nextNode != NULL) {
    nextNode->prev = newNode;
  }
  return head;
}

int main() {
  int arr[] = {2, 3, 4, 5};
  int size = sizeof(arr) / sizeof(arr[0]);
  Node* head = convertArr2DLL(arr, size);
  head = insertAtPos(head, 3, 100);
  printForward(head);
  return 0;
}
