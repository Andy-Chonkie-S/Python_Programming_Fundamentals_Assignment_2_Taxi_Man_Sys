# Name: Andrew Sevilla
# Student ID: s2010815T
# Code problems / unmet requirements: All. Just a draft at this stage.

# Analysis / Reflection of code explaining :- 
## 1) Design process: 
### a) How I came up with the program design : My program design was again iterative for each part, except for the parts that were built for Assignment 1. I went back and refactored std out statements to f strings as I wanted to cement my knowledge of them, being the Python way of doing that.
### b) How I started writing the code after the design process : I started with the classes, methods and attributes/variables as a shell for the code. Then started working through the easiest bits towards the harder stuff. Importing the menu, then onto Location, Rate,
## 2) Challenges I met during code development : Here we go.. OO is the bane of my existence, meaning I should work on this more. Further to that my mental state was not good going into the assignment with other priorities and this was further impacted by a close passing. I started applying for special consideration, and reaching our to my RMIT psychologist, but ended up having to self medicate to try and get through this as they weren't able to provide me with an IAS in time. When it rains.. I had initial issues with accessing variables in classes but then realised I was an idiot as my syntax was wrong. I had similar issued with the formatting and syntax using f strings but got around that with some trial and error. So much trial and error... Also hacking and slashing my code from Assignment 1 was an issue. Like I didn't want to get rid of it to start afresh. This again is due to my mental state and trying to get medicated for it. Getting my head around the exception handling at the start was challenging too. Far out.. At the PART B Package/Service file reading stage I couldn't work out WHY I couldn't get attributes. I ended up running around and doing list stuff instead of OO. Then went back and realised I hadn't instantiated classes to the variable that was being assigned the data so instead of creating new objects I was just putting the data into lists, as I'd copied the code from the read_customers method, amended it, and forgot to add in Package / Service before the opening brackets. Yup. [Insert Mike Shrekowski with arms hanging down image here].

# Another challenge was getting my head around the compute_cost vs get_discount methods. I worked out why both but I figured get_discount was superfluous. Which it kind of is, but I guess we're doing it to demonstrate we understand inheritance.

# References: (Sources of info / websites / tools other than course contents directly under Canvas / Modules) : Nothing to reference, except Googling issues, so stack overflow, python docs and other Python blogs, etc. No code blocks were used / copied just troubleshooting assistance for my stupidity.

# Highest level attempted : HIGH DISTINCTION level - ran out of time and am still going to chase up special consideration as I didn't hear back from my RMIT counsellor. I sent emails to both her, my tutor and the  lecturer. I'm not happy.

import os
import sys

# Parent customer class which contains empty super methods and super properties for child BasicCustomer and EnterpriseCustomer classes.
class Customer:

    def __init__(self, customer_ID, customer_name):
        self.customer_ID = customer_ID
        self.customer_name = customer_name

    @property
    def get_customer_ID(self):
        return self.customer_ID

    @property
    def get_customer_name(self):
        return self.customer_name

    def get_discount(self):
        pass

    def display_info(self):
        pass

    def adjust_discount_rate(self):
        pass


# Child customer class Of Customer class which inherits super methods and super properties.
class BasicCustomer(Customer):

    __discount_rate = 0.1

    def __init__(self, customer_ID, customer_name, __discount_rate = 0.1):
        super().__init__(customer_ID, customer_name)
        self.__discount_rate = __discount_rate

    @property
    def get_customer_ID(self):
        return self.customer_ID

    @property
    def get_customer_name(self):
        return self.customer_name
    
    @property
    def get_discount_rate(self):
        return BasicCustomer.__discount_rate    

    # Method to return the discount once multiplied to the distance fee.
    def get_discount(self, distance_fee):
       
        self._calculated_discount = BasicCustomer.__discount_rate * distance_fee
        return self._calculated_discount
    
    # Method to display Basic Customer info.
    def display_info(self):
        print(f'The Basic Customer class attributes in ID position {self.customer_ID} are:\nName: {self.customer_name}\nDiscount Rate: {BasicCustomer.__discount_rate}.\n')
        return None

    # Method to adjust Basic Customer discount rate.
    @staticmethod
    def set_discount_rate(adjusted_rate):
        BasicCustomer.__discount_rate = adjusted_rate
        return None


    # Method to set discount rate containing exception handling
    def adjust_discount_rate(self):

        while True:
            try:
                discount_rate_update_value = InvalidRateException.validate_new_rate(input('Please enter the updated Basic Customer discount rate:\n').strip())
                break
            except InvalidRateException as e:
                print(e)
                continue

        BasicCustomer.set_discount_rate(discount_rate_update_value / 100)
        print(f"Standard Basic Customer Discount rate adjusted to {discount_rate_update_value}%.")        

        return None

