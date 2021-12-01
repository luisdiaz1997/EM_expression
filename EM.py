import numpy as np

class EM():
    def __init__(self, reads, isoforms):
        self.A = isoforms.T
        self.C = reads.reshape(1, -1)
        self.O = np.ones(self.A.shape[0])[:, None]
        self.scores = [self.log_prob()[0]]
     
    def expected(self):
        return np.dot(self.O, self.C) * self.A/np.dot(self.O.T, self.A)

    def em_step(self):
        expected_m = self.expected()
        O = np.sum(expected_m, axis=1, keepdims=True)
        return O

    def log_prob(self):
        return np.dot(self.C, np.dot(self.A.T, self.O)) - sum(np.dot(self.A.T, self.O))
    
    def train(self, steps=20):
#         self.scores.append(log_prob(O, C, A)[0])
#         iterations = 10
        for i in range(steps):
            self.O = self.em_step()
            self.scores.append(self.log_prob()[0])