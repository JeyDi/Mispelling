from HMMispelling.core import model
import numpy as np

states = ('A', 'B', 'E')
possible_observation = ('A', 'B', 'E')

start_prob = np.matrix('0.3 0.3 0.4')
transition_prop = np.matrix('0.3 0.5 0.2; 0.6 0.1 0.3; 0.4 0.4 0.2')
emission_prop = np.matrix('0.7 0.1 0.2; 0.2 0.6 0.2; 0.1 0.1 0.8')

mispelling_modes = model.MispellingHMM(start_probability=start_prob, transition_matrix=transition_prop,
                                       hidden_states=states, observables=possible_observation,
                                       emission_matrix=emission_prop)

obs1 = ('A', 'B', 'B', 'B')

x = mispelling_modes.viterbi(obs1)
print(x)