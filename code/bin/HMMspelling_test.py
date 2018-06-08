from Model import HMMspelling as HMM
import numpy as np

############### Testing Mispelling HMM model ####################

# List of possible states
states = ('state_1', 'state_2', 'state_3', 'state_4')

# Mapping states into integer dictionary
states_map = {1: 'state_1', 2: 'state_2',
              3: 'state_3', 4: 'state_4'}

# list of possible observations
possible_observations = ('A', 'B', 'C', 'D', 'E')

# The observations that we observe to feed to the model
observations = ('C', 'B', 'B', 'D')

# obs4 = ('B', 'A', 'B')
# observation_tuple = []
# observation_tuple.extend([observations, obs4])
# quantities_observations = [10, 20]

# Matrix of priori probability
start_probability = np.matrix('0.25 0.25 0.25 0.25')

# Matrix of transition in states
transition_probability = np.matrix('0.1 0.3 0.2 0.4 ; 0.8 0.05 0.05 0.1 ; 0.1 0.3 0.1 0.5 ; 0.2 0.5 0.2 0.1')

# Matrix of observations in states
observation_probability = np.matrix('0.1 0.3 0.2 0.1 0.3 ; 0.8 0.05 0.05 0.05 0.05 ; 0.1 0.3 0.1 0.4 0.1 ; 0.1 0.5 0.2 0.1 0.1 ')

# Build the HMM for mispelling check
test = HMM.HMMspelling(states,
                       possible_observations,
                       start_probability,
                       transition_probability,
                       observation_probability)

# Forward algorithm
print("")
print(test.forward(observations))

# Viterbi algorithm
print("")
print(test.viterbi(observations))

# start_prob,em_prob,trans_prob=start_probability,emission_probability,transition_probability
# prob = test.hmm.log_prob(observation_tuple, quantities_observations)
# print("")
# print("Sequence probability with original parameters:")
# print(prob)

# print("applied Baum welch on")
# print(observation_tuple)

# e, t, s = test.hmm.train_hmm(
#     observation_tuple,
#     1000,
#     quantities_observations)

# print("parameters emission,transition and start")
# print(e)
# print("")
# print(t)
# print("")
# print(s)

# prob = test.hmm.log_prob(observation_tuple, quantities_observations)
# print("probability of sequence after %d iterations : %f" % (1000, prob))