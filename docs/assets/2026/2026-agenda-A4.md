---
title: "Applied Mathematics and Informatics in Drug Discovery (AMIDD)"
subtitle: "Course outline — Fall semester 2026, University of Basel"
author: "Jitao David Zhang · jitao-david.zhang@unibas.ch · www.AMIDD.ch"
documentclass: extarticle
geometry: "a4paper,margin=13mm"
fontsize: 9pt
papersize: a4
colorlinks: true
header-includes:
  - \usepackage{titlesec}
  - \titlespacing*{\section}{0pt}{5pt}{0pt}
  - \titleformat{\section}{\large\bfseries}{}{0pt}{}
  - \setlength{\parskip}{2.5pt}
  - \usepackage{titling}
  - \setlength{\droptitle}{-4.5em}
  - \setlength{\thanksmarkwidth}{0pt}
  - \renewcommand{\arraystretch}{0.9}
  - \usepackage{wrapfig}
---

**Fridays 12:15–14:00 · Spiegelgasse 5, Seminarraum 05.002 · in-person only · twelve lectures, 18.09.–18.12.2026.** On 20.11. only, we meet at Hörsaal 101, *Alte Universität*, Rheinsprung 9. The course is open to bachelor, master, and PhD students of mathematics, computer science, physics, chemistry, (computational) biology, pharmacy, epidemiology, and medicine. There are no prerequisites beyond curiosity: whatever your background, you bring expertise that the rest of us lack. If you have questions, you can reach Jitao David Zhang, the lecturer, at [jitao-david.zhang@unibas.ch](mailto:jitao-david.zhang@unibas.ch).

## What we will learn together

Drug discovery is an interdisciplinary craft. In this course, we will get an impression of how researchers in drug discovery and development use mathematics as a language and computation as a tool to understand biology and drug-body interactions.

We start the journey with real-world examples of clinically approved drugs such as semaglutide (brand names *Ozempic* and *Rybelsus* for diabetes, and *Wegovy* for weight management). We back-trace the discovery and development of the medicine through the linear model of the drug-discovery pipeline, and explore the interaction between semaglutide and the human body by adopting a multiscale view:

**molecule → target → cell → organ and system → whole body → population**

Two threads then run through every lecture: that multiscale climb, because each scale calls for models of its own, and five key questions that every project answers, whatever the scale (lecture 3). What is the **medical need**? What is the **target and the modality**? What is the **PK/PD** relationship? What is the **benefit and the risk**? Which **patients** benefit most?

From there, we explore the major players and stakeholders of the drug discovery process, and then climb the scales: the biology that makes a protein a drug target; two ways of learning from data, statistical and machine learning models on the one hand and causal models on the other; and their application to molecules, in lead identification and optimization, to cells and networks, to understand the mechanism and mode of action of drugs, and finally to the whole body and the population, with PK/PD modeling as an example of ODE-based models. The course ends with a guest lecture and a collaboration challenge, where teams work towards a common goal within limited time and resources.

## Agenda

| #  | Date   | Session                                                           | Focus                                      |
|----|--------|-------------------------------------------------------------------|--------------------------------------------|
| 1  | 18.09. | Introduction to drug discovery                                    | The whole arc, seen through one drug       |
| 2  | 25.09. | The *What*, the *Who*, and the *How* of drug discovery            | Workflow, stakeholders, paths to a drug    |
| 3  | 02.10. | Key questions in drug discovery                                   | The five questions as a project compass    |
| 4  | 09.10. | Biological foundation of drug discovery                           | From genes to phenotypes                   |
| 5  | 16.10. | Protein as drug target                                            | Molecular, physics-based models            |
| 6  | 23.10. | Statistical, machine learning, and artificial intelligence models | Learning from data: prediction and beyond  |
| 7  | 30.10. | Causal inference                                                  | Causal models, generative simulation       |
| —  | 06.11. | No lecture — hands-on project with tabular models                 | Models you run yourself                    |
| 8  | 13.11. | Lead identification and optimization                              | Molecule-level design and profiling        |
| 9  | 20.11. | Mechanism and mode of action of drugs *(Alte Universität)*        | Omics, networks, cell-level models         |
| —  | 27.11. | *Dies academicus* — no lecture                                    |                                            |
| 10 | 04.12. | PK/PD modeling and basics of clinical trials                      | Organ, whole-body, and population models   |
| 11 | 11.12. | Guest lectures                                                    | Practitioners' perspectives                |
| 12 | 18.12. | A collaboration challenge                                         | Everything above, applied in teams         |

## Topics we will cover

**Drug discovery and biomedicine.** Modalities (small molecules, peptides, antibodies, oligonucleotides, and emerging ones); medical need and indication selection; target identification, assessment, and validation; the biological basis of disease; proteins as drug targets and structure–function relationships; ADME (absorption, distribution, metabolism, and excretion), potency, selectivity, and safety profiling; pharmacokinetics and pharmacodynamics; clinical trial design, endpoints, and adverse events; regulatory milestones and stakeholders.

**Mathematics and informatics.** Mechanistic and physics-based modeling; binding kinetics and dose–response; statistical inference; machine learning, transformer-based AI models and their evaluation; structure prediction and ligand-based design; causal inference; sequence analysis and language models; omics data analysis and network biology; multiscale, PK/PD and physiologically based (PBPK) models; population models; reproducibility and the responsible use of LLMs and AI agents in research.

## How we work, and how you are assessed

An ideal classroom is diverse, interactive, and curious. Each lecture is followed by one or more offline activities, such as reading a paper, watching a video, or trying out an analysis, as well as (from time to time) a short, anonymous feedback survey. Your grade is given by participation including quizzes (30%), offline activities (40%), and the collaboration challenge in the final session (30%).

![](amidd-qr.png){width=1.45cm} Scan for the syllabus, slides, papers, and submission links: [AMIDD.ch](http://www.amidd.ch) · CC-BY-SA 4.0.
