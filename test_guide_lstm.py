# test_guide.py

# A module to centrally define the test phase information

##################
####  TRAINING ###
##################
def get_train_start(phase):
    train_start_dates = {1:'2013-01-01',
                         2:'2013-01-01'}            
    return train_start_dates.get(phase)
    
def get_train_end(phase):
    train_end_dates = {1:'2017-12-01',
                       2:'2020-12-01'}            
    return train_end_dates.get(phase)
    
    
####################
####  VALIDATION ###
####################
def get_val_start(phase):
    val_start_dates = {1:'2017-01-01',
                       2:'2020-01-01'}            
    return val_start_dates.get(phase)
    
def get_val_end(phase):
    val_end_dates = {1:'2018-12-01',
                     2:'2021-12-01'}            
    return val_end_dates.get(phase)


##############
####  TEST ###
##############
def get_test_start(phase):
    test_start_dates = {1:'2018-01-01',
                        2:'2021-01-01'}            
    return test_start_dates.get(phase)
    
def get_test_end(phase):
    test_end_dates = {1:'2019-12-01',
                      2:'2022-12-01'}            
    return test_end_dates.get(phase)