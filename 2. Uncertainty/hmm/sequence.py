from model import model
import numpy

# Observed data
observations = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella",
]
sequence = numpy.array(
    [[[["umbrella", "no umbrella"].index(observation)] for observation in observations]]
)
# Predict underlying states
predictions = model.predict(sequence)
for prediction in predictions[0]:
    print(["sun", "rain"][prediction.item()])
