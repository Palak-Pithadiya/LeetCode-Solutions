int countNodesInLoop(struct ListNode *head) {
  struct ListNode *slow = head;
  struct ListNode *fast = head;

  while(fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;

    if(slow == fast) {
      int cnt = 1;
      struct ListNode *temp = slow;
      while(temp->next != slow) {
        cnt++;
        temp = temp->next;
      }
      return cnt;
    }
  }
  return 0;
}
