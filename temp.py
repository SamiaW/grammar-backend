import spacy

job_description = '''
Senior Angular Developer - Waterloo

Waterloo, Ontario

Must be currently residing in North America.


Looking for either locals or those who would be willing to relocate (probably back to the office in 3-9 months). Client will cover relocation expenses.
• Fully remote till end of pandemic
• Work permit would work
• Permanent role, not a contract


Required Knowledge, Skills, and Abilities: (Submission Summary):

1. 5+ years of relevant experience in the field

2. Hands on experience with most of the following: (Please indicate # of years experience in each)

a. Angular

b. Extensive knowledge of Rxjs and state management

c. Understanding of MVC, MVVM, MVP patterns

d. Core JavaScript

e. CSS, HTML, Responsive and Adaptive web design

f. Consuming and understanding of RESTful interfaces

g. SDLC and CI/CD

h. Unit testing

i. Clean code concepts
'''

skills = ['Java', 'Python', 'JavaScript', 'Angular', 'HTML']

nlp = spacy.load("en_core_web_md")

threads_array = []

match_dictionary = {}

popular_languages = ['angular', 'html', 'css', 'javascript', 'java', 'react', 'php', 'go', 'scala', 'c#', 'c', 'c++'
                     '.NET', 'es6', 'ecmascript', 'express', 'node.js', 'ruby', 'rails', 'python', 'flask', 'django', 'spring',
                     'vue', 'bootstrap', 'scss', 'less', 'typescript', 'react native', 'android', 'ios', 'jquery',
                     'swift', 'docker', 'jenkins', 'kubernetes', 'aws', 'azure', 'gcp', 'google cloud platform',
                     'mocha', 'selenium', 'jest', 'mysql', 'postgresql', 'mongodb', 'heroku', 'sql', 'firebase'
                     , 'backbone', 'marionette']

def description_search(skills=None, job_description=""):
    if skills is None:
        skills = []

    match_dictionary = {}
    doc = nlp(job_description)
    for token in doc:
        if token.text.lower() in popular_languages:
            if token.text not in match_dictionary:
                match_dictionary[token.text] = {}
                for skill in skills:
                    if token.text == skill:
                        match_dictionary[token.text][skill] = str(1)
                    else:
                        doc2 = nlp(skill)
                        print(token.text, skill, token.similarity(doc2[0]))
                        match_dictionary[token.text][skill] = str(token.similarity(doc2[0]))
                match_dictionary[token.text] = dict(sorted(match_dictionary[token.text].items(), key=lambda item: item[1], reverse=True))

    return match_dictionary

retval = description_search(skills, job_description)
print(retval)