/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL || k == 0) {
        return head;
    }
    
    struct ListNode* temp = head;
    int len = 1;

    while(temp->next != NULL) {
        len++;
        temp = temp->next;
    }

    k = k % len;
    // if (k == 0) return head;

    temp->next = head;
    struct ListNode* newNode = head;
    for(int i = 0; i < len - k - 1; i++) {
        newNode = newNode->next;
    }

    struct ListNode* newHead = newNode->next;
    newNode->next = NULL;

    return newHead;
}