# Child customer class Of Customer class which inherits super methods and super properties.
class EnterpriseCustomer(Customer):

    _rate_multiplier = 0.05
    _threshold = 100

    def __init__(self, customer_ID, customer_name, discount_rate = 0.2, threshold = 100):
        super().__init__(customer_ID, customer_name)       
        self.__discount_rate = discount_rate
        self._threshold = threshold

    @property
    def get_customer_ID(self):
        return self.customer_ID

    @property
    def get_customer_name(self):
        return self.customer_name

    @property
    def get_threshold(self):
        return self._threshold
    
    @property
    def get_discount_rate(self):
        return self.__discount_rate

    #method to adjust an Enterprise Customer's discount rate    
    def adjust_discount_rate(self, adjusted_discount_rate):
        self.__discount_rate = adjusted_discount_rate
    
    # Method to return the discount once multiplied to the distance fee. If the distance fee is less than a threshold amount then the discount percentage rate is reduced by a multiplier amount.
    def get_discount(self, distance_fee):

        if distance_fee < self._threshold:
            discount_rate = discount_rate - self._rate_multiplier
       
        self._calculated_discount = self.__discount_rate * distance_fee
        return self._calculated_discount
    
    # Method to display Enterprise Customer info.
    def display_info(self):
        print(f'The Enterprise Customer class attributes in ID position {self.customer_ID} are:\nName: {self.customer_name}\nDiscount Rate: {self.__discount_rate}\nReduced Discount Rate: {(self.__discount_rate - self._rate_multiplier)}\nReduced Discount Rate percentage: {self._rate_multiplier}\nDiscount Rate Threshold: {self._threshold}.\n')
        return None

    # Method to update the Enterprise Customer discount rate.
    def adjust_enterprise_customer_discount_rate(self, records_instance):

        validate_enterprise_customer = None

        while True:
            validate_customer = input("Please enter the Enterprise Customer name / ID that requires their discount rate updated: ").strip()

            try:            
                validate_enterprise_customer = InvalidEnterpriseCustomerException.validate_enterprise_customer(validate_customer, records_instance)
                enterprise_customer_name = validate_enterprise_customer.get_customer_name
                break
            except InvalidEnterpriseCustomerException as e:
                print(e)
                continue

        while True:
            try:            
                discount_rate_update_value = InvalidRateException.validate_new_rate(input(f'Please enter the updated Enterprise Customer discount rate for {enterprise_customer_name}:\n').strip())
                break
            except InvalidRateException as e:
                print(e)
                continue

        validate_enterprise_customer.adjust_discount_rate(discount_rate_update_value / 100)
        print(f"Enterprise Customer Discount rate adjusted to {discount_rate_update_value}%.")        

        return None    

    # Method to update the Enterprise Customer rate threshold rate.
    def set_threshold(self, threshold_update_value):
        self._threshold = threshold_update_value
        return self._threshold


# Class containing the Location data structure
class Location:
    location_ID = None
    location_name = None

    def __init__(self, location_ID, location_name):
        self.__location_ID = location_ID
        self.__location_name = location_name

    #method to display location info
    def display_info(self):
        print(f'The Location class attributes in ID position {self.__location_ID} are:\nName: {self.__location_name}.\n')
        return None

    @property
    def get_location_ID(self):
        return self.__location_ID

    @property
    def get_location_name(self):
        return self.__location_name
    

