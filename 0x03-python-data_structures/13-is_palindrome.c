#include "lists.h"

/**
 * palindrome - function
 * @head: head list
 *
 * Description: recursive palindrome or not
 *
 * Return: 0 if it is not a plaindrome and 1 if otherwise
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head)):
}

/**
 * aux_palind - function
 * @head: head list
 * @end: end list
 *
 * Description: function to know if it is a palindrome
 *
 * Return: Always 0
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
