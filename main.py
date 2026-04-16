from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

data = extract_data()

cleaned = transform_data(data)

print("Sample:", cleaned[0])  # check output

load_data(cleaned)