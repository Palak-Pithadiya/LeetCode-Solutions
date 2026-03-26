/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *head1, struct ListNode *head2) {
    if(head1 == NULL || head2 == NULL) {
        return NULL;
    }
    struct ListNode* t1 = head1;
    struct ListNode* t2 = head2;

    while(t1 != t2) {
        t1 = (t1 == NULL) ? head2 : t1->next;
        t2 = (t2 == NULL) ? head1 : t2->next;
    }   
    return t1;
}
