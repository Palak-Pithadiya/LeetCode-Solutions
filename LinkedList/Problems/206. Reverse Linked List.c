/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* temp = head;
    struct ListNode* prevNode = NULL;
    struct ListNode* nextNode = NULL;

    while(temp) {
        nextNode = temp->next;
        temp->next = prevNode;

        prevNode = temp;
        temp = nextNode;
    }
    return prevNode;
}
