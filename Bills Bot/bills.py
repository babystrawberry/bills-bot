import pandas as pd
df = pd.read_csv(r'/Users/sahanasantosh/Documents/Bills Bot/bills - Sheet1.csv')
df['doc-number'] = df['doc-number'].str.replace(' ', '', regex=False)
df['Sponsors'] = df['Sponsors'].str.replace(r'(\d+(?:st|nd|rd|th))', r'\1\n', regex=True)
df['Committees'] = df['Committees'].str.replace(r'(House Committee:.*?)(Senate Committee:)', r'\1\n\2', regex=True)
df['Committees'] = df['Committees'].str.replace(':', ': ')

def bill_finder(billnum):
    billnum = billnum.replace(" ", "")
    billnum = billnum.upper()
    bill= df.loc[df['doc-number'] == billnum]
    bill_list = bill.values.tolist()
    if len(bill_list) == 1:
        return bill_list[0] 
    return bill_list 

