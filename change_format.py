### Note Due to the length of the data scraping process, the data was first saved in JSON format in the main.py file, and then the file format was changed in the change_format.py file.
import pandas as pd
df = pd.read_json('emlak_bilgileri.json')

# Boş hücreleri "None" ile doldur
df.fillna('None', inplace=True)

df.to_excel('emlak_bilgileri.xlsx', index=False, engine='openpyxl')

# with open('emlak_bilgileri.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# df = pd.DataFrame(data)

# # CSV dosyasına kaydet
# df.to_csv('emlak_bilgi.csv', index=False, encoding='utf-8')