// Caden Johnson - CSCI 301-03 - Due 9/29/2020
// Project 4 - Excersizing a Doubly-Linked List Class
// This project will be in two parts. There will be a class that implements
// a doubly-linked list where the nodes have a link to the next and previous nodes.
// The second part will be a program meant for client access to the class.

#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

struct Item
{
	public:
		char data;
		Item *next;
		Item *previous;
};

class List
{
	public:	
		Item *first;
		Item *last;
		
		// Constructor
		List()
		{
			first = NULL;
			last = NULL;
		}
		
		// Destructor
		~List(){}
		
		// checks to see if the list is empty
		bool empty()
		{
			if(first == NULL && last == NULL)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		
		// used to add items/nodes to the list
		void append(char entry)
		{
			Item *current = new Item();
			if(first == NULL && last == NULL)
			{
				current->data = entry;
				current->previous = NULL;
				current->next = NULL;
				first = current;
				last = current;
			}
			else
			{
				current->data = entry;
				current->previous = last;
				current->next = NULL;
				current->previous->next = current;
				last = current;
			}
		}
		
		// used to remove the last item/node from the list
		void remove_last()
		{
			last = last->previous;
			delete last->next;
			last->next = NULL;
		}
		
		void output_list()
		{
			Item *current;
			if(empty())
			{
				cout << "The list is empty" << endl << endl;
			}
			else
			{
				cout << "Printing List:" << endl;
				current = first;
				while(current != NULL)
				{
				cout << current->data;
				current = current->next;
				}
			}
		}
	
};



int main()
{
	List list;
	string sentence;
	char letter;
	int length=0, pounds=0;
	cout << "Enter a line of characters; # => delete the most recent character." << endl;
	cout << "->";
	cin >> sentence;
	for(int i=0; i < (sentence.length() + 1); i++)
	{
		letter = sentence[i];
		if(letter == '#' && length > pounds)
		{
			list.remove_last();
			pounds += 1;
		}
		else
		{
			list.append(letter);
			length += 1;
		}
	}
	cout << endl;
	list.output_list();
	
	return 0;
}













