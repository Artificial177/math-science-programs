library(gmp)
library(rstudioapi)

largenums <- readLines("RMathText/problem13.txt") # The Directory Containing The Numbers

firstten <- function(){
  digits <- sum(as.bigz(largenums))
  return(substr(as.character(digits), 1, 10))
}

firstten()
