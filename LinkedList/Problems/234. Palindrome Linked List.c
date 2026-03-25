/**
 * a for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    if(head == NULL || head->next == NULL) return true;

    struct ListNode* slow = head;
    struct ListNode* fast = head;

    while(fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* temp = slow->next;
    struct ListNode* prevNode = NULL;
    struct ListNode* nextNode = NULL;

    while(temp) {
        nextNode = temp->next;
        temp->next = prevNode;
        prevNode = temp; 
        temp = nextNode;
    }

    struct ListNode* f_half = head;
    struct ListNode* s_half = prevNode;
    while(s_half != NULL) {
        if(s_half->val != f_half->val) return false;
        f_half = f_half->next;
        s_half = s_half->next;
    }
    return true;
}
