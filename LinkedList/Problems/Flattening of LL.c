// Structure of LinkedList
typedef struct ListNode {
  int data;
  struct ListNode* next;
  struct ListNode* child;
}

struct ListNode* merge2Head(struct ListNode* l1, struct ListNode* l2) {
  struct ListNode dummy;
  struct ListNode* res = &dummy;
  dummy.child = NULL;

  while(l1 != NULL && l2 != NULL) {
    if(l1->data < l2->data) {
      res->child = l1;
      res = l1;
      l1 = l1->child;
    }
    else {
      res->child = l2;
      res = l2;
      l2 = l2->child;
    }
    res->next = NULL;
  }
  
  if(l1) {
    res->child = l1;
  }
  else {
    res->child = l2;
  }

  if (res->child) res->child->next = NULL;
  return dummy.child;
}

// Main Function
struct ListNode* flattenLinkedList(struct ListNode* head) {
  if(head == NULL || head->next == NULL) {
    return head;
  }
  struct ListNode* mergeHead = flattenLinkedList(head->next);
  head->next = NULL;
  return merge2Head(head, mergeHead);
}
