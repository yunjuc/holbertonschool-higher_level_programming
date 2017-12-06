#include "lists.h"

/**
 * check_cycle - check if a linked list has cycle
 * @list: pointer to list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slower, *faster;

	if (list == NULL || list->next == NULL)
		return (0);

	slower = list;
	faster = list->next; 
	while (faster->next != NULL)
	{
		if (slower == faster)
			return (1);
		else if (faster->next == NULL)
			return (0);
		slower = slower->next;
		faster = faster->next->next;
	}
	return (0);
}
