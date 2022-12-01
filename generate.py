import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

#names = ["ADMIN", "ADMIN", "ADMIN", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER"];
names=["samarth","sanjay","sanmat","sanath","shamith","sathwick","manu","sonu","ronu"];
usernames = ["samarth","sanjay","sanmat","sanath","shamith","sathwick","manu","sonu","ronu"];
passwords = ["samarth","sanjay","sanmat","sanath","shamith","sathwick","manu","sonu","ronu"];

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/  "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)