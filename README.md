# gillespie
#### Implementaion of the Lytic-Lysogenic switch in phage Lambda

##### Biology

Upon infecting a bacterial host cell, the phage Lambda enters into one of two dramatically different lifestyle pathways: virulent or temperate. 

During a virulent lifestyle a phage infects a bacteria; its genome is replicated many times; and the newly created copies are released into the surrounding environment through lysis, extrusion or budding. 

In contrast during a temperate lifestyle, a phage infects a bacteria and either integrates its DNA into the bacterial genome or re-circularizes its DNA into a stable plasmid. The temperate phage will live in this semi-stable lifestyle as a prophage as the host bacteria continues to grow and divide. The prophage will be carried through future bacterial cell divisions until appropriate environmental conditions cause the temperate phage to enter into a virulent lifestyle and release itself from the host bacterium.  

There are many factors that govern which pathway the phage ultimately goes down, most based around various gene regulatory networks.  One of the better known, and easier to model, is the multiplicity of infection, which is simply the ratio of phage genomes to target cells.  When this number is high, there are multiple phage infections per bacterial cell.  

The presence of multiple phage genome copies in the cell cause feedback into these biochemical pathways and act as a a sort of switch, to govern which of the two lifestyle the phage should enter.

##### Computer Modeling
Using the previous work by Arkin, Ross, and McAdams (1998), the phage Lambda lysis-lysogeny decision circuit (shown in the figure below) was reconstructed.  
![alt text](http://www.genetics.org/content/genetics/149/4/1633/F1.large.jpg)

This involves the implementation of the kinetic model that will use the chemical kinetics, stochastic modeling of gene regulation, and thermodynamic models of promoter regulation to calculate the probabilities of transcription and translation.
