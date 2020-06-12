"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import interpreting_brain_volume, cognitive_function_advice,find_CDR, have_appointment
    
def test_cognitive_function_advice():
    """Tests whether cognitive_function_advice is callable as a function
       Checks whether a string would output based on the given input of a float
       Checks whether a specific input of a float returns back the correct string
    """
    
    assert callable(cognitive_function_advice)
    assert isinstance(cognitive_function_advice(0.86573599), str)
    assert cognitive_function_advice(0.86573599) ==  ("To sustain your healthy cognitive functioning, you should keep learning new things. \
Learn a new skill like doing a puzzle, learn a language. \
Anything to keep the neurons in your brain firing and making new connections. \
Keep up the good work.")
    
    
def test_interpreting_brain_volume():
    """Tests whether interpreting_brain_volume is callable as a function
       Checks whether a string would output based on the given input of a float
       Checks whether a specific input of a float returns back the proper string
    """
    
    assert callable(interpreting_brain_volume)
    brain = interpreting_brain_volume(0.85875571)
    assert isinstance(brain, str)
    assert interpreting_brain_volume(0.85875571) == "Based on your brain volume, your brain is functioning in a healthy manner"

    
def test_find_CDR():
    """Tests whether find_CDR is callable as a function
       Checks whether a string would return based on the given input of a flaot
       Checks whether a specific input of a float returns back the right string
    """
    assert callable(find_CDR)
    assert isinstance(find_CDR(-1.4571406888753655), str)
    assert find_CDR(-1.4571406888753655) == ("Your healthy brain volume and CDR indicates that there exists \
no signs of clinical dementia, which is good")
                

        

        
