struct ListNode* deleteAllOccurrences(struct ListNode* head, int target) {
  struct ListNode* temp = head;
  while(temp != NULL) {
    if(temp->data == target) {
      struct ListNode* accuredNode = temp;
  
      if(temp->prev != NULL) {
        temp->prev->next = temp->next;
      }
      else{
        head = temp->next;
      }
      if(temp->next != NULL) {
        temp->next->prev = temp->prev;
      }
      temp = temp->next;
      free(accuredNode);
    } else {
      temp = temp->next;
    }
  }
  return head;
}  
