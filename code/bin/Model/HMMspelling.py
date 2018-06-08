import hidden_markov


class HMMspelling():
    def __init__(self, states, possible_observations, start_probability, transition_matrix, observation_matrix):
        self.states = states
        self.possible_observations = possible_observations
        self.start_probability = start_probability
        self.transition_matrix = transition_matrix
        self.observation_matrix = observation_matrix

        self.hmm = hidden_markov.hmm(
            states=states,
            observations=possible_observations,
            start_prob=start_probability,
            trans_prob=transition_matrix,
            em_prob=observation_matrix)

    def viterbi(self, observation_sequence):
        return self.hmm.viterbi(observation_sequence)

    def forward(self, observation_sequence):
        return self.hmm.forward_algo(observation_sequence)
