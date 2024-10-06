from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.hmm import DenseHMM

# Observation model for each state
sun = Categorical([[0.2, 0.8]])
rain = Categorical([[0.9, 0.1]])

model = DenseHMM()

model.add_distributions([sun, rain])

# Start
model.add_edge(model.start, sun, 0.5)
model.add_edge(model.start, rain, 0.5)

# Transition model
model.add_edge(sun, sun, 0.8)
model.add_edge(sun, rain, 0.2)
model.add_edge(rain, rain, 0.7)
model.add_edge(rain, sun, 0.3)
