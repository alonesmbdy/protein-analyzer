import streamlit as st
from Bio import SeqIO
from utils import search_uniprot, annotate_sequence, build_phylo_tree, generate_protein_description

st.set_page_config(page_title="Protein Analyzer", layout="wide")

st.title("🔬 Protein Sequence Analyzer")

input_type = st.radio("Choose input type", ["UniProt ID", "Upload FASTA"])
sequence = None

if input_type == "UniProt ID":
    uniprot_id = st.text_input("Enter UniProt ID (e.g., P68871)")
    if uniprot_id:
        sequence = search_uniprot(uniprot_id)
elif input_type == "Upload FASTA":
    fasta_file = st.file_uploader("Upload FASTA file", type=["fasta", "fa"])
    if fasta_file:
        seq_record = next(SeqIO.parse(fasta_file, "fasta"))
        sequence = str(seq_record.seq)

if sequence:
    st.subheader("🔎 Sequence")
    st.code(sequence, language="text")

    st.subheader("🧠 OpenAI Description")
    with st.spinner("Generating description..."):
        st.markdown(generate_protein_description(sequence))

    st.subheader("🧬 Annotations")
    st.json(annotate_sequence(sequence))

    st.subheader("🌿 Phylogenetic Tree")
    tree_fig = build_phylo_tree(sequence)
    st.pyplot(tree_fig)