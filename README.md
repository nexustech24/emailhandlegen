# emailhandlegen

This is a simple Python GUI application that generates email handles based on user input. The handle is constructed using the following pattern:

[first three letters of first name][two-digit day][month][first three letters of last name]

For example, if the input is:

First Name: John

Day: 5

Month: 3

Last Name: Doe

The resulting email handle will be: joh0503doe.

Features

Validates inputs to ensure required fields are filled.

Automatically formats the day to include a leading zero if it is a single digit.

Displays the generated email handle in a readonly field for easy copying.

Prevents window resizing to maintain a consistent layout.

Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

Installation

Clone this repository:

git clone https://github.com/yourusername/email-handle-generator.git

Navigate to the project directory:

cd email-handle-generator

Run the application:

python email_handle_generator.py

How to Use

Enter your first name (at least 3 characters).

Enter the day of your birthday (1-31).

Enter the month of your birthday (1-12).

Enter your last name (at least 3 characters).

Click the "Generate" button.

Copy the generated email handle from the readonly field.


Contributing

Feel free to open issues or submit pull requests to improve the application.

Author

munitionne
