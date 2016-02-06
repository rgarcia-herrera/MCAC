#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(argparse))

parser <- ArgumentParser(description="plot gmaf vs groupaf variant's ")
parser$add_argument("--csv", required=TRUE, help="archivo con columnas 2= variable, 3=gmaf, 4=groupaf ")
parser$add_argument("--labeled", default="no", help="se le pone etiqueta al punto?")
parser$add_argument("--loglog", default="no", help="transfromacion log log?")
args <- parser$parse_args()



freqs<-read.table(file=args$csv, header = TRUE)
rownames(freqs) <- as.character(freqs[,2])

x <- freqs[,3]
y <- freqs[,4]
if (args$loglog=="yes"){loglog<-"xy"} else if (args$loglog=="no"){loglog<-""} else {stop("loglog must be yes or no")}

plotfile = file.path(dirname(args$csv), paste(sub("^([^.]*).*", "\\1", args$csv),".pdf",sep=""))

if (args$labeled=="no"){
	pdf(file=plotfile,width=7,height=8)
	plot(x,y, xlab="gmaf", ylab="groupaf", main="gmaf vs groupaf", col=rgb(0,100,0,50,maxColorValue=255), log= loglog)
	dev.off()
} else if (args$labeled=="yes"){
	pdf(file=plotfile,width=7,height=8)
	plot(x,y, xlab="gmaf", ylab="groupaf", main="gmaf vs groupaf", col=rgb(0,100,0,50,maxColorValue=255), log= loglog)
	text(x, y, rownames(freqs), cex=0.6, pos=4, col="blue")
	dev.off()
} else {
	stop("labeled must be yes or no")
}