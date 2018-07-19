import os
# import utility
from configparser import ConfigParser
from models_IO import io_model
from generate_model import create_model
from generate_model import model

# Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def launch_model_creation(message,input_dicts,input_layout,input_dict_name):
    
    print(message)

    #Build a merged dictionary to train the model
    input_dict_path = create_model.compute_dictionary(input_dicts)

    #Train the model
    model, states, observation, start_prob, transition, emission = create_model.generate_model(
            input_dict_path)
            
    # Output the model
    io_model.save_model(input_dict_name, states, observation, start_prob, transition, emission)

    return model
    
def existsModel(input_dicts):
    config = ConfigParser()
    config.read('../config.ini')

    input_dict_name = "".join(input_dicts)

    # Check if the model already exists
    if io_model.check_model(input_dict_name):
        return True
    else:
        return False


def tryViterbi(inputString,input_dicts):

    config = ConfigParser()
    config.read('../config.ini')

    # Set to true for recomputing the model even if it exists
    force_model_computing = False

    # Name of qwerty layout Json
    input_layout = 'qwerty_simple'

    # input_dicts = []
    # # Choose the dicts to append as input
    # input_dicts.append('tweet_result_MercedesAMG')
    # input_dicts.append('tweet_result_rogerfederer')
    # input_dicts.append('tweet_result_realDonaldTrump')
    # input_dicts.append('tweet_result_Forbes')
    # #input_dicts.append('text_for_testing')

    # Build the dictionary name
    input_dict_name = "".join(input_dicts)


    if not force_model_computing:
        # Check if the model already exists
        if io_model.check_model(input_dict_name):

            print("Model already existing, retrieving the elements...")

            # Import model elements
            states, observation, start_prob, transition, emission = io_model.import_model(
                input_dict_name)

            # Rebuild the model
            model = create_model.generate_model_with_input(
                states, observation, start_prob, transition, emission)

            print("Model restored!")

        else:
            model = launch_model_creation("Model not existing, ready to compute it!",input_dicts,input_layout,input_dict_name)
    else:
        model = launch_model_creation("Force recomputing enable, computing the model...",input_dicts,input_layout,input_dict_name)

    result = model.viterbi(list(inputString))
    return "".join(result)


#print(tryViterbi("baok"))