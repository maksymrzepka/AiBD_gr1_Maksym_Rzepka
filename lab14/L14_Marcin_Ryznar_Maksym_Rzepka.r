library(magrittr)
install.packages("ggplot2")
install.packages("GGally")
library("ggplot2")
library("GGally")
library("cluster")

#Zadanie 1

list_1_10 <- 1:10
print(list_1_10)
list_1_10 %<>% log2() %>% sin() %>% sum()  %>% sqrt()
print(list_1_10)

data(iris)
print(head(iris))
mean_aggre <- iris %>% aggregate (. ~ Species, ., mean)
print(mean_aggre)


#Zadanie 2
chart1 <- ggplot(iris, aes(x=Sepal.Length)) + geom_histogram(aes(fill=Species, color=Species),bins=20) + 
            geom_vline(data=mean_aggre, aes(xintercept=Sepal.Length, color = Species), linetype = "dashed") + labs(x='x_axis',y='y_axis')

ggsave("/home/chart1.jpg", plot = chart1)

chart2 <- ggpairs(data = iris, aes(color=Species))
ggsave("/home/chart2.jpg", plot = chart2)

#Zadanie 3
x<- iris[,1:4]
y<- iris[,5]

sum_sqr <- c()

for (i in 1:10){
    kmeans_r <- kmeans(x, i)
    sum_sqr <- append(sum_sqr, kmeans_r$tot.withinss)
}
chart3 <- ggplot(data.frame(iteration = 1:length(sum_sqr), value = sum_sqr), aes(x = iteration, y=sum_sqr))+geom_line()
ggsave("/home/chart3.jpg", plot = chart3)

kmeans_r <- kmeans(x,3)

chart4 <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = kmeans_r$cluster)) + geom_point()
ggsave("/home/chart4.jpg", plot = chart4)


chart5 <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = Species)) + geom_point()
ggsave("/home/chart5.jpg", plot = chart5)


