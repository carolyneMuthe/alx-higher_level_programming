#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next; // store next node
        current->next = prev; // reverse current node's pointer
        prev = current;       // move prev and current one step forward
        current = next;
    }

    return prev; // new head of the reversed list
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half;
    listint_t *prev_of_slow = NULL;
    int result = 1; // assume it's a palindrome

    // Step 1: Find the middle of the list
    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_of_slow = slow;
            slow = slow->next;
        }

        // Step 2: Reverse the second half of the list
        second_half = slow; // slow is now at the middle
        prev_of_slow->next = NULL; // terminate first half
        second_half = reverse_list(second_half); // reverse second half

        // Step 3: Compare the two halves
        listint_t *first_half = *head;
        while (second_half != NULL)
        {
            if (first_half->n != second_half->n)
            {
                result = 0; // not a palindrome
                break;
            }
            first_half = first_half->next;
            second_half = second_half->next;
        }

        // step 4: Restore the list (not necessary for this task)
        // second_half = reverse_list(second_half); // restore original order
        // prev_of_slow->next = second_half; // reconnect the first half
    }

    return result; // return whether it's a palindrome
}
