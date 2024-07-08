![header](header.png)

# Regular Expression for Rule-Based Content Moderation

## About
This project aims to address the taboo expressions in a computer-mediated communication in a company by detecting and censoring specific elements of a message (e.g., *"Shit, I forgot!"* $\rightarrow$ *"\*\*\*\*, I forgot!*)". A rule-based approach with regular expression was considered over a machine learning approach due to its efficient implementation, high explainability (for stakeholders), and high possibility of detecting inappropriate expressions if matching the rules. 

## Content
    .
    ├── README.md                <- The top-level README for using this project.
    ├── data
    │   └── badword_list.csv     <- List of censored words 
    ├── notebook.ipynb           <- The Jupyter notebook to run and explain the code
    └── requirements.txt         <- The requirements file for reproducing the environment.

## Getting Started
To replicate my analysis or explore the data further, kindly follow the following steps:
1. Clone this repository to your local machine.
```bash
git clone https://github.com/LingAdeu/regex-for-content-moderation.git
```
2. Ensure that all necessary dependencies are installed, especially Python and Jupyter Notebook. All libraries are specified on file requirements.txt.
3. Run my Jupyter Notebook file (`*.ipynb`) in [notebook](https://github.com/LingAdeu/regex-for-content-moderation/blob/main/notebook.ipynb) folder to reproduce the code. Alternatively, kindly check this Jupyter Notebook Viewer [URL](https://nbviewer.org/github/LingAdeu/regex-for-content-moderation/blob/main/notebook.ipynb) to see the notebook.

## Feedback
If there are any questions or suggestions for improvements, feel free to contact me here:

<a href="https://www.linkedin.com/in/adelia-januarto/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"/>
  </a>
<a href="mailto:januartoadelia@gmail.com" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/gmail/default.svg"  width="52" height="40" alt="gmail logo"/>
  </a>