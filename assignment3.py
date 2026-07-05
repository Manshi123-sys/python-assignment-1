#include <stdio.h>

int main()
{
    // -----------------------------
    // Program 1: Grade Calculator
    // -----------------------------
    int s1, s2, s3, s4, s5, total;
    float percentage;

    printf("===== PROGRAM 1 : GRADE CALCULATOR =====\n");

    printf("Enter marks of Subject 1: ");
    scanf("%d", &s1);

    printf("Enter marks of Subject 2: ");
    scanf("%d", &s2);

    printf("Enter marks of Subject 3: ");
    scanf("%d", &s3);

    printf("Enter marks of Subject 4: ");
    scanf("%d", &s4);

    printf("Enter marks of Subject 5: ");
    scanf("%d", &s5);

    total = s1 + s2 + s3 + s4 + s5;
    percentage = total / 5.0;

    printf("\nTotal Marks = %d", total);
    printf("\nPercentage = %.2f%%\n", percentage);

    if (percentage >= 60)
        printf("Grade = A\n");
    else if (percentage >= 50)
        printf("Grade = B\n");
    else if (percentage >= 40)
        printf("Grade = C\n");
    else if (percentage >= 33)
        printf("Grade = D\n");
    else
        printf("Result = Fail\n");

    // -----------------------------
    // Program 2: Multiplication Table
    // -----------------------------
    int num, i;

    printf("\n\n===== PROGRAM 2 : TABLE =====\n");

    printf("Enter a number between 2 and 50: ");
    scanf("%d", &num);

    if (num >= 2 && num <= 50)
    {
        printf("\nTable of %d\n", num);

        for (i = 1; i <= 10; i++)
        {
            printf("%d x %d = %d\n", num, i, num * i);
        }
    }
    else
    {
        printf("Number is not in range (2 to 50).\n");
    }

    // -----------------------------
    // Program 3: Palindrome Number
    // -----------------------------
    int number, original, reverse = 0, remainder;

    printf("\n===== PROGRAM 3 : PALINDROME NUMBER =====\n");

    printf("Enter a number: ");
    scanf("%d", &number);

    original = number;

    while (number != 0)
    {
        remainder = number % 10;
        reverse = reverse * 10 + remainder;
        number = number / 10;
    }

    if (original == reverse)
        printf("%d is a Palindrome Number.\n", original);
    else
        printf("%d is NOT a Palindrome Number.\n", original);

    return 0;
}
