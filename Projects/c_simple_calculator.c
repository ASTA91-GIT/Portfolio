#include <stdio.h>
#include <stdlib.h>

// Function declarations
void displayMenu();
float add(float a, float b);
float subtract(float a, float b);
float multiply(float a, float b);
float divide(float a, float b);
void clearScreen();

int main() {
    float num1, num2, result;
    char operator;
    int choice;
    char continue_calc = 'y';
    
    printf("=== Simple Calculator ===\n");
    printf("Welcome to the Calculator!\n\n");
    
    while (continue_calc == 'y' || continue_calc == 'Y') {
        // Display menu
        displayMenu();
        
        // Get user choice
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);
        
        // Validate choice
        if (choice < 1 || choice > 5) {
            printf("Invalid choice! Please enter a number between 1 and 5.\n\n");
            continue;
        }
        
        // Exit if choice is 5
        if (choice == 5) {
            printf("Thank you for using the calculator!\n");
            break;
        }
        
        // Get two numbers
        printf("Enter first number: ");
        scanf("%f", &num1);
        printf("Enter second number: ");
        scanf("%f", &num2);
        
        // Perform calculation based on choice
        switch (choice) {
            case 1:
                result = add(num1, num2);
                operator = '+';
                break;
            case 2:
                result = subtract(num1, num2);
                operator = '-';
                break;
            case 3:
                result = multiply(num1, num2);
                operator = '*';
                break;
            case 4:
                if (num2 == 0) {
                    printf("Error: Division by zero is not allowed!\n\n");
                    continue;
                }
                result = divide(num1, num2);
                operator = '/';
                break;
            default:
                printf("Invalid choice!\n");
                continue;
        }
        
        // Display result
        printf("\nResult: %.2f %c %.2f = %.2f\n\n", num1, operator, num2, result);
        
        // Ask if user wants to continue
        printf("Do you want to perform another calculation? (y/n): ");
        scanf(" %c", &continue_calc);
        printf("\n");
    }
    
    return 0;
}

// Function to display the menu
void displayMenu() {
    printf("Available Operations:\n");
    printf("1. Addition (+)\n");
    printf("2. Subtraction (-)\n");
    printf("3. Multiplication (*)\n");
    printf("4. Division (/)\n");
    printf("5. Exit\n");
    printf("------------------------\n");
}

// Function to add two numbers
float add(float a, float b) {
    return a + b;
}

// Function to subtract two numbers
float subtract(float a, float b) {
    return a - b;
}

// Function to multiply two numbers
float multiply(float a, float b) {
    return a * b;
}

// Function to divide two numbers
float divide(float a, float b) {
    return a / b;
}

// Function to clear screen (cross-platform)
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}
