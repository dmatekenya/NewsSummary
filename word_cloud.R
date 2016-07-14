# Load required packages
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")
#--------------------------------------------------
#Load data: I dumped all articles in one text file to make things simple
filePath <- "/Users/dmatekenya/PycharmProjects/WebMining/NewsClassifier/data_nyasa_times/2016-07-13/all.txt"
text <- readLines(filePath)
# Load the data as a corpus
docs <- Corpus(VectorSource(text))
#--------------------------------------------

#Text Data Preprocessing
toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
#Replace special characters with space
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")
# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))
# Remove numbers
docs <- tm_map(docs, removeNumbers)
# Remove punctuations
docs <- tm_map(docs, removePunctuation)
# Remove common English stopwords
docs <- tm_map(docs, removeWords, stopwords("english"))
# I also removed extra stopwords after noticing that they werent adding any value
docs <- tm_map(docs, removeWords, 
               c("can","also", "said","will","malawi","one","says","among","around","must","two","percent","since","without")) 
# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)
#--------------------------------------------

#Covert text to word document matrux
dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
#--------------------------------------------

#finally, the best part, create word cloid
set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 15,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

#create a simple barchart to see most occuring words
barplot(d[1:10,]$freq, las = 2, names.arg = d[1:10,]$word,
        col ="lightblue", main ="Most Frequent Words (Top 10)",
        ylab = "Word Frequencies")
#--------------------------------------------