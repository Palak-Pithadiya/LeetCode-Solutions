#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
}Node;

Node* createNode(int data1) {
  Node* newNode = (Node*)malloc(sizeof(Node));
  if(newNode == NULL) {
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

void print(Node* head) {
  Node* temp = head;
  while(temp) {
    printf("%d ", temp->data);
    temp = temp->next;
  }
  printf("\n");
}

Node* deleteEle(Node* head, int val) {
  if(head == NULL) return NULL;
  if(head->data == val) {
    Node*temp = head;
    head = head->next;
    free(temp);
    return head;
  }

  Node* temp = head;
  Node* prev = NULL;

  while(temp != NULL) {
    if(temp->data == val){
        prev->next = temp->next;
        free(temp);
        break;
    }
    prev = temp;
    temp = temp->next;
  }

  return head;
}

int main() {
  int arr[] = {2, 3, 4, 5, 6};
  int size = sizeof(arr) / sizeof(arr[0]);
  Node* head = convertArr2LL(arr, size);
  int val = 3;
  head = deleteEle(head, val);
  print(head);
  
  return 0;
}
