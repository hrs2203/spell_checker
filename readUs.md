# RESEARCH TRACKING SYSTEM
> Final Project, Information Retrival, Semester 5

## Introduction
Tracking research in any niche topic is a daunting task. We often get lost in the myriad of citations and references for any paper of interest.
We have created a library for Retrieving Relevant Research papers and tracking research on topics like Neural Ordinary Differential Equations. 
Our system, based on a user entered query, retrieves the information of a paper form Arxiv and Semantic Scholar. The user then can look for the citations and the references for that paper. Our system will automatically get these and present them in a ranked fashion. At the same time the system will also keep a track of the choice of papers requested by the user and create a forward (Citation) and backward (Reference) branches respectively.
This will help in better keeping track of the flow of ideas and discovering new ideas in the domain.
At the same time, by looking at the References, this will help in understanding how ideas have been developing to get to the present point in the research.

## Tasks Implimented

- Web Crawler ( Raahul Singh )
- Creating Inverted Index ( Sayam Kumar )
- Spell Check system ( Hrishabh Pandey )
- Tf-IDF ( Sayam Kumar )
- Pseudo relevance feedback ( Hrishabh Pandey )
- Citation graph ( Raahul Singh )

## How it works
```python3
from query import QueryCheck

if __name__ == "__main__":
    queryChecker = QueryCheck("distance of sun from eart")

    # List of all word corrections
    print("====== Correction Word wise =================")
    wordCorrections = queryChecker.getCorrectedWords()
    for wordObj in wordCorrections:
        print(wordObj)
    print("=============================================")

```

## Submitted By
- Sayam Kumar , S20180010158
- Raahul Singh , S20180010141
- Hrishabh Pandey , S20180010064
