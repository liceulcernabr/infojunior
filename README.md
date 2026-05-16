# InfoJunior — Site concurs

Site publicat pe **GitHub Pages**, actualizat automat la fiecare push.

---

## 📁 Structura folderelor

```
infojunior/
├── index.html              ← site-ul (nu se modifică manual)
├── data.json               ← generat automat, nu edita manual
├── generate_data.py        ← scriptul care generează data.json
├── rezultate/              ← PDF-uri cu rezultatele concursului
│   └── Rezultate_Basme.pdf
├── lucrari/
│   ├── basme/              ← desene Paint (JPG, PNG)
│   ├── grafica/            ← grafică calculator (JPG, PNG)
│   ├── powerpoint/         ← prezentări (PPTX)
│   ├── soft/               ← soft educațional
│   ├── web/                ← pagini web (ZIP sau HTML)
│   ├── scratch/            ← proiecte Scratch (SB3)
│   ├── programare/         ← soluții C++ (ZIP)
│   └── robotica/           ← imagini/video roboți
└── .github/
    └── workflows/
        └── update-data.yml ← GitHub Actions (rulează automat)
```

---

## ✅ Cum adaugi lucrări (workflow zilnic)

### Varianta A — prin GitHub.com (fără terminal, recomandat)

1. Mergi pe repo-ul tău pe **github.com**
2. Intră în folderul potrivit (ex. `lucrari/basme/`)
3. Click **Add file → Upload files**
4. Trage fișierele primite pe email
5. Click **Commit changes**
6. GitHub Actions rulează automat în ~30 secunde → site-ul se actualizează

### Varianta B — prin terminal (Git)

```bash
# Copiază fișierele în folderul potrivit
cp ~/Desktop/BASME_Scoala_Ion_Maria.png lucrari/basme/

# Adaugă și publică
git add .
git commit -m "Adaug lucrări basme - Școala Ion Creangă"
git push
```

---

## 📄 Cum adaugi rezultate PDF

Pune PDF-ul în folderul `rezultate/` și dă push (ca mai sus).

**Exemplu de denumire:**
```
rezultate/Rezultate_Basme_2026.pdf
rezultate/Rezultate_Programare_2026.pdf
```

---

## 📝 Convenție de denumire fișiere

Urmează convenția din regulament pentru ca titlul să apară corect pe site:

| Secțiune | Format |
|----------|--------|
| Lumea Basmelor | `BASME_Scoala_NumePrenume.png` |
| Grafică | `GRAFICA_Scoala_NumePrenume.jpg` |
| PowerPoint | `PPT_Scoala_NumePrenume.pptx` |
| Soft | `SOFT_Scoala_NumePrenume.zip` |
| Web | `WEB_Scoala_NumePrenume.zip` |
| Scratch | `PROGRAMARE_Scoala_NumePrenume.sb3` |
| Robotică | `ROBOTI_Scoala_NumePrenume.mp4` |

---

## 🚀 Prima configurare (o singură dată)

### 1. Creează repo pe GitHub

```bash
git init
git add .
git commit -m "Prima versiune InfoJunior"
git branch -M main
git remote add origin https://github.com/UTILIZATOR/infojunior.git
git push -u origin main
```

### 2. Activează GitHub Pages

- GitHub → repo → **Settings → Pages**
- Source: **Deploy from a branch**
- Branch: **main** / folder: **/ (root)**
- Save → site-ul apare la `https://UTILIZATOR.github.io/infojunior/`

### 3. Verifică GitHub Actions

- GitHub → repo → **Actions**
- Ar trebui să vezi workflow-ul `Actualizare site InfoJunior`
- La primul push, rulează automat și generează `data.json`

---

## ❓ Depanare

| Problemă | Soluție |
|----------|---------|
| Site-ul nu se actualizează | Verifică **Actions** → dacă workflow-ul a eșuat, click pe el pentru detalii |
| Lucrarea nu apare în galerie | Verifică că fișierul e imagine (JPG/PNG) și e în folderul corect |
| PDF-ul nu se deschide | Verifică că fișierul e în `rezultate/` și are extensia `.pdf` |
| `data.json` e gol | Rulează manual: **Actions → Actualizare site → Run workflow** |