# Class containing the Rate data structure
class Rate:

    def __init__(self, rate_ID, rate_name, price_per_km):
        self.__rate_ID = rate_ID
        self.__rate_name = rate_name
        self.__price_per_km = price_per_km

    #method to display booking info
    def display_info(self):
        print(f'The Rate class attributes in ID position {self.__rate_ID} are:\nRate Type Name: {self.__rate_name}\nRate Type Price per km: {self.__price_per_km}.\n')
        return None
    
    @property
    def get_rate_ID(self):
        return self.__rate_ID

    @property
    def get_rate_name(self):
        return self.__rate_name
    
    @property
    def get_rate(self):
        return self.__price_per_km
    
    # method to update existing rates
    def update_rate(self, rate_amount_update):
        self.__price_per_km = rate_amount_update
    
    # method which accepts two list inputs from user of rates and rate amounts, validates the rates and checks the rate types to see whether they're existing or not and either adds new rates or updates existing rates respectively.
    def add_update_rate_types_and_prices(self, records_instance):
        
        _existing_rate_object_dict = {}
        _new_rate_dict = {}
        _update_existing_rates_dict = {}
        _add_new_rates_dict = {}

        rate_names_update = input('Please enter the list of rate name(s) to update the current list. The rate types must be entered as a list that separates by commas (e.g. metropolitan, deluxe, premium.)\n').strip().split(',')

        rate_item_counter = 1

        for rate_name in rate_names_update:
            rate_name.strip()
            existing_rate_object = records_instance.find_rate(rate_name)
            if existing_rate_object != None:
                _existing_rate_object_dict[rate_item_counter].append(existing_rate_object)
            else:
                _new_rate_dict[rate_item_counter].append(rate_name)
            rate_item_counter += 1

        while True:            
            try:
                rate_amounts_update = InvalidRateException.validate_new_rate(input('\n\nNow please enter the list of rate amount(s) corresponding to the above list in that order. The rate amounts must also be entered as a list that separates by commas (e.g. 2.0, 2.5, 2.2.)\n').strip().split(','))
                break
            except InvalidRateException as e:
                print(e)                
                continue

        rate_amounts_update = [rate_amounts.strip() for rate_amounts in rate_amounts_update]

        for existing_rate_object_key, existing_rate_object_value in _existing_rate_object_dict.items():
            if existing_rate_object_key == rate_amounts_update.index(existing_rate_object_value):
                _update_existing_rates_dict[existing_rate_object_key] = (existing_rate_object_value, rate_amounts_update[existing_rate_object_key])
                _existing_rate_object_dict[existing_rate_object_value].rate_amount_update(rate_amounts_update[existing_rate_object_key])

        for new_rate_object_key, new_rate_object_value in _new_rate_dict.items():
            if new_rate_object_key == rate_amounts_update.index(new_rate_object_value):
                _add_new_rates_dict[new_rate_object_key] = (new_rate_object_value, rate_amounts_update[new_rate_object_key])
                
                latest_rate_ID_number = int(self.records_instance.get_last_rate_ID()[1:])

                new_rate_ID = ('R' + str(latest_rate_ID_number))
                latest_rate_ID_number += 1
                records_instance.append_new_rate(Rate(new_rate_ID, _add_new_rates_dict[new_rate_object_key], rate_amounts_update[new_rate_object_key]))

        print(f'Updates to rate list are as follows : {_existing_rate_object_dict}\n {_add_new_rates_dict}\n')
    
        return None


# Class containing the Booking data structure which contains variables that are accessible via getter methods. I added a method to get the latest booking list item's ID as well as a list item to store the booking objects. Thhe service / package is optional.
class Booking:

    _basic_fee = 4.2

    def __init__(self, booking_ID, booking_customer_ID, departure_ID, destination_ID, distance, booking_rate_ID, service_package_ID = None):
        self.__booking_ID = booking_ID
        self.__booking_customer_ID = booking_customer_ID
        self.__booking_rate_ID = booking_rate_ID
        self.__destination_ID = destination_ID
        self.__departure_ID = departure_ID
        self.__distance = distance
        self.__service_package_ID = service_package_ID

    @property
    def get_booking_ID(self):
        return self.__booking_ID

    @property
    def get_booking_customer_ID(self):
        return self.__booking_customer_ID

    @property
    def get_booking_rate_ID(self):
        return self.__booking_rate_ID

    @property
    def get_destination_ID(self):
        return self.__destination_ID
    
    @property
    def get_departure_ID(self):
        return self.__departure_ID
    
    @property
    def get_distance(self):
        return self.__distance
    
    @property
    def get_service_package_ID(self):
        return self.__service_package_ID

    @property
    def get_basic_fee(self):
        return self._basic_fee

    # method to compute the cost items for a booking. It expects a list containing the distance, price per km rate and an optional discount, applies some arithmetic and returns a list distance fee, basic fee and calculated discount.
    def compute_cost(self, customer_object, distance, price_per_km, discount = 0):

        if customer_object != None:
            discount = customer_object.get_discount(distance)

        raw_rate = price_per_km * distance
        discount = discount * distance
        calculated_rate = raw_rate - discount
        distance_fee = calculated_rate + Booking._basic_fee
        return distance_fee, Booking._basic_fee, discount


