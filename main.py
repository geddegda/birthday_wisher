import datetime as dt
import random
import os, re
import pandas as pd
import blast

def get_emails_templates():
    files = [f for f in os.listdir('./letter_templates') if os.path.isfile(f'./letter_templates/{f}')]
    return files
    
df = pd.read_csv('birthdays.csv')

for index, row in df.iterrows():
    if row['month'] == dt.datetime.today().month:
        if row['day'] == dt.datetime.today().day:
            name_person = row['name']
            print(f'It is {name_person} birthday today, just fyi')
            file_email_selection = random.choice(get_emails_templates())
            with open(f'./letter_templates/{file_email_selection}') as f:
                updated_text = re.sub(re.escape('[NAME]'), row['name'], f.read())
                print(updated_text)
            blast.send_email(content=updated_text, recipient= row['email'])
