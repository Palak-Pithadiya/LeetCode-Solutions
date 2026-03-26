/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int helper(struct ListNode *temp) {
  if(temp == NULL) {
    return 1;
  }
  struct ListNode* carry = helper(temp->next);
  temp->data = temp->data + carry;
  if(temp->data < 10) {
    return 0;
  }
  temp->data = 0;
  return 1;
}

struct ListNode *addOne(struct ListNode *head) {
  if(head == NULL) {
      return 1;
  }
  struct ListNode* carry = helper(temp->next);
  if (carry == 1) {
    struct ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->data = carry;
    newNode->next = head;
    return newNode;
  }
  return head;
}
