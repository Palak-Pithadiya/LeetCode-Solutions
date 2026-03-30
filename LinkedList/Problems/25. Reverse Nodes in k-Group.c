/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseLL(struct ListNode* head) {
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

struct ListNode* getKthNode(struct ListNode* temp, int k) {
    k -= 1;
    while(temp != NULL && k > 0) {
        k--;
        temp = temp->next;
    }
    return temp;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if(head == NULL || k == 1) return head;

    struct ListNode* temp = head;
    struct ListNode* prevNode = NULL;

    while(temp) {
        struct ListNode* kthNode = getKthNode(temp, k);
        if(kthNode == NULL) {
            if(prevNode) {
                prevNode->next = temp;
            }
            break;
        }
        struct ListNode* nextNode = kthNode->next; 
        kthNode->next = NULL;
        reverseLL(temp);

        if(temp == head) {
            head = kthNode;
        }
        else {
            prevNode->next = kthNode;
        }
        
        prevNode = temp;
        temp = nextNode;
    }
    return head;
}