# Class containing the Records data. As the Booking data wasn't specified to be kept in the Records class I opted to keep it in the Booking class, although I might change this later if it makes more sense as I go along. Also, I feel there's a more elegant way to be reading in the file data and searching so I feel I could make a general purpose method that gets called by the required methods in Part A if I have time.
class Records:

    def __init__(self):
        self.__existing_customer_list = []
        self.__existing_location_list = []
        self.__existing_rate_type_list = []
        self.__booking_list = []        
        self.__existing_service_package_list = []
        self._current_directory = os.path.dirname(os.path.abspath(__file__))
        self._customer_file_exists = False

    # method to read customer CSV data file which will exit the program if the file doesn't exist, raising an exception and displaying a message. These customer objects are then stored in a list.
    def read_customers(self, customers_filename):

        try:
            filepath = os.path.join(self._current_directory, customers_filename)
            with open(filepath, 'r') as file_name:
                line = file_name.readline()
                while line:
                    filedata_field = line.strip().split(",")              
                    if filedata_field[2].strip() == 'E':
                        new_customer = EnterpriseCustomer(int(filedata_field[0].strip()), filedata_field[1].strip(), float(filedata_field[3].strip()), int(filedata_field[4].strip()))
                    elif filedata_field[2].strip() == 'B':
                        new_customer = BasicCustomer(int(filedata_field[0].strip()), filedata_field[1].strip(), float(filedata_field[3].strip()))
                    line = file_name.readline()                                   
                    self.__existing_customer_list.append(new_customer)
                file_name.close()
            return None
        except OSError as e:
            raise SystemExit(f'\nCustomers file not found. Exiting.\n\n{e}\n')

    # method to read a location CSV data file which will exit the program if the file doesn't exist, raising an exception and displaying a message. These location objects are then stored in a list.
    def read_locations(self, locations_filename):

        try:
            filepath = os.path.join(self._current_directory, locations_filename)
            with open(filepath, 'r') as file_name:
                line = file_name.readline()
                while line:
                    filedata_field = line.strip().split(",")
                    new_location = Location(filedata_field[0].strip(), filedata_field[1].strip())
                    line = file_name.readline()                                   
                    self.__existing_location_list.append(new_location)
                file_name.close()
            return None
        except OSError as e:
            raise SystemExit(f'\nLocations file not found. Exiting.\n\n{e}\n')

    # method to read a rates CSV data file which will exit the program if the file doesn't exist, raising an exception and displaying a message. These location objects are then stored in a list.
    def read_rates(self, rates_filename):
        filepath = os.path.join(self._current_directory, rates_filename)

        try:
            with open(filepath, 'r') as file_name:
                line = file_name.readline()
                while line:
                    filedata_field = line.strip().split(",")
                    new_rate = Rate(filedata_field[0].strip(), filedata_field[1].strip(), float(filedata_field[2].strip()))
                    line = file_name.readline()
                    self.__existing_rate_type_list.append(new_rate)
                file_name.close()
            return None
        except OSError as e:
            raise SystemExit(f'\nRates file not found. Exiting.\n\n{e}\n')


    # method to read a services CSV data file which will exit the program if the file doesn't exist, raising an exception and displaying a message. These services objects are then stored in a list.
    def read_service(self, services_filename):

        try:
            filepath = os.path.join(self._current_directory, services_filename)
            with open(filepath, 'r') as file_name:
                line = file_name.readline()
                while line:
                    filedata_field = line.strip().split(",")       

                    if filedata_field[0].strip().startswith('S'):
                        new_service = Service(filedata_field[0].strip(), filedata_field[1].strip(), float(filedata_field[2].strip()))
                        self.__existing_service_package_list.append(new_service)

                    elif filedata_field[0].strip().startswith('P'):
                        multiple_service_ID_input = filedata_field[2:]

                        # Iterate through service ID list read in to strip each service ID
                        service_ID_list = []
                        for service_ID in multiple_service_ID_input:
                            service_ID = service_ID.strip()
                            service_ID_list.append(service_ID)

                        new_package = Package(filedata_field[0].strip(), filedata_field[1].strip(), service_ID_list)
                        self.__existing_service_package_list.append(new_package)
                    line = file_name.readline()

                file_name.close()
            return None
        except OSError as e:
            raise SystemExit(f'\Services file not found. Exiting.\n\n{e}\n')
        

    # method to read a services CSV data file which will exit the program if the file doesn't exist, raising an exception and displaying a message. These services objects are then stored in a list.
    def read_bookings(self, bookings_filename):

        try:
            filepath = os.path.join(self._current_directory, services_filename)
            with open(filepath, 'r') as file_name:
                line = file_name.readline()
                while line:
                    filedata_field = line.strip().split(",")       

                    if filedata_field[0].strip().startswith('S'):
                        new_service = Service(filedata_field[0].strip(), filedata_field[1].strip(), float(filedata_field[2].strip()))
                        self.__existing_service_package_list.append(new_service)

                    elif filedata_field[0].strip().startswith('P'):
                        multiple_service_ID_input = filedata_field[2:]

                        # Iterate through service ID list read in to strip each service ID
                        service_ID_list = []
                        for service_ID in multiple_service_ID_input:
                            service_ID = service_ID.strip()
                            service_ID_list.append(service_ID)

                        new_package = Package(filedata_field[0].strip(), filedata_field[1].strip(), service_ID_list)
                        self.__existing_service_package_list.append(new_package)
                    line = file_name.readline()

                file_name.close()
            return None
        except OSError as e:
            raise SystemExit(f'\Services file not found. Exiting.\n\n{e}\n')

    # method to read add a new booking to the booking list. It accepts a Booking object. I may make the object creation internal and pass in raw values here at a later stage, if deemed appropriate.
    def append_new_booking(self, new_booking):
        self.__booking_list.append(new_booking)
        return None

    # method to find a customer in the customer object list given a search value, on either customer ID or name.
    def find_customer(self, search_value):
        
        for customer_object in self.__existing_customer_list:
            if isinstance(customer_object, Customer):
                if customer_object.get_customer_ID == search_value or customer_object.get_customer_name == search_value:
                    return customer_object

        return None

    # method to find a location in the location object list given a search value, on either location ID or name.
    def find_location(self, search_value):

        for location_object in self.__existing_location_list:
            if isinstance(location_object, Location):
                if location_object.get_location_ID == search_value or location_object.get_location_name == search_value:
                    return location_object

        return None

    # method to find a rate in the rate object list given a search value, on either rate ID or name.
    def find_rate(self, search_value):
        
        for rate_object in self.__existing_rate_type_list:
            if isinstance(rate_object, Rate):
                if rate_object.get_rate_ID == search_value or rate_object.get_rate_name == search_value:
                    return rate_object

        return None
    
    # method to find a service or package in the service / package object list given a search value, on either package / service ID or name.
    def find_service(self, search_value):

        for service_package_object in self.__existing_service_package_list:
            print(service_package_object)
            if isinstance(service_package_object, (Service, Package)):
                print('service_package_object')
                if service_package_object.get_ID == search_value or service_package_object.get_name == search_value:
                    return service_package_object

        return None

    # method to list customers in the customer object list.
    def list_customers(self):
        for customer in self.__existing_customer_list:
            customer.display_info()
        return None
    
    # method to retrieve the last customer object in the customer object list.
    def get_last_customer(self):
        return self.__existing_customer_list[-1]

    # method to list locations in the location object list.
    def list_locations(self):
        for location in self.__existing_location_list:
            location.display_info()
        return self.__existing_location_list

    # method to list rates in the rate object list.
    def list_rates(self):
        for rate in self.__existing_rate_type_list:
            rate.display_info()
        return None
    
    # method to list services/packages.
    def list_service(self):
        print('The Service data is as follows:')
        for service_package_item in self.__existing_service_package_list:
            print(service_package_item)
        return self.__existing_service_package_list

    # method to append a new customer object to the existing customer object list.
    def append_new_customer(self, new_customer):
        self.__existing_customer_list.append(new_customer)

    # method to retrieve the last booking object in the booking object list.
    def get_latest_booking_ID(self):
        if self.__booking_list != []:
            return self.__booking_list[-1]
        else:
            return None
        
    # method to retrieve the last location object ID in the location object list.
    def get_last_location_ID(self):
        last_location_object = self.__existing_location_list[-1]
        last_location_ID = last_location_object.get_location_ID
        return last_location_ID
    
    # method to append a new location object to the existing location object list.
    def append_new_location(self, new_location):
        self.__existing_location_list.append(new_location)

    # method to retrieve the last rate object ID in the rate object list.
    def get_last_rate_ID(self):
        last_rate_object = self.__existing_rate_type_list[-1]
        last_rate_object_ID = last_rate_object.get_rate_ID
        return last_rate_object_ID

    # method to append a new rate object to the existing location object list.
    def append_new_rate(self, new_rate):
        self.__existing_rate_type_list.append(new_rate)

    # method to display all bookings in booking list
    def display_all_bookings(self):
        for booking_list_object in self.__booking_list:
            booking_customer_ID = self.__booking_list.get_booking_customer_ID(booking_list_object)
            booking_rate_ID = self.__booking_list.get_booking_rate_ID(booking_list_object)
            departure_ID = self.__booking_list.get_departure_ID(booking_list_object)
            destination_ID = self.__booking_list.get_destination_ID(booking_list_object)
            distance = self.__booking_list.get_distance(booking_list_object)
            service_package_ID = self.__booking_list.get_service_package_ID(booking_list_object)
            basic_fee = self.__booking_list.get_basic_fee(booking_list_object)

        print(f'{booking_customer_ID}, {booking_rate_ID}, {departure_ID}, {destination_ID}, {distance}, {service_package_ID}, {basic_fee}')
    

    def display_most_popular_customer(self):
        pass


    def display_customer_booking_history(self):
        pass

