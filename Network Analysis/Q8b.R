#Install the library iGraph
install.packages("igraph")
install.packages("centiserve")
library("igraph")
library("Matrix")
library("centiserve")
links <- read.table("C:\\Users\\arunav\\Desktop\\moreno_train\\out.moreno_train_train",sep = " ",header = T)
head(links)

#Create an igraph object from data frame
zachary <- graph_from_data_frame(d=links,directed = T)



#Check number of vertices
length(V(zachary))

 hubbell(zachary)
#Plot the graph with vertex size proportional to eccentricity
plot(zachary,layout=layout.star(zachary),edge.arrow.size=0.3,vertex.size=(0.1*hubbell(zachary)),edge.color="lightblue",vertex.color="orange",vertex.size=15, 
     
     vertex.frame.color="black", vertex.label.color="black", 
     
     vertex.label.cex=0.7, vertex.label.dist=0)

