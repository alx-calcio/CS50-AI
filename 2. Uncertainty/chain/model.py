from pomegranate import *
from pomegranate.distributions import *
from pomegranate.markov_chain import MarkovChain

# Define starting probabilities
start = Categorical([[0.5, 0.5]])

# Define transition model
transitions = ConditionalCategorical([[[0.8, 0.2], [0.3, 0.7]]])

# Create Markov chain
model = MarkovChain([start, transitions])

# Sample 50 states from chain
print(model.sample(50))
