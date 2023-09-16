Welcome to the website for *Applied Mathematics and Informatics In Drug
Discovery* (AMIDD), the course series running at the Department of Mathematics
and Informatics, University of Basel in the fall semester 2023.

The course series introduces interdisciplinary research in drug discovery with
mathematics as the language and computation as the tool. We have a diverse and
lively class room that learn together and from each other: every year about two
third students of the class study mathematics or computer science, while other
students study physics, chemistry, (computational) biology, pharmacy, and other
fields such as epidemiology and medicine.

More information on the course can be found at [the course directory of the University
Basel](https://vorlesungsverzeichnis.unibas.ch/de/recherche?id=276986).

## Table of content

- [Time and place](#time-and-place)
- [Course material and licensing](#course-material-and-licensing)
- [Pre-course survey](#pre-course-survey)
- [Assessment](#assessment)
- [Syllabus](#syllabus)
  * [1. Drug discovery: an overview](#1-drug-discovery-an-overview) (22.09.2023)
  * [2. The central dogma and drug discovery](#2-the-central-dogma-and-drug-discovery) (29.09.2023)
  * [3. Biological sequence analysis](#3-biological-sequence-analysis) (06.10.2023)
  * [4. From sequences to structures](#4-from-sequences-to-structures) (13.10.2023)
  * [5. Proteins and ligands](#5-proteins-and-ligands) (20.10.2023)
  * [6. Structure- and ligand-based drug design](#6-structure--and-ligand-based-drug-design) (27.10.2023)
  * [7. From individial interactions to networks](#7-from-individual-interactions-to-networks) (03.11.2023)
  * [8. Biological networks](#8-biological-networks) (10.11.2023)
  * [9. Omics and cellular modelling](#9-omics-and-cellular-modelling) (17.11.2023)
  * [10.*Dies academicus*](#10-dies-academicus) (24.11.2023, no lecture)
  * [11. PK/PD modelling](#11-pkpd-modelling) (01.12.2023)
  * [12. Population modelling](#12-population-modelling) (15.12.2023)
  * [13. Guest-speaker session](#13-guest-speaker-session) (08.12.2023)
  * [14. Collaboration challenge](#14-collaboration-challenge) (22.12.2023)
- [Further questions or suggestions?](#further-questions-or-suggestions)
- [Archives of past courses](#archives-of-past-courses)

## Time and place

The lecture takes place on Fridays between 12:15 and 14:00 at Spiegelgasse 5,
Seminarraum 05.002.

## Course material and licensing

Course material, including lecture notes, slides, and reading material, are
shared on the course's web site, [AMIDD.ch](http://amidd.ch), unless otherwise
specified in the course.

All course material, unless otherwise stated, is shared under the Creative
Commons (CC-BY-SA 4.0) license.

## Pre-course survey

Prior to attending the first session, please [fill out the voluntary pre-course
survey](https://forms.gle/Xbk6ExbfNUxUgqm76). Your reply helps me to shape the
course to meet your needs.

## Assessment

The final note is given by participation including quizzes (30%), offline
activities (40%), and a collaboration challenge in the final session (30%).

## Syllabus

### 1. Drug discovery: an overview

* [Slides]({{site.assetbaseurl}}{% link assets/2022/01/AMIDD-2022-01-Intro.pdf %})
* Anonymous Post-lecture Survey of Lecture 1
* Material for offline activities (see slides 31-33)
    * Watch [a video](https://www.ibiology.org/human-disease/herceptin/) on the
      discovery and development of the drug *Herceptin*, presented by Susan
      Desmond-Hellmann, and answer questions. See the questions and submit your
      answers [here via a Google Form](https://forms.gle/1mAdkeebsB2QDx3m6).
    * Required reading: [Principles of early drug discovery]({{site.assetbaseurl}}{% link assets/2022/01/Principles-DD-Hughes.pdf %}) by Hughes *et al.*

### 2. The central dogma and drug discovery

* [Slides]({{site.assetbaseurl}}{% link assets/2022/02/AMIDD-2022-02-TheCentralDogma.pdf %})
* Material for offline activities (see slides 22-24)
    * Required reading: [Clinical efficacy of a RAF inhibitor needs broad target blockade in BRAF-mutant melanoma]({{site.assetbaseurl}}{% link assets/2022/02/Bollag-Nature-2010.pdf %}) by Bollag *et al.*, Nature 2010.
    * Optional reading: [A comprehensive map of molecular drug targets]({{site.assetbaseurl}}{% link assets/2022/02/Santos-NRDD-2017.pdf %}) by Santos *et al.*, Nature Reviews Drug Discovery, 2017
* Submit your answers for Offline Activities [here via Google Form](https://forms.gle/QhPwTK68BqzDMZ5ZA)

### 3. Biological sequence analysis

* [Slides]({{site.assetbaseurl}}{% link assets/2022/03/AMIDD-2022-03-BiologicalSequenceAnalysis.pdf %})
* [Anonymous Post-lecture Survey, #3](https://forms.gle/rj5hRuss8oE8kdSKA)
* Material for offline activities
  * Please go through the [slides #22 and #23]({{site.assetbaseurl}}{% link assets/2022/03/AMIDD-2022-03-BiologicalSequenceAnalysis.pdf %}) to try out calculating the Levenshtein distance with dynamic programming.
  * Required reading: [Discovery of a selective inhibitor of oncogenic B-Raf kinase with potent antimelanoma activity]({{site.assetbaseurl}}{% link assets/2021/03/Tsai-BRAF-PNAS-2008.pdf %}) by Tsai *et al.*, PNAS 2008.
  * Optional reading: Richard Bell, the inventor of Dynamic Programming, on the origin of the name. See slide [#29]({{site.assetbaseurl}}{% link assets/2022/03/AMIDD-2022-03-BiologicalSequenceAnalysis.pdf %}).
  * [Handout for lecture 3 and 4]({{site.assetbaseurl}}{% link assets/2022/03/AMIDD-2022-Lecture3-Handout.pdf %}), which contains genetic codes, information on amino acids, and offline exercises for both lecture 3 and 4. *Not all questions need to be answered now.* Please read the instructions in the Google Form below to finish this week's task.
  * Submit your answers for offline activities [here via the Google Form *AMIDD-2022-OfflineActivity-Lecture3*](https://forms.gle/K5Z4PGsJofa66zHp6).


### 4. From sequences to structures

* [Slides]({{site.assetbaseurl}}{% link assets/2022/04/AMIDD-2022-04-From-Sequences-to-Structures.pdf %})
* Material for offline activities
  * Required reading: [What does AlphaFold mean for drug discovery](https://www.nature.com/articles/d41573-021-00161-0), Asher Mullard, Nature Reviews Drug Discovery. See [the PDF version here]({{site.assetbaseurl}}{% link assets/2022/04/NRDD-2021-AlphaFold-DD.pdf %}).
  * Optional readings:
      * [AlphaFold2 is here: what’s behind the structure prediction miracle](https://www.blopig.com/blog/2021/07/alphafold-2-is-here-whats-behind-the-structure-prediction-miracle/), by Oxford Protein Informatics Group (OPIG). Recommended if you are interested in protein structure prediction and how AlphaFold2 achieved good performance.
  * A question about Markov chains: Given the Markov chain model represented on slide #15 [in the slides]({{site.assetbaseurl}}{% link assets/2022/04/AMIDD-2022-04-From-Sequences-to-Structures.pdf %}), what is the ratio between $p(ACGTGGT\|M)$ and $p(ACCTGGT\|M)$?
  * [Handout for lecture 3 and 4]({{site.assetbaseurl}}{% link assets/2022/03/AMIDD-2022-Lecture3-Handout.pdf %}), please finish the tasks titled *A subset of BLOSUM 50 values per aligned residue pair* and *What does Fomivirsen target?*.
  * Submit your answers for offline activities [here via the Google Form *AMIDD-2022-OA-Lecture4*](https://forms.gle/BbBVLNyzvQvsKqNd6).

### 5. Proteins and ligands

* [Slides]({{site.assetbaseurl}}{% link assets/2022/05/AMIDD-2022-05-protein-ligand-interaction.pdf %})
* Material for offline activities:
   * Watch the [YouTube video](https://www.youtube.com/watch?v=Q1ftYq13XKk) about the *Ramachandran Principal* by Prof. [Eric Martz](https://www.umass.edu/molvis/martz/), or read [the notes (including slides) on Proteopedia](https://proteopedia.org/wiki/index.php/Tutorial:Ramachandran_principle_and_phi_psi_angles), and finish a [Practice Quiz](https://proteopedia.org/w/User:Eric_Martz/Ramachandran_Principle_Quiz). 
   * Required reading: [*Evaluation of the Biological Activity of Compounds: Techniques and Mechanism of Action Studies*]({{site.assetbaseurl}}{% link assets/2022/05/BiologicalActivity-Dougall-Unitt.pdf%}) by Iain G. Dougall and John Unitt, chapter two of the book *The Practice of Medicinal Chemistry*. **To answer offline-activity questions**, it is required to read pages 15-22 (1-8 of the 29 pages in total, before section &lsquo;*4. Types of Enzyme Inhibition and Their Analysis*&rsquo;), page 27 (section 6A), and pages 34-37 (*Assay Biostatistics*). The rest is optional reading.
   * Submit your results here [via Google Form](https://forms.gle/LXpMecFWjQ36oETA9)
   * Optional reading: [Mathematics techniques in structural biology]({{site.assetbaseurl}}{% link assets/2022/04/JRQuine-MathBiophysicsBook.pdf %}) by John R. Quine.  Recommended booklet for students interested in applications of mathematics in determining structures of DNA and proteins without or with drugs.

### 6. Structure- and ligand-based drug design

* [Slides]({{site.assetbaseurl}}{% link assets/2022/06/AMIDD-2022-06-Structure-and-ligand-based-drug-discovery.pdf %})
* [Anonymous post-lecture survey for lecture 6](https://forms.gle/QcVXr4UP7NT7qy978)
* Material for offline activities:
    * Required reading: [*An introduction to machine learning*]({{site.assetbaseurl}}{% link assets/2022/06/Badillo-ML-2020.pdf %}) by Badillo *et al.*.
    * Required reading for this and next week: [*Computational methods in drug discovery*]({{site.assetbaseurl}}{% link assets/2022/06/Sliwoski-PharmacologicalReviews-2014-Computational-Methods-In-Drug-Discovery.pdf %}) by Gregory Sliwoski *et al.*. Please submit your replies to questions [via this Google Form](https://forms.gle/pfKX76K5XYuzxNSu8). The deadline of submitting the replies is *November 11th*.


### 7. From individual interactions to networks

* [Slides]({{site.assetbaseurl}}{% link
  assets/2022/07/AMIDD-2022-07-from-individual-interactions-to-networks.pdf %}).
  This week we discussed QSAR, machine learning models, and causal inference.
  And we introduced compartment models to model ligand-receptor interaction and
  enzyme kinetics. Next week we will continue with the compartment model and
  biological network analysis.
* This week's offline activity is to finish the readings of the last week.
     * Required reading: [*An introduction to machine learning*]({{site.assetbaseurl}}{% link assets/2022/06/Badillo-ML-2020.pdf %}) by Badillo *et al.*.
     * Required reading for this and next week: [*Computational methods in drug discovery*]({{site.assetbaseurl}}{% link assets/2022/06/Sliwoski-PharmacologicalReviews-2014-Computational-Methods-In-Drug-Discovery.pdf %}) by Gregory Sliwoski *et al.*. Please submit your replies to questions [via this Google Form](https://forms.gle/pfKX76K5XYuzxNSu8). The deadline of submitting the replies is *November 11th*.
* Optional reading:  [Causal inference in drug discovery and development](https://arxiv.org/abs/2209.14664), pre-print manuscript on *arxiv*.

### 8. Biological networks

* [Slides]({{site.assetbaseurl}}{% link assets/2022/08/AMIDD-2022-08-biological-networks.pdf %})
* Offline activities: three optional readings *for fun*:
	1. Bennett, Craig M., Michael B. Miller, and George L. Wolford. “Neural Correlates of Interspecies Perspective Taking in the Post-Mortem Atlantic Salmon: An Argument for Multiple Comparisons Correction.” Neuroimage 47, no. Suppl 1 (2009): S125.
	2. Lazebnik, Yuri. “Can a Biologist Fix a Radio?—Or, What I Learned While Studying Apoptosis.” Cancer Cell 2, no. 3 (September 1, 2002): 179–82. https://doi.org/10.1016/S1535-6108(02)00133-2
	3. Jonas, Eric, and Konrad Paul Kording. “Could a Neuroscientist Understand a Microprocessor?” PLOS Computational Biology 13, no. 1 (January 12, 2017): e1005268. https://doi.org/10.1371/journal.pcbi.1005268.


### 9. Omics and cellular modelling

* [Slides]({{site.assetbaseurl}}{% link assets/2022/09/AMIDD-2022-09-omics-and-cellular-modelling.pdf %})
* Offline activities are about image analysis. Biological image analysis is another important way to characterize MoA of compounds besides omics methods.
    * Required readings (1): [Biological Image Analysis Primer]({{site.assetbaseurl}}{% link assets/2022/09/Meijering-vanCappellen-2006-BioImage.pdf %}) by Erik Meijering and Gert van Cappellen (2006).
    * Required readings (2): Rudin, Markus, and Ralph Weissleder. 2003. “[Molecular Imaging in Drug Discovery and Development](https://doi.org/10.1038/nrd1007).” Nature Reviews Drug Discovery 2 (2): 123–31. ([PDF version]({{site.assetbaseurl}}{% link assets/2022/09/Rudin-Weissleder-2003-Molecular-imaging.pdf %}))
    * Submit your offline activities with regard to the required reading [here via the Google Form](https://forms.gle/2oy6NX2acdSpQasZA). Deadline: Friday, December 2nd, 2022.


### 10. *Dies academicus*

No lectures. We invite registered students to visit Roche. Details are announced via email.

### 11. PK/PD modelling

* [Slides]({{site.assetbaseurl}}{% link assets/2022/10/AMIDD-2022-10-PK-PD-modelling.pdf %})
* Offline activities
    * Required reading: the backup slides of lecture 10 to learn about the principles of population modelling, especially non-linear mixed-effect models (NLMEs), and about clinical trials.
    * Optional reading:
        * Davies, Michael, et al.. 2020. “[Improving the Accuracy of Predicted Human Pharmacokinetics: Lessons Learned from the AstraZeneca Drug Pipeline Over Two Decades](https://doi.org/10.1016/j.tips.2020.03.004).” Trends in Pharmacological Sciences 41 (6): 390–408. *A good introduction to prediction of PK profiles in industry*.
        * Jones, H. M., and K. Rowland‐Yeo. 2013. “[Basic Concepts in Physiologically Based Pharmacokinetic Modeling in Drug Discovery and Development](https://doi.org/10.1038/psp.2013.41).” CPT: Pharmacometrics & Systems Pharmacology 2 (8): 63. *A good introduction to PBPK modelling*.

### 12. Population modelling

Details to be announced

### 12. Guest-speaker session

Details to be announced

### 13. Collaboration challenge

Details to be announced


## Further questions or suggestions?

Please contact the lecturer, Jitao David Zhang, at [jitao-david.zhang@unibas.ch](mailto:jitao-david.zhang@unibas.ch).


## Archives of past courses

* [AMIDD 2022]({{site.baseurl}}{% link archive/README-2022.md %})
* [AMIDD 2021]({{site.baseurl}}{% link archive/README-2021.md %})
* [AMIDD 2020]({{site.baseurl}}{% link archive/README-2020.md %})
* [AMIDD 2019]({{site.baseurl}}{% link archive/README-2019.md %})
