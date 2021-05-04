#include "lists.h"
/**
 * is_palindrome - checks if palindrome
 * @head: head of node
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = *head;
	int array[5000];
	int len, j, i;

	if (!head)
		return (0);
	if (!*head || ((*head)->next == NULL))
		return (1);

	for (len = 0; temp2->next != NULL; len++)
	{
		temp2 = temp2->next;
	}
	for (i = 0; i <= len; i++)
	{
		array[i] = temp->n;
		temp = temp->next;
	}

	for (j = 0, len; j < len; j++, len--)
	{
		if (array[j] != array[len])
		{
			return (0);
		}
	}
	return (1);
}
