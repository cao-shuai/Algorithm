from Algorithm.MyAlgorithms import BFS
from Algorithm.MyAlgorithms import Dijkstraalgorithm
from Algorithm.MyAlgorithms import ApproximationAlgorithm



if __name__ == '__main__':
    myBFS=BFS()
    person=myBFS.findSeller()
    if person == None:
        print("我没有芒果销售商的人际关系")
    else:
        print(person, "是芒果销售商")

    myDijkstra=Dijkstraalgorithm()
    myDijkstra.findResoult()
    myDijkstra.dumpFormatData()

    myApproximationAlgorithm = ApproximationAlgorithm()
    myApproximationAlgorithm.FindBestSoultion()
    #top=MyApplication()
    #top.setWindowSize(0,0)
    #top.flushdisplay()