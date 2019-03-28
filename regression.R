#install.packages("rstudioapi")
library(rstudioapi)
current_path = getActiveDocumentContext()$path
setwd(dirname(current_path))

data_set = read.csv("Temperatures.csv")

print(data_set[,1])

x = data_set[,1]
y = data_set[,2]

relation = lm(y~x)

print(relation)

#print(summary(relation))