# This class contains the menu method as well as initiates the reading of files and records lists, and contains a method to book a trip, which prints a receipt.
class Operations:

    _length_of_border = 60

    def __init__(self):
        self.records_instance = Records()

        self.records_instance.read_customers('customers.txt')
        self.records_instance.read_locations('locations.txt')
        self.records_instance.read_rates('rates.txt')
        self.records_instance.read_service('services.txt')
#        self.records_instance.read_bookings('bookings.txt')        

    # A method to display a menu and await input selection. It will loop until a correct selection is made, and exit if 0 is entered. So pretty.
    def menu(self):
        menu_input = ''
        while (menu_input != '0'):
            print('\nWelcome to the RMIT taxi management system!\n')
            print(f'{"#" * self._length_of_border}')
            print('You can choose from the following options:')
            print('1: Book a trip')
            print('2: Display existing customers')
            print('3: Display existing locations')
            print('4: Display existing rate types')
            print('5: Display existing services/packages')
            print('6: Add new locations')
            print('7: Adjust the discount rate of all Basic customers')
            print('8: Adjust the discount rate of an Enterprise customer')
            print('9: Add/update rate types and prices')
            print('10: Display all bookings')
            print('11: Display the most popular customer')
            print('12: Display a customer booking history')            
            print('0: Exit the program')
            print(f'{"#" * self._length_of_border}')
            menu_input = input('Choose one option: ')

            match menu_input:
                case '1':
                    self.book_a_trip()
                case '2':
                    self.records_instance.list_customers()
                case '3':
                    self.records_instance.list_locations()
                case '4':
                    self.records_instance.list_rates()
                case '5':
                    self.records_instance.list_service()
                case '6':
                    self.add_new_locations()
                case '7':
                    BasicCustomer.adjust_discount_rate(self)
                case '8':
                    EnterpriseCustomer.adjust_enterprise_customer_discount_rate(self, self.records_instance)
                case '9':
                    Rate.add_update_rate_types_and_prices(self)
                case '10':
                    self.records_instance.display_all_bookings()
                case '11':
                    self.records_instance.display_most_popular_customer()
                case '12':
                    self.records_instance.display_customer_booking_history()


    # This method books a trip by prompting the user and accepting their input, with some error handling (distance being a float..), and stripping of whitespaces. The new booking is then appended to the booking list because reasons.
    def book_a_trip(self):

        _space = ' '
