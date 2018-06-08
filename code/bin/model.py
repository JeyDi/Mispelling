import hidden_markov
import numpy as np
import pandas as p


#Class to launch and use the hidden_markov library with our data
#It's a wrapper of the library
class HMM():
    
    #Class constructor
    def __init__(self,states,evidence,probability,transition,emission):
        #Hidden states of the net
        self.states = states
        #Evidence or observable
        self.evidence = evidence
        #starting probability for the initialization
        self.probability = probability
        #matrix for transition probability
        self.transition = transition
        #matrix of emission
        self.emission = emission
    
        #Call the hidden_markov library model and initialize the model
        self.model = hidden_markov.hmm(states,evidence,probability,transition,emission)

    ##FORWARD FUNCTION
    def forward(self,sequence):
        return self.forward(sequence)

    ##VITERBI FUNCTION to filter the net
    def viterbi(self,sequence):
        return self.model.viterbi(sequence)
        
        