#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;  // Store next node
        current->next = prev;  // Reverse current node's pointer
        prev = current;        // Move prev and current one step forward
        current = next;
    }

    return prev;  // New head of the reversed list
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;  // An empty list or a single node is a palindrome

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half;
    listint_t *prev_of_slow = NULL;

    // Find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    // Handle odd-sized lists
    if (fast != NULL) 
    {
        second_half = slow->next;  // Skip the middle element
    } 
    else 
    {
        second_half = slow;  // For even-sized lists
    }

    // Reverse the second half
    second_half = reverse_list(second_half);
    listint_t *first_half = *head;

    // Compare the two halves
    int result = 1;  // Assume it's a palindrome
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            result = 0;  // Not a palindrome
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the original list (optional)
    second_half = reverse_list(second_half);
    if (prev_of_slow != NULL)
    {
        prev_of_slow->next = second_half;
    }

    return result;  // Return whether it's a palindrome
}
