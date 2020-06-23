#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - dulces sueños
 * Return: 0 for success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main function of program
 * Return: 0 for success
 */
int main(void)
{
	int i = 0;
	int pid;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0) /*the child was created*/
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
		{
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