#        _booking_history_width = self._length_of_border / 2

        computed_cost = []
        service_package_ID = None

        while True:
            try:
                validated_name = InvalidCharactersException.validate_name(input_name = input('Enter the name of the customer [e.g. Huong]:\n').strip())
                break
            except InvalidCharactersException as e:
                print(e)                
                continue

        while True:
            try:
                validated_departure = InvalidLocationException.validate_location(self.records_instance, input_location = input('Enter the departure location [enter a valid location only, e.g. Melbourne]:\n').strip())
                break
            except InvalidLocationException as e:
                print(e)
                continue

        multiple_destination_flag = 'y'
        # Variable to compare current destination with most recent to avoid user entering same location twice in a row
        previous_destination = None

        destination_list = []
        distance_list = []

        while multiple_destination_flag == 'y':

            booking_departure_object = self.records_instance.find_location(validated_departure)
            booking_departure_ID = booking_departure_object.get_location_ID

            while True:
                try:
                    validated_destination = InvalidLocationException.validate_destination(self.records_instance, previous_destination, input_location = input('Enter the destination location [enter a valid location only, e.g. Chadstone]:\n').strip())
                    break
                except InvalidLocationException as e:
                    print(e)
                    continue

            previous_destination = validated_destination

            booking_destination_object = self.records_instance.find_location(validated_destination)
            booking_destination_ID = booking_destination_object.get_location_ID

            while True:
                try:
                    validated_distance = InvalidDistanceException.validate_distance(input_distance = input('Enter the distance (km) [enter a positive number only, e.g. 12.5, 6.8]:\n').strip())
                    break
                except InvalidDistanceException as e:
                    print(e)
                    continue
            
            destination_list.append(booking_destination_ID)
            distance_list.append(validated_distance)

            multiple_destination_flag = input('Did you want to enter another Destination? Please only enter \'y\' or \'n\'.\n').strip()            

            while multiple_destination_flag not in ('y', 'n'):
                multiple_destination_flag = input('The response is not valid. Do you want to enter another destination? (i.e. \'y\' or \'n\')\n')

        while True:
            try:
                validated_rate = InvalidRateException.validate_rate(self.records_instance, input_rate_type = input('Enter the rate type [enter a valid type only, e.g. standard, peak, weekends, holiday]:\n').strip())
                break
            except InvalidRateException as e:
                print(e)
                continue

        while True:
            try:
                input_service_package_confirmation = InvalidServicePackageException.validate_service_package_confirmation(self.records_instance, input_service_package_confirmation = input('Would you like to order an extra service / package? (i.e. \'y\' or \'n\')\n').strip())
                break
            except InvalidServicePackageException as e:
                print(e)
                continue

        if input_service_package_confirmation == 'y':
            while True:
                try:
                    validate_service_package_selection = InvalidServicePackageException.validate_service_package(self.records_instance, input_service_package = input('Which service / package would you like to order? (e.g. Drink, Internet, Starter, etc.).\n').strip())
                    break
                except InvalidServicePackageException as e:
                    print(e)
                    continue

            service_package_object = self.records_instance.find_service(validate_service_package_selection)
            service_package_ID = service_package_object.get_ID
            service_package_name = service_package_object.get_name
            service_package_price = service_package_object.get_price

        # Get rate data to compute cost(s), etc.
        booking_rate_object = self.records_instance.find_rate(validated_rate)
        booking_rate = booking_rate_object.get_rate
        booking_rate_ID = booking_rate_object.get_rate_ID

        booking_customer_object = self.records_instance.find_customer(validated_name)

        computed_cost = Booking.compute_cost(self, booking_customer_object, validated_distance, booking_rate)
        total_cost = computed_cost[0] + computed_cost[1] - computed_cost[2]

        # Check if new customer and append to customer list but if not get customer ID, to then create a Booking object (getting the latest booking ID) and appending the object to the booking list.
        if (booking_customer_object == None):
            last_customer = self.records_instance.get_last_customer()
            booking_customer_id = last_customer.get_customer_ID + 1

            new_discount_rate = BasicCustomer.get_discount_rate
            new_customer = BasicCustomer(booking_customer_id, validated_name, new_discount_rate)

            self.records_instance.append_new_customer(new_customer)
        else:
            booking_customer_type = booking_customer_object.__class__.__name__
            booking_customer_id = booking_customer_object.get_customer_ID
           
            print(f'\n{validated_name} is an existing customer. Their customer type is: {booking_customer_type}.\n')            

        latest_booking_ID = self.records_instance.get_latest_booking_ID()

        if latest_booking_ID == None:
            latest_booking_ID = 1
        else:
            latest_booking_ID = latest_booking_ID + 1

        new_booking = Booking(latest_booking_ID, booking_customer_id, booking_departure_ID, destination_list, distance_list, booking_rate_ID, service_package_ID)

        self.records_instance.append_new_booking(new_booking)

        # The Taxi receipt is printed here.
        print(f'{"-" * self._length_of_border}')
        print(f'{"Taxi Receipt" : ^{self._length_of_border}}')
        print(f'{"-" * self._length_of_border}')
        
        print(f'Name:{_space:<{int((self._length_of_border / 2) - 5)}}{validated_name}')
        print(f'Departure:{_space:<{int((self._length_of_border / 2) - 10)}}{validated_departure}')
        print(f'Rate:{_space:>{int((self._length_of_border / 2) - 5)}}{booking_rate:.2f} (AUD per km)')
        print(f'Total Distance: {validated_distance:>{int((self._length_of_border / 2) - 12)}.2f} (km)')
        print(f'{"-" * self._length_of_border}')
        print(f'Basic fee: {computed_cost[1]:>{int((self._length_of_border / 2) - 7)}.2f} (AUD)')
        print(f'Distance fee: {computed_cost[0]:>{int((self._length_of_border / 2) - 10)}.2f} (AUD)')
        print(f'Discount: {computed_cost[2]:>{int((self._length_of_border / 2) - 6)}.2f} (AUD)')

        if input_service_package_confirmation == 'y':
            print(f'Service/Package Name:{_space:<{int((self._length_of_border / 2) - 21)}} {service_package_name}')            
            print(f'Service/Package Price: {service_package_price:>{int((self._length_of_border / 2) - 18)}.2f} (AUD)')
            total_cost = total_cost + service_package_price

        print(f'{"-" * self._length_of_border}')
        print(f'Total cost: {total_cost:>{int((self._length_of_border / 2) - 8)}.2f} (AUD)\n')

    #method to add new locations to records instance object  
    def add_new_locations(self):

        new_locations_list = []
        existing_location_list = []

        latest_location_ID_number = int(self.records_instance.get_last_location_ID()[1:])

        locations_update_list = input('\nPlease enter the list of locations to update the current list. The locations must be entered as a list that separates by commas (e.g. Bummaroo, Humpybong, Mamungkukumpurangkuntjunya)\n').title().strip().split(',')

        for input_location_name in locations_update_list:

            input_location_object = self.records_instance.find_location(input_location_name.strip())

            if input_location_object != None:
                existing_location_list.append(input_location_name.strip())
            else:
                new_locations_list.append(input_location_name.strip())
                new_location_ID = ('L' + str(latest_location_ID_number))
                latest_location_ID_number += 1
                self.records_instance.append_new_location(Location(new_location_ID, input_location_name.strip()))
                
        if existing_location_list:
            print(f'\nThese locations are duplicates and have been omitted:\n{", ".join(map(str, existing_location_list))}')

        print(f'\nUpdated location list is : {new_locations_list}\n\n')

        return None


