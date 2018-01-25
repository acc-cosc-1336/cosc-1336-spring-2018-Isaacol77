def get_hours_since_midnight(seconds):
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    return (seconds//3600)

'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''
    seconds_left = (seconds % 3600)
    return (seconds_left // 60)

def get_seconds(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''
    seconds_left = (seconds % 3600)
    return  (seconds_left % 60)

# used the // to get the amount of minutes left and the % to get the remaining seconds. 
