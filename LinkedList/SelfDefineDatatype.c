#include <stdio.h>
#include <stdlib.h>

// In C, we define a struct and usually use a typedef for easier usage
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Since C doesn't have constructors, we create a helper function
Node* createNode(int data1, Node* next1) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        return NULL; // Handle memory allocation failure
    }
    newNode->data = data1;
    newNode->next = next1;
    return newNode;
}

int main() {
    // C uses standard arrays instead of vectors
    int arr[] = {2, 5, 8, 7};
    
    // Creating the node using our helper function
    Node* y = createNode(arr[0], NULL);
    
    // Printing the memory address (equivalent to 'cout << y')
    // Use %p for pointer addresses
    printf("%p\n", (void*)y);
    
    // Don't forget to free memory in C!
    free(y);
    
    return 0;
}