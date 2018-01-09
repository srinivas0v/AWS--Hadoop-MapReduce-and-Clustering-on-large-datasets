# AWS--Hadoop-MapReduce-and-Clustering-on-large-datasets

A web application to perform Mapreduce, kmeans clustering on large datasets. Visualizing the clustered output to get meaningful results. Built using Hadoop, AWS bucket, Python Flask, plot.ly and D3.JS packages for visualization.

code.py
    + On AWS please take the CSV file and place it on AWS, either in EC2 or S3 (or similar).
    + Using a clustering method, find: 
       5 clusters based on columns District and Sector
    + Show, in textual form, time to run, centroids for the clusters, and number of points in each cluster.
    + Create a web form (on AWS) that allows a user to input two column names (for example "B" and "C" -or- "District" and "Sector")
      and the number of clusters to find.
    + On a web page, with your name, class, and ID number at the top,
      Show the results, in textual form: centroids, and list all of the points in each cluster.  
      
    + In your browser show a bar chart (graph), where the bars are vertically placed, such that each bar represents a cluster,
      where the bars are sorted, from minimum to maximum by number of points in that cluster,       
      where the label of each bar is the number of points in that cluster, where different colors shows number of points in
      that cluster, 
      and the height of that bar is proportional to the number of points in that cluster.
    + Show a scatter plot (graph) of ONLY the centroid points, identifying cluster-centroids by color.
