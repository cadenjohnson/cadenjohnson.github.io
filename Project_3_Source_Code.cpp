// This is a program to determine whether a string input is a valid IP address
// Caden Johnson  12/9/19

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define DELIM "."


int checkDigit(char *address_digit)
{
    while (*address_digit)
	{
        if (*address_digit >= '0' && *address_digit <= '9')
            ++address_digit;
        else
            return 0;
    }
    return 1;
}


int validateIP(char *ip_address)
{
    int NUM;
	int dot_counter = 0;
    char *ptr;
    if (ip_address == NULL)
        return 0;

	// Step One ***************************************
    ptr = strtok(ip_address, DELIM);
    if (ptr == NULL)
        return 0;

    while (ptr)
	{
		// Step 2 **************************************
        if (!checkDigit(ptr))
        {
            return 0;
		}

        NUM = atoi(ptr);
        if (NUM >= 0 && NUM <= 255)
		{
            ptr = strtok(NULL, DELIM);
            
            if (ptr != NULL)
                ++dot_counter;
        }
		else
		{
            return 0;
		}
    }

	// Step 3 ********************************************
    if (dot_counter != 3)
    {
        return 0;
	}
	else
	{
    return 1;
	}
}


int main() 
{ 
    char test[15]; 
    printf("Enter IP Address: ");
    gets(test);
    validateIP(test)? printf("Valid\n"): printf("Invalid\n");
    
    return 0; 
} 



    
    
