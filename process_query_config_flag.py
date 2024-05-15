import pandas as pd

# Path to the CSV file
csv_file_path = 'query-config.csv'

# Set of processing keys
processing_keys_to_update = {406, 409, 410, 411, 412, 413, 415, 416, 417, 418, 419, 420, 308, 312, 201, 202, 323, 203, 204, 205, 206, 212, 333, 334, 214, 215, 216, 337, 338, 341, 100, 342, 343, 224, 345, 347, 348, 349, 351, 352, 353, 354, 11, 12, 13, 240, 247, 21, 26, 28, 251, 30, 32, 381, 384, 42, 44, 49, 391, 392, 395, 396, 397, 50, 54, 59, 164, 166, 289, 60, 62, 63, 67, 68, 290, 291, 177, 178, 70, 72, 185, 186, 187, 188, 189, 81, 85, 86, 89, 190, 193, 194, 195, 196, 199}  # Add your processing keys here

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Update the 'skipQueryExecution' column based on the processing keys
df.loc[df['processingKey'].isin(processing_keys_to_update), 'skipQueryExecution'] = 'BOOLEAN_CONFIG_FALSE'
df.loc[~df['processingKey'].isin(processing_keys_to_update), 'skipQueryExecution'] = 'BOOLEAN_CONFIG_TRUE'

# Save the updated DataFrame back to the CSV file
df.to_csv(csv_file_path, index=False)