class Service:

    def __init__(self, ID, name, price):
        self.__ID = ID
        self.__name = name
        self.__price = price
  
    @property
    def get_ID(self):
        return self.__ID

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_price(self):
        return self.__price

    def display_info(self):
        print(f"ID: {self.get_ID()}\nName: {self.get_name()}\nPrice: {self.get_price()} (AUD)")

    #method to display Service info
    def display_info(self):
        print(f'The Service class attributes in ID position {self.__ID} are:\nService Name: {self.__name}\nService Price: {self.__price}.\n')
        return None    


# This class inherits the parent class Service, to effectively contain an object list of services. To retrieve the package cost it multiplies the amount by the package discount, initially set to 80%.
class Package(Service):

    _package_discount = 0.8
    
    def __init__(self, ID, name, list_of_services):
        super().__init__(ID, name, 0)
        self.__list_of_services = list_of_services

    @property
    def get_list_of_services(self):
        return self.__list_of_services
    
    #method to display Package info
    def display_info(self):
        print(f'The Package class attributes in ID position {self.__ID} are:\nPackage Name: {self.__name}\nList of Services in Package: {self.__list_of_services}.\n')
        return None
    
    def get_package_price(self):
        _total_price = 0
        for service_ID in self.__list_of_services: 
            service = Service(service_ID, "", 0)
            _total_price += service.__price
        return _total_price * self._package_discount


