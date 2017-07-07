#include <stdio.h>

struct node_t {
	int val;
	struct node_t *next;
};
typedef struct node_t node;

node *reverse(node* initHead) {
	node *cur = initHead;
	node *last = NULL;
	while (cur != NULL) {
		node *savedNext = cur->next;
		cur->next = last;
		last = cur;
		cur = savedNext;
	}
	return last;
}

void printLL(node* head) {
	node* cur = head;
	do {
		printf("%d ", cur->val);
		cur = cur->next;
	} while (cur != NULL);
	printf("\n");
}

int main() {
	node a;
	node b;
	node c;
	node d;
	a.val = 10;
	b.val = 20;
	c.val = 30;
	d.val = 40;
	a.next = &b;
	b.next = &c;
	c.next = &d;
	d.next = NULL;
	
	printLL(&a);
	//printf("Reversing.\n");
	node* newHead = reverse(&a);
	//printf("Should be 40, 30, 20, 10.");
	printLL(newHead);
}
