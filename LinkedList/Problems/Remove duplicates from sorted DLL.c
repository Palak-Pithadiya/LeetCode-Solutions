struct ListNode* removeDuplicates(struct ListNode* head){
  if(head == NULL || head->next == NULL) return head;
  struct ListNode* temp = head;

  while(temp != NULL) {
    if(temp->data == temp->next->data) {
      struct ListNode* duplicate = temp->next;

      temp->next = duplicate->next;
      if(duplicate->next != NULL) {
        duplicate->next->prev = temp;
      }
      free(duplicate);
    }
    else {
      temp = temp->next;
    }
  return head;
}
