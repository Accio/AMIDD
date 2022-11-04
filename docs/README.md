Welcome to the website for *Applied Mathematics and Informatics In Drug
Discovery* (AMIDD), the course series running at the Department of Mathematics
and Informatics, University of Basel in the fall semester 2022.

The course series introduces interdisciplinary research in drug discovery with
mathematics as the language and informatics as the tool. We have a diverse and
lively class room that learn together and from each other: every year about two
third students of the class study mathematics or computer science, while other
students study physics, chemistry, (computational) biology, pharmacy, and other
fields such as epidemiology and medicine.

More information on the course can be found at [the course directory of the University
Basel](https://vorlesungsverzeichnis.unibas.ch/de/recherche?id=269095).

## Table of content

- [Time and place](#time-and-place)
- [Course material and licensing](#course-material-and-licensing)
- [Pre-course survey](#pre-course-survey)
- [Syllabus](#syllabus)
  * [1. Drug discovery: an overview](#1-drug-discovery-an-overview) (23.09.2022)
  * [2. The central dogma and drug discovery](#2-the-central-dogma-and-drug-discovery) (30.09.2022)
  * [3. Biological sequence analysis](#3-biological-sequence-analysis) (07.10.2022)
  * [4. From sequences to structures](#4-from-sequences-to-structures) (14.10.2022)
  * [5. Proteins and ligands](#5-proteins-and-ligands) (21.10.2022)
  * [6. Structure- and ligand-based drug design](#6-structure--and-ligand-based-drug-design) (28.10.2022)
  * [7. From individial interactions to networks](#7-from-individual-interactions-to-networks) (04.11.2022)
  * [8. Omics and cellular modelling](#8-omics-and-cellular-modelling) (11.11.2022)
  * [9. PKPD modelling](#9-pkpd-modelling) (18.11.2022, exceptionally at Kollegienhaus, Hörsaal 120)
  * [10.*Dies academicus - optional Ask Me Anything session*](#10-dies-academicus---optional-ask-me-anything-session) (25.11.2022)
  * [11. Population modelling](#11-population-modelling) (02.12.2021)
  * [12. Guest-speaker session](#11-guest-speaker-session) (09.12.2021)
- [Student presentation topics and reference papers](#student-presentation-topics-and-reference-papers)
  * [12. Student presentation (I)](#12-student-presentation-i) (16.12.2021)
  * [13. Student presentation (II)](#13-student-presentation-ii) (23.12.2021)
- [End-term project](#end-term-project)
- [Assessment](#assessment)
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
survey](https://forms.gle/bkWpDSiwvRQHZeQs7). Your reply helps me to shape the
course to meet your needs.

## Syllabus

### 1. Drug discovery: an overview

* [Slides]({{site.assetbaseurl}}{% link assets/2022/01/AMIDD-2022-01-Intro.pdf %})
* [Anonymous Post-lecture Survey of Lecture 1](https://forms.gle/XBZu3iHJyL1D618Y7)
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

### 8. Omics and cellular modelling

* [Slides]({{site.assetbaseurl}}{% link assets/2021/08/AMIDD-2021-08-omics.pdf %})
* Offline activities
    * Required readings (1): [Biological Image Analysis Primer]({{site.assetbaseurl}}{% link assets/2021/08/Meijering-vanCappellen-2006-BioImage.pdf %}) by Erik Meijering and Gert van Cappellen (2006).
    * Required readings (2): Rudin, Markus, and Ralph Weissleder. 2003. “[Molecular Imaging in Drug Discovery and Development](https://doi.org/10.1038/nrd1007).” Nature Reviews Drug Discovery 2 (2): 123–31. ([PDF version]({{site.assetbaseurl}}{% link assets/2021/08/Rudin-Weissleder-2003-Molecular-imaging.pdf %}))
    * Submit your offline activities with regard to the required reading [here via the Google Form](https://forms.gle/BP8r46B2iWaeMaXL7). Deadline: Friday, November 26th, 2021.
    * Optional reading: [Spatial omics and multiplexed imaging to explore cancer biology](https://www.nature.com/articles/s41592-021-01203-6), a review by Lewis *et al.*

### 9. PKPD modelling

* [Slides]({{site.assetbaseurl}}{% link assets/2021/09/AMIDD-2021-09-PK-PD-modelling.pdf %})
* Offline activities:
    * Required reading: backup slides on non-linear mixed-effect (NLME) models and clinical trials.
    * Optional reading:
        * Davies, Michael, et al.. 2020. “[Improving the Accuracy of Predicted Human Pharmacokinetics: Lessons Learned from the AstraZeneca Drug Pipeline Over Two Decades](https://doi.org/10.1016/j.tips.2020.03.004).” Trends in Pharmacological Sciences 41 (6): 390–408. *A good introduction to prediction of PK profiles in industry*.
        * Jones, H. M., and K. Rowland‐Yeo. 2013. “[Basic Concepts in Physiologically Based Pharmacokinetic Modeling in Drug Discovery and Development](https://doi.org/10.1038/psp.2013.41).” CPT: Pharmacometrics & Systems Pharmacology 2 (8): 63. *A good introduction to PBPK modelling*.


### 10. *Dies academicus - optional Ask Me Anything session*

You can ask me anything in this session.

Besides scientific topics in drug discovery, my experience is that many students
are interested in career topics: should I do a PhD or not? Should I consider
working in industry? You may this article below interesting if you consider
doing a PhD and perhaps doing a postdoc in pharma: Zhang, Jitao David. “[Ten
Simple Rules for Doing a Postdoc in
Pharma.](https://doi.org/10.1371/journal.pcbi.1008989)” PLOS Computational
Biology 17, no. 6 (June 3, 2021): e1008989.

### 11. Population modelling

### 12. Guest-speaker session

To be announced

# Student presentation topics and reference papers

## 13-14. Student presentations

Each team is expected to deliver a talk of 30 minutes, which is followed by 10 minutes of Q&A.

You can vote for your presentation topics via [Google Form](https://forms.gle/VvQx7xfAK5FgRyQZ6) by November 14th.

In HS 2022, our class will present on the following four topics:

1. Phenotypic drug discovery: how phenotypic drug discovery complements target-based drug discovery.
2. Productivity in drug discovery: return of investment, cost, and research productivity in drug discovery.
3. Mathematical modeling in drug discovery: mathematical modeling techniques used in preclinical and clinical studies.
4. Reverse translation: how we can leverage data from clinical trials and observational studies to empower preclinical studies.

Teams are also welcome to bring up their own ideas. If there are enough participants, we may adopt these initiatives.


## End-term project

All participants are expected to finish the end-term project either individually
or in a team of two people. She or he or the team shall choose *one* concept from a list of candidate topics, upon which they will write a short essay introducing the
concept to non-experts, with examples and ideally applications in drug
discovery. The topics will be announced during the semester.

The essay should have an abstract (less than 200 words), a list of references,
and a main text that does not exceed 3,000 words. Visual elements like table and
figures that help readers understand the concept are welcome but not obligatory.
In case of a team work, the contribution of the two people should be specified.

Essays in literature-programming styles, combining texts and source code with
Jupyter notebook or Rmarkdown, are encouraged. For such essays the source code does
not count to the total words.

List of candidate topics of year 2022:

* Simple to intermediate
    * Principal component analysis (PCA)
    * The Lotka-Volterra predator-prey model
    * Response surface method designs
* Intermediate to demanding
    * Exploratory factor analysis
    * Regression trees and random forests
    * Mann-Whitney-Wilcoxon tests
    * Regularization (e.g. Ridge, LASSO, and elastic net)
* Advanced
    * Instrumental variable and Mendelian randomization
    * Graph neural network
    * Shapley values

The choice of topic and the team composition is to be submitted via [this Google
Form of voting for the project topic](https://forms.gle/m8vmz2XTeDkNZQFZ6) by
*Thursday, December the 1st*. Two people working together need to vote just
once. The deadline for submitting the essay by email is *January 13th, 2022*. No
extension is possible.

Submitted essays will be shared with the whole class for open review and joint
learning.

## Assessment

The final note is given by participation (40%), presentation (30%), and project
work (30%).

## Further questions or suggestions?

Please contact the lecturer, Jitao David Zhang, at [jitao-david.zhang@unibas.ch](mailto:jitao-david.zhang@unibas.ch).


## Archives of past courses

* [AMIDD 2021]({{site.baseurl}}{% link archive/README-2021.md %})
* [AMIDD 2020]({{site.baseurl}}{% link archive/README-2020.md %})
* [AMIDD 2019]({{site.baseurl}}{% link archive/README-2019.md %})
