import torch
from model import model

X = torch.tensor(
    [
        [
            2,
            -1,
            1,  # delayed
            -1,
        ]
    ]
)

X_masked = torch.masked.MaskedTensor(X, mask=(X != -1))

states = (
    ("rain", ["none", "light", "heavy"]),
    ("maintenance", ["yes", "no"]),
    ("train", ["on time", "delayed"]),
    ("appointment", ["attend", "miss"]),
)

# Calculate predictions
predictions = model.predict_proba(X_masked)

# Print predictions for each node
for (node_name, values), prediction in zip(states, predictions):
    if 1 in prediction[0]:
        print(f"{node_name}: {values[(prediction[0] == 1).nonzero(as_tuple=True)[0]]}")
    else:
        print(f"{node_name}")
        for value, probability in zip(values, prediction[0]):
            print(f"    {value}: {probability:.4f}")
