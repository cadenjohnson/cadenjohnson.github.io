// Caden Johnson - CSCI 301 - 03
// Project 5 - Due 10/5/2020
// This project input an integer and output the integer's prime factors.
// Additionally, this program will implement an array based stack
// to store the factors and eventually output them in a decreasing order. 

#include <iostream>
using namespace std;

static const int CAPACITY = 15;
bool complete = false;

// stack class
class Stack
{
	private:
		int data[CAPACITY];
		int used;
		
	public:
		// Constructor
		Stack()
		{
			used = -1;
		}
		
		// Push
		void push(int entry)
		{
			if(used + 1 == CAPACITY)
			{
				cout << "ERROR : integer is too large, update CAPACITY" << endl;
			}
			else
			{
				used++;
				data[used] = entry;
			}
		}
		
		// Pop
		int pop()
		{
			if(used == -1)
			{
				cout << "ERROR : stack is empty" << endl;
				return -1;
			}
			else
			{
				int temp = data[used];
				return temp;
			}
		}
		
		// displays items in stack
		void showStack()
		{
			int temp;
			while(used >= 0)
			{
				temp = pop();
				if(used == 0)
				{
					cout << temp << endl;
				}
				else if(used > 0)
				{
					cout << temp << " x ";
				}
				used --;
				if(used == -1)
				{
					break;
				}
			}
		}
};


// function for finding all prime factors of integer
void findPrimes(int number, Stack stack)
{
	for(int i=2; i<=number; i++)
	{
		if(number%i == 0)
		{
			stack.push(i);
			if(i != number)
			{
				findPrimes((number/i), stack);
				break;
			}
		}
	}
	if(!complete)
	{
		stack.showStack();
		complete = true;
	}
	
}


// main function
int main()
{
	Stack stack;
	int entry = 1;
	while(entry != 0)
	{
		cout << "Enter a positive integer (0 to stop): ";
		cin >> entry;
		if(entry == 1)
		{
			cout << "Prime factors: 1 = 1" << endl;
		}
		else if(entry > 1)
		{
			findPrimes(entry, stack);
		}
		else if(entry < 0)
		{
			cout << "ERROR : invalid input" << endl;
		}
	}	
	
	return 0;
}









