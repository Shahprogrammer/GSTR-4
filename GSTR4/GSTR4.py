from pandas import read_csv
from Company import GST_Company
COMPANIES={}
def generate_dataframe(input="./Input.csv"):
    df=read_csv(input)
    df.fillna(0,inplace=True)
    df.rename(columns={"GSTIN of supplier *": "GSTNO", "Place of supply *": "POS", "Supply type *": "ST", 'Rate *': "RATE", 'Taxable value': "TAXABLE", 'Integrated tax': "IGST", 'Central tax': "CGST", 'State/UT tax': "SGST", 'Cess': "CESS"},inplace=True)
    return df


def remove_duplicates(df):
    return df.drop_duplicates(subset=['GSTNO', 'RATE'], keep='first').to_dict(orient='records')


def generate_company(df_dict):
    global COMPANIES
    for comp in df_dict:
        COMPANIES.update({comp['GSTNO']+str(comp['RATE']):GST_Company.from_dict(comp)})
    return None

def update_company_invoices(df_dict):
    global COMPANIES
    for invoice in df_dict:
        COMPANIES[invoice['GSTNO']+str(invoice['RATE'])].updata_invoice(invoice['TAXABLE'],invoice['CGST'],invoice['SGST'],invoice['IGST'],invoice['CESS'])


def output(output="./Output.csv"):
    from csv import writer
    global COMPANIES
    with open(output,'w',newline="")as file:
        csv=writer(file)
        csv.writerow(['GSTIN of supplier *', 'Place of supply *', 'Supply type *',
            'Taxable value', 'Rate *', 'Integrated tax', 'Central tax',
            'State/UT tax', 'Cess','Total Value'])
        for comp in COMPANIES.values():
            q=comp.generate_output()
            csv.writerow(q)
    
def main():
    df=generate_dataframe()
    generate_company(remove_duplicates(df))
    update_company_invoices(df.to_dict(orient="records"))
    output()
    return None

if __name__ == "__main__":
    main()