library(HMM)
set.seed(1887)
hmmModel <- initHMM(States=c("A", "D"), # A=Angel, D=Devil
                    Symbols=c("B", "R"), # B=Blessing, R=Rant
                    startProbs=c(0.5, 0.5),
                    transProbs = matrix(c(0.8, 0.2, 0.2, 0.8), nrow=2),
                    emissionProbs = matrix(c(0.9, 0.1, 0.1, 0.9), nrow=2))
simHmm <- simHMM(hmmModel, 100)
simStates <- paste(simHmm$states, collapse="")
simSymbols <- paste(simHmm$observation, collapse="")
starts <- seq(1, 81, by=20)
ends <- seq(20, 100, by=20)
statesSplit <- sapply(seq(along=starts), 
                      function(i) substr(simStates, starts[i], ends[i]))
symbolsSplit <- sapply(seq(along=starts), 
                      function(i) substr(simSymbols, starts[i], ends[i]))
res <- unlist(lapply(seq(along=starts),
              function(i) c(statesSplit[i], symbolsSplit[i])))
writeLines(res, "simHmm.txt")
