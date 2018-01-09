import pandas
from flask import Flask, request, render_template, redirect
import numpy as np
import pandas as pd
import matplotlib
from pandas.compat import numpy

matplotlib.use('AGG')
import matplotlib.pyplot as plt
import time
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
app = Flask(__name__)

path = 'C:/Users/srinivas venkatesh/Desktop/'
spath = 'C:/Users/srinivas venkatesh/Documents/cloud computing/assg6/static/'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
      if request.form['submit'] == 'cluster':
          cno = request.form['no']
          c1 = request.form['col1']
          c2 = request.form['col2']
          a =cno+'$$'+c1+'$$'+c2
          print cno
          return redirect('/cluster/' + a)
    return render_template('index.html')



@app.route('/cluster/<a>', methods=['POST', 'GET'])
def k_means(a):
    colnames = ['House','District','Sector','City','State','Lat','Long']
    data = pandas.read_csv(path + 'data1.csv',names= colnames,  header=1)
    cno,col1,col2 = a.split('$$')
    print col1,col2
    x = data[col1].values.tolist()
    y = data[col2].values.tolist()
    n = int(cno)
    print 'here'
    N = len(y)
    x = range(N)
    width = 1 / 1.5
    plt.bar(x, y, width, color="blue")
    plt.savefig(spath + 'f.png')

    #plt.scatter(x, y)
    #plt.savefig(spath+'f.png')
    #plt.show()

    X = np.column_stack((x, y))
    print X.shape
    starttime = time.time()
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    print(centroids)
    print(labels)
    label = kmeans.predict(X)
    print 'lable'
    print label

    {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}

    x = {i: X[np.where(kmeans.labels_ == i)] for i in range(kmeans.n_clusters)}
    print 'here'
    print x



    unique, counts = np.unique(labels, return_counts=True)
    a = dict(zip(unique, counts))
    print a

    colors = ["g.", "r.", "c.", "y.","b."]

    for i in range(len(X)):
        #print("coordinate:", X[i], "label:", labels[i])
        #plt.plot(X[i][0], X[i][1], colors[labels[i] % len(colors)], markersize=10)
        plt.bar(X[i][0], X[i][1], width, colors[labels[i]])

    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    endtime = str(time.time() - starttime)
    plt.savefig(spath+'s.png')
    return render_template('clusters.html', cent=centroids,time = endtime,count = x,  img = 'f.png', img1 = 's.png')


if __name__ == '__main__':
    app.run(debug='true', port=5000)
