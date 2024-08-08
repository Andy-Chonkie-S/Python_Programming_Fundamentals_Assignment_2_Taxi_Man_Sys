# Python Programming Fundamentals Assignment 2
**Student Name:** Andrew Sevilla

**Student ID:** s2010815T

**Repo Name:** Python_Programming_Fundamentals_Assignment_2_Taxi_Man_Sys
**Short Description:** Second Python Programming Fundamentals Assignment, building on the Assignment 1 Taxi Management System program.

## Overview
This repository contains the code for Assignment 2 of the Python Programming Fundamentals course (COSC2531). The assignment involves developing on the taxi management system in Assignment 1, this time using the object-oriented programming (OOP) paradigm.

It implements a basic taxi booking system with functionalities such as:

* User input prompts for customer information, trip details (departure, destination, distance), rate type, and optional service package selection.
* Error handling for invalid user input (e.g., non-numeric distance, invalid characters in names, etc.).
* Calculation of trip cost based on distance, rate type, and potential customer discount.
* Customer record management (adding new customers or retrieving existing ones).
* Service package selection (optional) with pricing consideration.
* Generation of a taxi receipt displaying booking details and final cost.

**Download the full assignment spec:** [COSC2531_Assignment2_Sem22023.pdf](COSC2531_Assignment2_Sem22023.pdf)

## Dependencies
* Python (version 3.6)

## Code Structure

The program relies on several classes:

* `Operations`: Handles the main menu and user interaction.
* `Booking`: Represents a single taxi booking with customer, trip, and cost details.
* `Customer`: Represents a customer object with basic information and potential discount logic (base class).
* `BasicCustomer`: Inherits from `Customer`, representing a standard customer type.
* `EnterpriseCustomer` (not implemented): Could be added to represent a customer with a specific discount structure. (Consider adding this if planned for future development)
* `Location`: Represents a location object with an ID and name.
* `Rate`: Represents a rate type object with an ID and rate value.
* `Service`: Represents a service or package object with an ID, name, and price.
* `Package` (not fully implemented): Inherits from `Service`, potentially representing a service package with a list of included services and a discount mechanism.
* Various custom exception classes handle invalid user input (e.g., `InvalidCharactersException`, `InvalidDistanceException`, etc.).


## Usage

1. Save the code as a Python file (e.g., `taxi_booking.py`).
2. Open a terminal window and navigate to the directory containing the file.
3. Run the program using the `python` command:

```
bash
python taxi_booking.py
```

## Known Issues
* `EnterpriseCustomer` & `Package` are not fully implemented. There are likely other issues, but I'm not going to revisit this code unless the need arises.

## Additional Notes
* Do not use this code to cheat on your assignment, if similar. Cheating only cheats yourself!
  
