# Linked List Implementation in Python

This Python script provides a basic implementation of a linked list, including methods for insertion, deletion, updating, and traversal.

## Table of Contents

- [Overview](#overview)
- [Node Class](#node-class)
- [LinkedList Class](#linkedlist-class)
- [Methods](#methods)
  - [Insertion](#insertion)
  - [Update](#update)
  - [Deletion](#deletion)
  - [Traversal](#traversal)
  - [Size](#size)
- [Usage](#usage)
- [Example](#example)

## Overview

This implementation consists of two classes:

1. **Node Class:** Defines a node containing data and a reference to the next node.

    ```python
    # Node class to create a node.
    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
    ```

2. **LinkedList Class:** Implements a linked list with various methods for manipulating the list.

    ```python
    # LinkedList class
    class LinkedList:
        def __init__(self) -> None:
            self.head = None
    ```

## Methods

### Insertion

- **Insert at the Beginning:**
  - Inserts a node with the specified data at the beginning of the list.

    ```python
    def insertAtBegin(self, data):
        # Implementation details...
    ```

- **Insert at a Specific Index:**
  - Inserts a node with the specified data at the given index.

    ```python
    def insertAtIndex(self, data, index):
        # Implementation details...
    ```

- **Insert at the End:**
  - Inserts a node with the specified data at the end of the list.

    ```python
    def insertAtEnd(self, data):
        # Implementation details...
    ```

### Update

- **Update Node:**
  - Updates the data of the node at the specified index with the given value.

    ```python
    def updateNode(self, val, index):
        # Implementation details...
    ```

### Deletion

- **Delete at the Beginning:**
  - Deletes the first node in the list.

    ```python
    def deleteNodeAtBegin(self):
        # Implementation details...
    ```

- **Delete at the End:**
  - Deletes the last node in the list.

    ```python
    def deleteNodeAtEnd(self):
        # Implementation details...
    ```

- **Delete at a Given Index:**
  - Deletes the node at the specified index.

    ```python
    def deleteNodeAtindex(self, index):
        # Implementation details...
    ```

- **Delete by Data:**
  - Deletes the node containing the specified data.

    ```python
    def deleteNodebyData(self, data):
        # Implementation details...
    ```

### Traversal

- **Print Linked List:**
  - Prints the elements of the linked list.

    ```python
    def printLL(self):
        # Implementation details...
    ```

### Size

- **Size of Linked List:**
  - Returns the size (number of nodes) in the linked list.

    ```python
    def sizeOfLL(self):
        # Implementation details...
    ```

## Usage

To use the linked list, create an instance of the `LinkedList` class and utilize its methods for various operations.

## Example

Here's a simple example demonstrating the usage of the linked list:

```python
# Example Usage
my_list = LinkedList()

my_list.insertAtEnd(1)
my_list.insertAtEnd(2)
my_list.insertAtEnd(3)

print("Linked List:")
my_list.printLL()

print("Size of Linked List:", my_list.sizeOfLL())