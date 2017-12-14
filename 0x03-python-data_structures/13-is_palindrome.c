#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: double pointer to list head
 * Return: 0 if not a palindrome, 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0, count = 0, mid;
	listint_t *temp = *head, *ptr = *head;

	if (head == NULL || *head == NULL)
		return (0);

	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	if (count == 1 || count == 0)
		return (1);
	mid = count / 2;

	while (i <= mid)
	{
		temp = temp->next;
		i++;
	}
	if (count % 2 != 0)
		temp = temp->next;

	while (temp->next != NULL)
	{
		ptr = *head;
		for (i = 0; i < mid - 1; i++)
			ptr = ptr->next;
		if (ptr->n != temp->n)
			return (0);
		temp = temp->next;
		mid--;
	}
	return (1);
}
