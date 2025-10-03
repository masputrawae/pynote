# Quick Notes CLI Tools

## Tujuan

- Agar aku bisa nulis catatan cepat di direktori manapun
  Biar lebih cepat tanpa perlu `cd` ke `~/Notes/` hanya untuk menulis catatan cepat/fleeting
- Konsisten format penamaan file dan templates
- Kebutuhan pribadi jadi buat seminimal mungkin agar bisa di pakai cepat
- Mudah auto commit ke git
- Mudah pull dari github

## Kebutuhan

- Buat catatan 0tomatis, dengan templates yang sudah di sediakan
- Format nama catatan 060102151413_judul.md
- Direktori inbox: ~/Notes/inbox/

## Templates

```md
---
tags: ["tag_a"]
lastmod: 2006-01-02T15:14:12+07:00
---

isi catatan
```

```py
import os
from jinja2 import Environment, FileSystemLoader
from datetime import date

# Dapatkan folder tempat file script ini berada (absolute path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Setup environment jinja, loader ambil dari folder BASE_DIR
env = Environment(loader=FileSystemLoader(BASE_DIR))

# Load template dari folder yang sama dengan script
template = env.get_template('template.md')

# Data isi template
data = {
    'tanggal': date.today().strftime("%d-%m-%Y"),
    'daftar_kegiatan': ['Ngoding Python', 'Minum kopi', 'Baca buku'],
    'catatan': 'Hari ini produktif banget!'
}

# Render template
output = template.render(data)

# Simpan hasil di folder dimana kamu menjalankan script sekarang (CWD)
output_file = os.path.join(os.getcwd(), f'catatan_{data["tanggal"]}.md')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Catatan berhasil dibuat di: {output_file}")
```

Fungsi Date untuk template
```
{{ date_time() }}                         {# 2025-10-03 #}
{{ date_time("iso") }}                   {# 2025-10-03T16:12:45+07:00 #}
{{ date_time("%d/%m/%Y") }}              {# 03/10/2025 #}
{{ date_time("%A, %d %B %Y") }}          {# Friday, 03 October 2025 #}
{{ date_time("simple", "2022-12-01") }}  {# 2022-12-01 #}
```
