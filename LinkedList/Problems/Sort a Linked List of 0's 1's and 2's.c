struct ListNode* sortList(struct ListNode* head) {
  if (head == NULL || head->next == NULL) return head;
  
  struct ListNode zeroDummy = {0, NULL};
  struct ListNode oneDummy = {0, NULL};
  struct ListNode twoDummy = {0, NULL};
  
  struct ListNode* zeroTail = &zeroDummy;
  struct ListNode* oneTail = &oneDummy;
  struct ListNode* twoTail = &twoDummy;
  
  struct ListNode* temp = head;
  while(temp) {
    if(temp->val == 0) {
      zeroTail->next = temp;
      zeroTail = zeroTail->next; 
    }
    else if(temp->val == 1) {
      oneTail->next = temp;
      oneTail = oneTail->next; 
    }
    else {
      twoTail->next = temp;
      twoTail = twoTail->next; 
    }
    temp = temp->next;
  }
  oneTail->next = twoDummy.next;
  zeroTail->next = oneDummy.next ? oneDummy.next : twoDummy.next;
  twoTail->next = NULL;

  return zeroDummy.next;
}
