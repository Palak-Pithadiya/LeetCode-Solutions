struct ListNode* findPairsWithGivenSum(ListNode* head, int target) {
  if(head == NULL) return NULL;
  
  struct ListNode* start = head; 
  struct ListNode* last = head; 
  
  while(last->next != NULL) {
    last = last->next;
  }
  while(start != NULL && last != NULL && start != last && start->prev != last) {
    int sum = start->data + last->data;
    if(sum == target) {
      printf("[%d, %d]", start->data, last->data);
      start = start->next;
      last = last->prev;
    }
    else if(sum > target) {
      last = last->prev;
    }
    else {
      start = start->next;
    }
  }
  return NULL;
}
