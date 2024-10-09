#!/usr/bin/python3
"""
This module defines a Node class for a singly linked list and a
SinglyLinkedList class to manage the list.
"""


class Node:
    """
    This class represents a node in a singly linked list.
    Each node contains data and a pointer to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list.
              Defaults to None.

        Raises:
            TypeError: If data is not an integer or if next_node is not a Node.
        """
        self.data = data  # Use the setter to set the data
        self.next_node = next_node  # Use the setter to set the next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value  # Set the private attribute

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value  # Set the private attribute


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    It contains methods to insert nodes in sorted order and to print the list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None  # No setter for head

    def __str__(self):
        """Return a string representation of the list."""
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))  # Add each node's data
            current = current.next_node  # Move to the next node
        return "\n".join(result)  # Join all values with newline

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The data for the new node.
        """
        new_node = Node(value)  # Create a new node

        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse the list to find the insertion point
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node  # Set new_node's next
            current.next_node = new_node  # Insert the new node
