// Choyce Reynolds
// 10/19/2025

// I wanted C++ to handle displaying the menue and calling logic from python in order to display the information based on user input

#include <iostream>
#include <string>
#include <cstdlib> 

using namespace std;

// Displays the menu where users make their selections
void displayMenu() {
    cout << "***********************************" << endl;
    cout << "||     Corner Grocer Items       ||" << endl;
    cout << "***********************************" << endl;
    cout << "Please make a selection from the following options:" << endl;
    cout << "1. Count all items" << endl;
    cout << "2. Count one item" << endl;
    cout << "3. Show histogram" << endl;
    cout << "4. Exit menu" << endl;
    cout << "Enter your selection here: ";
}

int main() {
    int input;
    string item;

    // This loop will continue until the user exits the menu by entering 4
    do {
        displayMenu();
        cin >> input;

        switch (input) {
        case 1:
            system("python CornerGrocerCode.py all"); // Calls all items with their quantities from the python file
            break;
        case 2:
            cout << "Enter item name: ";
            cin >> item;
            system(("python CornerGrocerCode.py one " + item).c_str()); // Calls one item and its quantity from the python file
            break;
        case 3:
            system("python CornerGrocerCode.py histogram"); // Calls the histogram from the python file
            break;
        case 4:
            cout << "Exiting menu" << endl; // Exits the menu
            break;
        default:
            cout << "I'm sorry, but that is an invalid choice. Please try again." << endl; // This handles incorrect input from the user
        }
    } while (input != 4);

    return 0;
}
