# 🧬 Protein Analyzer

This is a Streamlit-based web application for searching and analyzing amino acid sequences using online databases like UniProt, Pfam, KEGG, Ensembl, and AlphaFold.

## 🔍 Features

- Search by UniProt ID or upload FASTA file
- Interactive UI for sequence visualization
- Auto-annotation using external databases (Pfam, GO, KEGG, OMA, AlphaFold)
- Generate protein descriptions using OpenAI API
- Build phylogenetic tree from similar sequences
- Web deployment via Render or local Docker

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Docker

```bash
docker build -t protein-analyzer .
docker run -p 8501:8501 protein-analyzer
```

## 🌐 Deploy on Render

1. Upload this project to GitHub
2. Go to https://render.com
3. Create new Web Service → Use Docker → Connect GitHub
4. Add environment variable `OPENAI_API_KEY`

## 📂 Input

- Accepts UniProt IDs (e.g., `P69905`)
- Accepts `.fasta` files

## 🧠 Powered by

- [UniProt](https://www.uniprot.org/)
- [KEGG](https://www.genome.jp/kegg/)
- [Pfam](https://pfam.xfam.org/)
- [OMA](https://omabrowser.org/)
- [AlphaFold DB](https://alphafold.ebi.ac.uk/)
- [OpenAI](https://platform.openai.com/)

## 📄 License

MIT License
