"""A collection of function for doing my project."""

# Age is a global variable where it would be easily called so that the question of the user's age does not have to asked multiple times 
age = 0
def want_cognitive_advice():
    """This function is made to asks the user if the want advice in 
    regards to their cognitive functioning
    
    Returns
    -------
    Y : Float
        A float that contains the calculated brain volume
    """
    
    message = input("Do you want to get helpful advice based on your stage of cogntive functioning (yes/no)?: ")
    
    if message == "yes":
        # Y is the brain volume that is taken into the cognitive_function_advice as the input in order to produce the necessary string
        # The global variable of age is called so that the user does not have to input their age again
        age
        # The linear regression equation is called so that it can be defined for the "cognitive_function_advice" function
        Y = (-0.00207326)*(float(age))+0.89814765
        print(Y)
        return float(Y)
        #This function below would be called in order for the input of Y to be taken in  
        cognitive_function_advice(Y)       
    

def cognitive_function_advice(Y):
    """This function creates strings of helpful advice for the user based on
    their threshold of cognitive functioning
    
    Parameters
    ----------
    Y : a float
        Float to establish brain volume and create a threshold
        for each level of cognitive functioning
    Returns
    -------
    out : string
        Returns an interpretation and evaluation of 
        of one's cognitive functioning based on their unique brain size
    """
    # Y represents the brain volume (in float form) from the "interpreting_brain_volume" function
    # Each conditional statment check if the given brain volume is within the certain calculated threshold in order to decipher and interpret cognitive functoining
    if Y > .77:
        out = ("To sustain your healthy cognitive functioning, you should keep learning new things. \
Learn a new skill like doing a puzzle, learn a language. \
Anything to keep the neurons in your brain firing and making new connections. \
Keep up the good work.")

    elif Y > .695 and Y < .77:
        out = ("Although you have some mild cognitive impairment, \
you can get cognitive rehabilitation that focuses on memory training \
along with a balanced diet and physical exercise which all can help slow down cognitive decline")

    elif Y < .695:
        out = ("It may be best to go see your primary doctor or neuropsychologist \
and get professional treatment for your potential severe impairment to your cognitive functioning.")

    else:
        out = "Can't interpret this, please input your given brain volume"

    print(out)
    return out

def want_brain_volume():
    """Calculates the brain volume of the user, using the user's age
    
    Returns
    -------
    Y: Float
        Returns the calculated brain volume in float form
    """
    age = input("What is your age?: ")
    # The input of age is taken in as a dependent variable in a calculated linear regression equation that has been generated on the basis of age and brain volume
    # X or float(age) represents the age input and the Y (output) represents the calculated brain volume 
    Y = (-0.00207326)*(float(age))+0.89814765
    print("Your brain volume is "+ str(round(Y,3)))
    print("This means " + str(round(Y,3)*100) + "% of your cranial space is brain tissue")
    
    return float(Y)

    cognitive_function_advice(Y)
    

def interpreting_brain_volume(Y): 

    """Evaluates and interprets one's brain volume through the input of one's age.   
    
       Parameters
       ----------
       Y : float
           A float of one's already calulated brain volume 
           
       Returns
       -------
       output : string
           Returns an interpretation of one's state of health when it comes to brain volume        
    """        

    # Because of the given threshold for brain volume (specified by a float), each conditional achieves an appropriate interpretation of one's brain volume (Y)  
    if Y > .77:
        
        output = "Based on your brain volume, your brain is functioning in a healthy manner"
 
    elif Y > .695 and Y < .77:
        
        output = "Based on your brain volume, your cognitve functioning could be worrisome"
    
    elif Y < .695:
        
        output = "It seems like cognitive functioining may be greatly impaired based on your brain volume"
        
    print(output)
            
    return output    
    
def want_CDR():
    """Determines whether the user wants to learn their Clinical Dementia Rating (CDR)
       on the basis of one's given brain volume
       
       Returns
       -------
       CDR: float
           A float containing the calculated CDR
    """
    input_message = input("Do you want to learn your Clinical Dementia Rating (CDR)"
                          + "on the basis of your brain volume (yes/no)?")
    if input_message == "yes":
        
        nWBV = input("Please input your given brain volume (the one in float form): ")

        CDR = (float(nWBV)-0.76697562)/-0.06298643
        print("Your CDR is " + str(round(CDR,3)))
        
        return float(CDR)
        find_CDR(CDR)
        
#     else:
#         print("Okay. That's fine")
                
    
def find_CDR(CDR):
    """Evaluates and calculates one's Clinical Dementia Rating (CDR)
    on the basis of one's given brain volume
    
    Parameters
    ----------
    CDR : float
        A float that that helps establishes the state of one's clinical dementia rating
    
    Returns
    --------
    outcome : string
        Returns a series of statements that interprets one's given Clinical
        Dementia Rating based on establsihed thresholds for CDR
    """

    if CDR < 0:
        outcome = ("Your healthy brain volume and CDR indicates that there exists \
no signs of clinical dementia, which is good")

    if CDR > 0 and CDR < 0.75:
        outcome = ("Your brain volume and CDR indicates that you may have mild impairment \
when it comes to your memory")

    if CDR > 0.75:
        outcome = ("You may have a clear signs of moderate to severe cognitive impairment \
on the basis of your brain volume and CDR")
    
    print(outcome)
    
    return outcome
   
    
def have_appointment():
    """Main function to run the chatbot"""
        
    output = input("Do you want to know your brain volume (yes/no)?")

    if output == "yes":
        # Only this function called because within this function, the other functions (find_CDR, cognitive_function_advice) are called within the brain volume function itself
        Y = want_brain_volume()
        interpreting_brain_volume(Y)

        CDR = want_CDR()
        # If the user wants to learn their CDR and inputs their brain volume, CDR will be calculated and return as a number and thus is not None and will continue on with the appointment
        if CDR != None:

            find_CDR(CDR)

            want_cognitive_advice()
            cognitive_function_advice(Y)
            print("Thank you for attending this appointment, that would be $200 please")
        # If the CDR is None (meannig that the user responds with not wanting CDR), then it prints out the following statement
        else:

            print("Okay. That's fine. Thank you for attending this appointment, that would be $200 please") 
            
    else:

        print("Okay. That's fine. Thank you for attending this appointment, that would be $200 please")


    

    