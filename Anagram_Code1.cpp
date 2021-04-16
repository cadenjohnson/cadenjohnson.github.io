// Caden Johnson - CSCI 301 - 03
// Project 1 - Due 9/1/2020
// This program will determine whether two input strings are anagrams
// and output its findings.

#include <string>
#include <iostream>
#include <ctype.h>
using namespace std;

bool Compare(string astring, string bstring)
{
	bool anagram = true;
	// Iterate through one of the strings
	for(int i=0; i<astring.length(); i++)
	{
		char c = astring.at(i);
		if(isalpha(c))
		{
			// Check if the character exists in the other string
			size_t exists = bstring.find(c);
			size_t lowerexists = bstring.find(tolower(c));
			if(exists == string::npos && lowerexists == string::npos)
			{
				anagram = false;
			}
		}
	}
	// Return whether or not the second string contains all of the same char's as the first
	return anagram;
}


int main()
{
	// initialize variables and obtain the input strings
	char a[60], b[60];
	bool atest, btest;
	cout << endl << "Enter first string: ";
	cin.get(a, 60);
	cin.get();
	cout << endl << "Enter second string: ";
	cin.get(b, 60);
	// Convert character arrays into string data type
	string astring(a);
	string bstring(b);
	
	// Call the compare function to compare the strings
	atest = Compare(astring, bstring);
	btest = Compare(bstring, astring);
	
	// Output the results of the comparisons
	if(atest && btest)
	{
		cout << endl << "The two strings ARE anagrams.";
	}
	else
	{
		cout << endl << "The two strings are NOT anagrams.";
	}
	
	return 0;
}
