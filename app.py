import streamlit as st
import re       # for regex pattern
import csv      # for importing word list

# build function to censor message
def censor_message(message, blacklisted_words):
    # specify regex pattern for all bad words
    pattern = '|'.join(map(re.escape, blacklisted_words))
    # replace offensive words and phrases with asterisks of the same length
    censored_message = re.sub(pattern, lambda m: '*' * len(m.group()), message, flags=re.IGNORECASE)
    return censored_message

# load bad word list
def load_wordlist(file_path):
    wordlist = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            wordlist.extend(row)
    # remove empty strings from the bad word list
    wordlist = list(filter(None, wordlist))
    return wordlist

# load the list of bad words
wordlist = load_wordlist('data/badword_list.csv')

# streamlit app setup
st.title("Taboo Expression Censorship Tool")
st.write("This tool identifies and censors taboo expressions in the input message.")

# user input
user_message = st.text_area("Enter a message to check:")

if st.button("Check Message"):
    if user_message:
        censored_message = censor_message(user_message, wordlist)
        st.write("**Original Message:**")
        st.write(user_message)
        st.write("**Censored Message:**")
        st.write(censored_message)
    else:
        st.warning("Please enter a message to be censored.")
