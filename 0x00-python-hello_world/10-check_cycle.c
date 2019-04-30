#include "lists.h"

/**
 * check_cycle - checks for possible loop in a linked list.
 * @list: pointer to the head of linked list
 * Return: 0 if no loop, 1 if loop
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *slow;

	head = list;
	slow = list;

	while(slow && head->next && head->next->next)
	{
		head = head->next->next;
		slow = slow->next;

		if (head == slow)
			return (1);
	}
	return (0);
}
