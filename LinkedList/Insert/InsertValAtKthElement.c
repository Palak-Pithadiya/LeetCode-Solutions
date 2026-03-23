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

Node* insertingKthEle(Node* head, int k, int val) {
  if(head == NULL) {
    if(k == 1) return createNode(val);
    else return NULL;
  }

  if(k == 1) {
    Node* temp = createNode(val);
    temp->next = head;
    return temp;
  }

  Node* temp = head;
  int cnt = 0;
  while(temp != NULL)  {
    cnt++;
    if(cnt == k-1) {
      Node* newNode = createNode(val);
      newNode->next = temp->next;
      temp->next = newNode;
      break;
    }
    temp = temp->next;
  }
  return head;
}

int main() {
  int arr[] = {2, 3, 4, 5, 6};
  int size = sizeof(arr) / sizeof(arr[0]);
  Node* head = convertArr2LL(arr, size);
  int k = 2;
  head = insertingKthEle(head, k, 10);
  print(head);
  
  return 0;
}