# This custom exception class accepts a variable and ensures it's either completely a number or a string, not a combination of both for the customer name / ID.
class InvalidCharactersException(Exception):
    
    def __init__(self, message="\nInvalid characters detected. Please try again.\n"):
        self.message = message
        super().__init__(message)

    @staticmethod
    def validate_name(input_name):
        if (not input_name.isdigit()) and (not input_name.isalpha()):
            raise InvalidCharactersException()
        return input_name


# This custom exception class raises an exception if a departure value is not in the records instance, or if the destination is not in the records instance or is equal to the departure value. 
# I might be able to nest this custom exception class but thought to just nest the validation method. I don't know which approach is more elegant but at this stage, I don't care and will fix it if there's time / I start caring again.
class InvalidLocationException(Exception):

    def __init__(self, message="\nInvalid location entered. Please try again.\n"):
        self.message = message
        super().__init__(message)

    @staticmethod
    def validate_location(records_instance, input_location):
        if not(records_instance.find_location(input_location)):
            raise InvalidLocationException()
        else:
            return input_location

    @staticmethod
    def validate_destination(records_instance, previous_destination, input_location):
        InvalidLocationException.validate_location(records_instance, input_location)
        if (previous_destination == input_location):
            raise InvalidLocationException()
        else:
            return input_location


# This custom exception class raises exceptions if the rate value is not contained within the records instance or if the new rate is not a positive number.
class InvalidRateException(Exception):

    def __init__(self, error_message = ""):
        super().__init__(error_message)

    @staticmethod
    def validate_rate(records_instance, input_rate_type):
        if not(records_instance.find_rate(input_rate_type)):
            raise InvalidRateException("\nInvalid rate type entered. Please try again entering a valid rate (e.g. standard, peak, etc.).\n")
        else:
            return input_rate_type
        
    @staticmethod
    def validate_new_rate(input_rate_list):
        _new_rate_error_message = "\nInvalid rate entered. Please try again, entering only positive number(s).\n"
        try:
            for rate_item in input_rate_list:
                rate_item = float(rate_item)
                if (float(rate_item) > 0):
                    rate_item = float(round(rate_item, 3))
                    return rate_item
                else:
                    raise InvalidRateException(_new_rate_error_message)
        except:
            raise InvalidRateException(_new_rate_error_message)


# This custom exception class raises an exception if the distance value is not a number, or is a negative number. The code seems inelegant but I'll leave it as is for now. Would need to research a better way, if there is one..
class InvalidDistanceException(ArithmeticError):
    
    def __init__(self, message="\nInvalid distance entered. Please try again, entering a positive number.\n"):
        self.message = message
        super().__init__(message)

    @staticmethod
    def validate_distance(input_distance):
        try:
            input_distance = float(input_distance)
            if (float(input_distance) > 0):
                input_distance = float(round(input_distance, 3))
                return input_distance
            else:
                raise InvalidDistanceException()
        except:
            raise InvalidDistanceException()
                

# This custom exception class raises an exception if the rate value is not contained within the records instance. 
class InvalidServicePackageException(Exception):

    def __init__(self, error_message = ""):
        super().__init__(error_message)

    @staticmethod
    def validate_service_package_confirmation(records_instance, input_service_package_confirmation):
        if input_service_package_confirmation not in ('y', 'n'):
            raise InvalidServicePackageException("\nInvalid entry. Please enter either \'y\' or \'n\'\n")
        else:
            return input_service_package_confirmation

    @staticmethod
    def validate_service_package(records_instance, input_service_package):
        if not(records_instance.find_service(input_service_package)):
            raise InvalidServicePackageException("\nInvalid service/package entered. Please enter a valid service/package name (Internet, Snack, Drink, Entertainment, etc.).\n")
        else:
            return input_service_package
        
class InvalidEnterpriseCustomerException(Exception):

    def __init__(self, message="\nInvalid Enterprise Customer entered. Please try again, entering a valid Enterprise Customer Name / ID (e.g. John).\n"):
        self.message = message
        super().__init__(message)

    @staticmethod
    def validate_enterprise_customer(validate_customer, records_instance):
        find_customer_object = records_instance.find_customer(validate_customer)
        if find_customer_object != None:
            customer_object_type = type(find_customer_object)
            if customer_object_type == EnterpriseCustomer:
                return find_customer_object
        
        raise InvalidEnterpriseCustomerException()


Run_Program = Operations()
Run_Program.menu()
