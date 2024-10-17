''' 
crete accessor methods for each attribute of the Course class and Register class. Write the code for the 
update_seat_count method
'''

class Course:

    def __init__(self,name,crn,seats,status):
        self.__name = name
        self.__crn = crn
        self.__seats = seats
        self.__status = status

    # Accessor method for name
    def get_name(self):
        return self.__name
    
    # Accessor method for crn
    def get_crn(self):
        return self.__crn
    
    # Accessor method for seats
    def get_seats(self):
        return self.__seats
    
    # Accessor method for status
    def get_status(self):
        return self.__status

    def update_seat_count(self):
        '''
        write the code that will reduce the
        number of seats by 1 every time this
        method is called. If the seat count
        reaches zero it should change the 'status' 
        attribute to 'closed'
        '''
        if self.__seats > 0:
            self.__seats -= 1
        else:
            self.__status = 'closed'


        

class Register:

    def __init__(self,name,crn):
        self.__studentname = name
        self.__crn = crn

    # Accessor method for name
    def get_name(self):
        return self.__studentname
    
    def get_crn(self):
        return self.__crn