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
Basel](https://vorlesungsverzeichnis.unibas.ch/de/recherche?id=269095).

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
  * [12. Guest-speaker session](#11-guest-speaker-session) (08.12.2023)
- [Student presentation topics and reference papers](#student-presentation-topics-and-reference-papers)
  * [13. Student presentation (I)](#13-student-presentation-i) (15.12.2023)
  * [14. Student presentation (II)](#14-student-presentation-ii) (22.12.2023)
- [End-term project](#end-term-project)
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

The final note is given by participation including quizzes (30%), offline activities (40%), and
a collaboration challenge in the final session (30%).

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

### 12. Guest-speaker session

To be announced

# Student presentation topics and reference papers

Each team is expected to deliver a talk of 30 minutes, which is followed by 10 minutes of Q&A.

You can vote for your presentation topics via [the Google Form of voting for presentation topics](https://forms.gle/VvQx7xfAK5FgRyQZ6) by November 14th.

In HS 2022, our class will present on the following four topics:

1. **Phenotypic drug discovery**: how phenotypic drug discovery complements target-based drug discovery.
2. **Productivity in drug discovery**: return of investment, cost, and research productivity in drug discovery.
3. **Mathematical modeling in drug discovery**: mathematical modeling techniques used in preclinical and clinical studies.
4. **Reverse translation**: how we can leverage data from clinical trials and observational studies to empower preclinical studies.

## 13. Student presentation (I)

### Team 1: Phenotypic drug discovery (December 16th)

1. Vincent, Fabien, Arsenio Nueda, Jonathan Lee, Monica Schenone, Marco Prunotto, and Mark Mercola. “Phenotypic Drug Discovery: Recent Successes, Lessons Learned and New Directions.” Nature Reviews Drug Discovery, May 30, 2022, 1–16. [https://doi.org/10.1038/s41573-022-00472-w](https://doi.org/10.1038/s41573-022-00472-w).
2. Moffat, John G., Fabien Vincent, Jonathan A. Lee, Jörg Eder, and Marco Prunotto. 2017. “Opportunities and Challenges in Phenotypic Drug Discovery: An Industry Perspective.” Nature Reviews Drug Discovery 16 (8): 531–43.  https://doi.org/10.1038/nrd.2017.111. ([PDF]({{site.assetbaseurl}}{% link assets/2020/13-14/Moffat-Phenotypic.pdf %}))
3. Vincent, Fabien, Paula M. Loria, Andrea D. Weston, Claire M. Steppan, Regis Doyonnas, Yue-Ming Wang, Kristin L. Rockwell, and Marie-Claire Peakman. “Hit Triage and Validation in Phenotypic Screening: Considerations and Strategies.” Cell Chemical Biology 27, no. 11 (November 19, 2020): 1332–46. [https://doi.org/10.1016/j.chembiol.2020.08.009](https://doi.org/10.1016/j.chembiol.2020.08.009).

### Team 2: Productivity in drug discovery and development (December 16th)

1. Smietana, Katarzyna, Leeland Ekstrom, Barbara Jeffery, and Martin Møller. “Improving R&D Productivity.” Nature Reviews Drug Discovery 14, no. 7 (July 2015): 455–56. [https://doi.org/10.1038/nrd4650](https://doi.org/10.1038/nrd4650).
2. Ringel, Michael S., Jack W. Scannell, Mathias Baedeker, and Ulrik Schulze. “Breaking Eroom’s Law.” Nature Reviews Drug Discovery 19, no. 12 (April 16, 2020): 833–34. [https://doi.org/10.1038/d41573-020-00059-3](https://doi.org/10.1038/d41573-020-00059-3).
3. Fernando, Kathy, Sandeep Menon, Kathrin Jansen, Prakash Naik, Gianluca Nucci, John Roberts, Shuang Sarah Wu, and Mikael Dolsten. “Achieving End-to-End Success in the Clinic: Pfizer’s Learnings on R&D Productivity.” Drug Discovery Today, December 2021, S1359644621005444. [https://doi.org/10.1016/j.drudis.2021.12.010](https://doi.org/10.1016/j.drudis.2021.12.010).
4. Scannell, Jack W., James Bosley, John A. Hickman, Gerard R. Dawson, Hubert Truebel, Guilherme S. Ferreira, Duncan Richards, and J. Mark Treherne. “Predictive Validity in Drug Discovery: What It Is, Why It Matters and How to Improve It.” Nature Reviews Drug Discovery, October 4, 2022, 1–17. [https://doi.org/10.1038/s41573-022-00552-x](https://doi.org/10.1038/s41573-022-00552-x).

## 14. Student presentation (II)

### Team 3: Mathematical modelling in drug discovery (December 23rd)

1. Handel, Andreas, Nicole L. La Gruta, and Paul G. Thomas. “Simulation Modelling for Immunologists.” Nature Reviews Immunology 20, no. 3 (March 2020): 186–95. [https://doi.org/10.1038/s41577-019-0235-3](https://doi.org/10.1038/s41577-019-0235-3).
2. Gieschke, R., and J. L. Steimer. “Pharmacometrics: Modelling and Simulation Tools to Improve Decision Making in Clinical Drug Development.” European Journal of Drug Metabolism and Pharmacokinetics 25, no. 1 (March 2000): 49–58. [https://doi.org/10.1007/BF03190058](https://doi.org/10.1007/BF03190058).
3. Elmokadem, Ahmed, Matthew M. Riggs, and Kyle T. Baron. “Quantitative Systems Pharmacology and Physiologically-Based Pharmacokinetic Modeling With Mrgsolve: A Hands-On Tutorial.” CPT: Pharmacometrics & Systems Pharmacology 8, no. 12 (2019): 883–93. [https://doi.org/10.1002/psp4.12467](https://doi.org/10.1002/psp4.12467).

### Team 4: Reverse translation (December 23rd)

1. Kasichayanula, Sreeneeranj, and Karthik Venkatakrishnan. “Reverse Translation: The Art of Cyclical Learning.” Clinical Pharmacology & Therapeutics 103, no. 2 (February 1, 2018): 152–59. [https://doi.org/10.1002/cpt.952](https://doi.org/10.1002/cpt.952).
2. Maciejewski, Mateusz, Eugen Lounkine, Steven Whitebread, Pierre Farmer, William DuMouchel, Brian K Shoichet, and Laszlo Urban. “Reverse Translation of Adverse Event Reports Paves the Way for De-Risking Preclinical off-Targets.” Edited by Fiona M Watt. ELife 6 (August 8, 2017): e25818. [https://doi.org/10.7554/eLife.25818](https://doi.org/10.7554/eLife.25818).
3. Michoel, Tom and Zhang, Jitao David. "Causal inference in drug discovery and development". [https://arxiv.org/abs/2209.14664](https://arxiv.org/abs/2209.14664).


## Further questions or suggestions?

Please contact the lecturer, Jitao David Zhang, at [jitao-david.zhang@unibas.ch](mailto:jitao-david.zhang@unibas.ch).


## Archives of past courses

* [AMIDD 2022]({{site.baseurl}}{% link archive/README-2022.md %})
* [AMIDD 2021]({{site.baseurl}}{% link archive/README-2021.md %})
* [AMIDD 2020]({{site.baseurl}}{% link archive/README-2020.md %})
* [AMIDD 2019]({{site.baseurl}}{% link archive/README-2019.md %})
