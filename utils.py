import requests
import openai
import os
from ete3 import Tree, TreeStyle
import matplotlib.pyplot as plt
from io import StringIO
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

def search_uniprot(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    res = requests.get(url)
    if res.ok:
        lines = res.text.splitlines()
        return ''.join(lines[1:])
    return None

def annotate_sequence(sequence):
    # Заглушка для аннотаций (Pfam/GO/KEGG/OMA/AlphaFold можно подключить отдельно)
    return {
        "Pfam": ["Mock domain A", "Mock domain B"],
        "GO Terms": ["GO:0005524", "GO:0004672"],
        "KEGG": ["hsa00010", "hsa00020"],
        "AlphaFold": "https://alphafold.ebi.ac.uk/entry/FAKE123"
    }

def build_phylo_tree(sequence):
    # Фиктивное дерево
    t = Tree()
    for i in range(5):
        t.add_child(name=f"Species_{i}", dist=random.uniform(0.1, 1.0))

    ts = TreeStyle()
    ts.show_leaf_name = True

    fig = plt.figure(figsize=(6, 4))
    t.render("%%inline", w=400, units="px", tree_style=ts)
    return fig

def generate_protein_description(sequence: str, openai_api_key: str) -> str:
    import openai
    openai.api_key = openai_api_key

    prompt = f"""Provide a functional summary for the following protein sequence:
{sequence}
Only output a short paragraph of 2–3 sentences in plain English, suitable for a biology researcher."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=300,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating description: {e}"
