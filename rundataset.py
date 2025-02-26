from torch.utils.data import Dataset
import pandas as pd 

class RunDataset(Dataset):
    def __init__(self, csv_data):
        self.df = pd.read_csv(csv_data)
        
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        pace = self.df.pace[idx]
        distance = self.df.distance[idx]
        label = self.df.label[idx]
  
        return distance, pace, label