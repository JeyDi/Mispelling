# import editdistance as ed
import numpy as np
from math import log
from collections import Counter
 
class HMMModel(object):
 
    def viterbi(self, sequence, states, initial_frequencies, state_matrix, emission_matrix):
            '''
            Handly Viterbi Algorithm:
            
            Task: generare la sequenza di stati più probabile.
            Input: Parametri del modello ridotto e sequenza di osservazioni
            
            '''
            
            k = len(states)
            t = len(sequence)
            T1 = np.zeros((k,t))
            T1[:,0] = initial_frequencies*emission_matrix[:,0]
            T2 = np.zeros((k,t))
            for i in range(1,t):
                for j in range(k):
                    temp = [T1[x,i-1]*state_matrix[x,j] for x in range(k)]
                    T1[j,i] = emission_matrix[j,i]*max(temp)
                    T2[j,i] = temp.index(max(temp))
            Z = np.zeros(t)
            X = [""]*t
            Z[t-1] = list(T1[:,t-1]).index(max(T1[:,t-1]))
            X[t-1] = states[int(Z[t-1])]
            for i in range(t-1,0,-1):
                Z[i-1] = T2[int(Z[i]),i]
                X[i-1] = states[int(Z[i-1])]
            return (X, T1, T2)