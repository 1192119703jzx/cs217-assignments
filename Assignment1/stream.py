import streamlit as st
import json
import os
from note import NoteBook
import pandas as pd

json_file_path = 'notebook.json'
if not os.path.exists(json_file_path):
    with open(json_file_path, 'w') as file:
        json.dump({}, file)
notebook = NoteBook(json_file_path)

if 'notebook' not in st.session_state:
    st.session_state.notebook = notebook
if 'selected_result' not in st.session_state:
    st.session_state.selected_result = None
if 'switch' not in st.session_state:
    st.session_state.switch = False

# Sidebar
st.sidebar.header("Search term")
search_term = st.sidebar.text_input("", placeholder="Enter your search term here")
st.sidebar.markdown("**Notes** (filtered for search term)")

if st.session_state.notebook.book:
    content_match = st.session_state.notebook.search_string(search_term)
    name_match = st.session_state.notebook.string_string_in_name(search_term)
else:
    content_match = st.session_state.notebook.show_all_notes()
    name_match = st.session_state.notebook.show_all_notes()

if search_term:
    st.sidebar.markdown("**Content match**")
    for i, note in enumerate(content_match):
        if st.sidebar.button(note, key=f"content_match_{i}"):
            st.session_state.selected_result = note
            st.session_state.switch = True
            st.rerun()
    st.sidebar.markdown("**Name match**")
    for i, note in enumerate(name_match):
        if st.sidebar.button(note, key=f"name_match_{i}"):
            st.session_state.selected_result = note
            st.session_state.switch = True
            st.rerun()
else:
    st.sidebar.markdown("**All notes**")
    for i, note in enumerate(notebook.show_all_notes()):
        if st.sidebar.button(note, key=f"all_notes_{i}"):
            st.session_state.selected_result = note
            st.session_state.switch = True
            st.rerun()

# Main
st.title("NoteBook")
tab1, tab2 = st.tabs(["Show note", "Add note"])

with tab1:
    if st.session_state.switch:
        st.session_state.switch = False
        selecte = st.session_state.selected_result
    else:
        selecte = st.selectbox("Select note", st.session_state.notebook.show_all_notes() if st.session_state.notebook.book else ["No notes yet"])
    if selecte != "No notes yet":
        st.markdown(f"#### {selecte}")
        st.write(st.session_state.notebook.search_name(selecte))
    if st.button("Back"):
        st.session_state.selected_result = None
        st.rerun()

with tab2:
    title = st.text_input("Title")
    content = st.text_area("Content")
    if st.button("Add note"):
        if title and content:
            st.session_state.notebook.create_note(title, content)
            st.write("Note has been successfully added")
            st.rerun()
        else:
            st.write("Both title and content are required")