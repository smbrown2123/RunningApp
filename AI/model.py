import pandas as pd

import torch
import torch.optim as optim

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from net import *

# import data and drop data column
data = pd.read_csv('AI/training.csv')
data = data.drop(columns=['date'])

# Normalize the numerical features
scaler = StandardScaler()
data[['distance', 'time', 'pace']] = scaler.fit_transform(data[['distance', 'time', 'pace']])

X = data.drop(columns=['label'])  # Features (distance, time, pace)
y = data['label']  # Labels (target variable)

# split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# convert to tensors
X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.long)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.long)

# Define the model ()
input_size = X_train.shape[1]  # Number of features (distance, time, pace)
hidden_size = 64  # You can experiment with this
output_size = 1  # For binary classification

model = NeuralNet(input_size, hidden_size, output_size)

# define loss function and optimizer
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 1000
batch_size = 64

for epoch in range(epochs):
    model.train()

    # Loop through the data in batches
    for i in range(0, len(X_train_tensor), batch_size):
        inputs = X_train_tensor[i:i+batch_size]
        labels = y_train_tensor[i:i+batch_size].unsqueeze(1).float()  # Make sure labels are float for BCELoss
        
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
    
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
    
model.eval()

with torch.no_grad():
    outputs = model(X_test_tensor)
    predicted = (outputs >= 0.5).float()  # Convert probabilities to class predictions
    accuracy = (predicted.squeeze() == y_test_tensor).sum().item() / len(y_test_tensor)
    print(f'Accuracy on test set: {accuracy * 100:.2f}%')