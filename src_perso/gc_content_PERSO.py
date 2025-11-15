import csv 
import os #The os module is used to manage paths and directories for saving files.
import matplotlib.pyplot as plt

#STEP A: Read the FASTA file — open it, read each sequence, and return a dictionary with identifier: sequence pairs.

def read_fasta(path): # The path parameter is expected to contain the path to the FASTA file.
    seqs = {} #Create a dictionary to store the final result as {id: sequence}.
    sid = None # Current identifier (e.g., "seq1").
    chunks = [] # Sequence lines to concatenate.

    with open(path, "r", encoding="utf-8-sig") as file: #Open the file named file, read it properly even with special characters, then close it.
        for raw in file: #Each raw line is read one by one from the text.
            line = raw.strip() # Remove spaces and newline characters (\n).
            if not line: # If the line is empty, skip it and move to the next one.
                continue 

            if line.startswith(">"): #Check if the line starts with the > symbol.
                if sid is not None: # Check if a sequence is already being processed (i.e., if a previous identifier has been read).
                                    # If so, it means the current sequence must be saved before starting a new one.
                    seqs[sid] = "".join(chunks) #Dictionary containing the sequence name (sid) associated with its complete sequence.
                    # Start a new sequence.
                sid = line[1:].split()[0] #Take the line and remove the first character (index 0), i.e., the > symbol.
                chunks = []
            else:
                chunks.append(line.upper())
            
    if sid is not None: 
                seqs[sid] = "".join(chunks)   
    return seqs 

#STEP B: Calculate the GC percentage for a single sequence.
def gc_percent(seq: str) -> float: # Compute the percentage of G and C in a sequence (string) and return it as a floating-point value.
    if not seq: # If the sequence is empty.
        return 0.0 # To avoid any calculation errors.
    seq = seq.upper() # Return the entire sequence in uppercase.
    g = seq.count("G")
    c = seq.count("C")
    denom =len(seq) #Total sequence length (used as the denominator in the calculation).
    return 100.0 * (g + c) / denom

# Export CSV
def save_gc_csv(seqs, out_path: str) -> None:
    # Save a CSV file containing ID, length, and GC% for each sequence.
    with open(out_path, "w", newline="", encoding="utf-8") as file:
    # Open a file in write mode ("w") using UTF-8 encoding, ready for CSV output.
        writer = csv.writer(file) # Create a CSV writer object to write data in column format.
        writer.writerow(["id", "length", "GC_percent"]) # Write the header row (column names)
        for sid, seq in seqs.items(): # Iterate over each sequence as in the test example.
            gcp = gc_percent(seq) # Compute the GC percentage.
            writer.writerow([sid, len(seq), f"{gcp:.4f}"]) #Write a row containing the identifier, length, and GC% formatted to four decimal places.


#Build a bar chart of GC% per sequence and save it as a PNG file.
def plot_gc_bar(seqs, out_path: str) -> None:
    ids = []
    gcs = []
    for sid, seq in seqs.items():
        ids.append(sid)
        gcs.append(gc_percent(seq))
    
    plt.figure(figsize=(6,4)) #Create a figure with a width of 6 inches and a height of 4 inches for plotting the chart.
    bars = plt.bar(ids, gcs) # Draw a bar chart with sequence IDs on the x-axis and GC% on the y-axis.
    plt.ylabel("GC %")
    plt.title("GC content per sequence")
    plt.xticks(rotation=45, ha="right") #Rotate sequence labels by 45° and align them to the right for better readability.
    plt.tight_layout() #Automatically adjust the layout to prevent labels or text from being cut off.
    plt.savefig(out_path, dpi= 150) #Save the plot as a PNG file with high quality (150 DPI).
    plt.close()


