# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # plt.vlines(1.769, 0, 1,color="red",label='node1 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(1.456, 0, 1,color="blue",label='node2 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(2.59, 0, 1,color="aqua",label='node3 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(3.154, 0, 1,color="darkblue",label='node4 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(2.53, 0, 1,color="gold",label='node5 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(1.371, 0, 1,color="green",label='node6 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(2.667, 0, 1,color="orange",label='node7 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(6.37, 0, 1,color="gray",label='node8 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(3.936, 0, 1,color="pink",label='node9 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.vlines(6.4, 0, 1,color="purple",label='node10 instructive activation value',linestyle="--",linewidth=0.8)#竖线
    # plt.plot([1.4,1.3], [0.073,0.147],marker="o",ms = 2, label='node1',color="red")
    # plt.plot([1.4,1.3],[0.024,0.098],marker="o",ms = 2, label='node2',color="blue")
    # plt.plot([4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[0.024,0.049,0.122,0.147,0.147,0.171,0.22,0.44,0.489],marker="o",ms = 2, label='node3',color="aqua")
    # plt.plot([6.4,5,4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[0.318,0.318,0.318,0.318,0.318,0.318,0.318,0.318,0.366,0.537,0.586],marker="o",ms = 2, label='node4',color="darkblue")
    # plt.plot([3,2.7,2.5,2.3,2,1.4,1.3],[0.098,0.122,0.122,0.147,0.22,0.44,0.489], marker="o",ms = 2,label='node5',color="gold")
    # plt.plot([1.3],[0.049],marker="o",ms = 2, label='node6',color="green")
    # plt.plot([5,4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[0.049,0.073,0.098,0.147,0.171,0.195,0.195,0.244,0.464,0.513], marker="o",ms = 2,label='node7',color="orange")
    # plt.plot([6.4,5,4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[1,1,1,0.977,0.806,0.757,0.733,0.708,0.684,0.782,0.806],marker="o",ms = 2, label='node8',color="gray")
    # plt.plot([6.4,5,4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[0.684,0.635,0.586,0.562,0.513,0.489,0.489,0.464,0.489,0.635,0.66], marker="o",ms = 2,label='node9',color="pink")
    # plt.plot([6.4,5,4.5,4,3,2.7,2.5,2.3,2,1.4,1.3],[1,1,1,1,1,1,1,1,1,1,1],marker= "o",ms = 2,label='node10',color="purple")
    # plt.xlabel('kt/ks')
    # plt.ylabel('storage rate')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    # plt.gca().invert_xaxis()
    # plt.savefig('./ktks_StorageRate.jpg',dpi=500,bbox_inches = 'tight')



    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.103,0.2,0.299,0.396,0.396,0.494,0.591,0.689,0.782,0.879,0.977,1], marker="o",ms=2, label='node1')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.097,0.194,0.292,0.39,0.39,0.488,0.585,0.585,0.782,0.879,0.977,1], marker="o",ms=2, label='node2')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.497,0.497,0.594,0.692,0.692,0.692,0.790,0.790,0.879,0.977,0.977,1], marker="o",ms=2, label='node3')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.586,0.586,0.684,0.684,0.782,0.782,0.782,0.879,0.879,0.977,0.977,1], marker="o",ms=2, label='node4')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.490,0.490,0.587,0.587,0.685,0.685,0.783,0.783,0.879,0.977,0.977,1], marker="o",ms=2, label='node5')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0,0.097,0.194,0.292,0.390,0.488,0.488,0.585,0.782,0.879,0.977,1], marker="o",ms=2, label='node6')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.581,0.581,0.581,0.679,0.679,0.679,0.777,0.777,0.879,0.977,0.977,1], marker="o",ms=2, label='node7')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.879,0.879,0.879,0.879,0.879,0.879,0.879,0.977,0.977,1,1,1], marker="o",ms=2, label='node8')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0.687,0.687,0.785,0.785,0.785,0.785,0.882,0.882,0.879,0.977,0.977,1], marker="o",ms=2, label='node9')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [1,1,1,1,1,1,1,1,1,1,1,1], marker="o",ms=2, label='node10')
    plt.plot([1.4,1.3,1.2,1.1,0.9,0.8,0.7,0.6,0.4,0.2,0.1,0.05], [0,0.053,0.126,0.199,0.343,0.416,0.489,0.562,0.708,0.854,0.927,0.964], marker="o",ms=2, label='theoretical min value',linestyle=":")
    plt.xlabel('kt/ks')
    plt.ylabel('storage rate')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.gca().invert_xaxis()
    plt.tight_layout(pad=0.4, w_pad=5.0, h_pad=5.0)
    plt.savefig('./low_ktks_StorageRate.jpg', dpi=500, bbox_inches='tight')
    plt.show()



    # plt.plot([20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480],[0.553,0.616,0.67,0.69,0.686,0.678,0.688,0.673,0.688,0.682,0.673,0.689,0.683,0.676,0.690,0.687,0.676,0.691,0.686,0.676,0.691,0.693,0.737,0.812] , marker="o",ms=2, label='kt/ks=0.25')
    # plt.plot([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480], [0.527, 0.602, 0.597, 0.61, 0.614, 0.621, 0.613, 0.622, 0.621, 0.612, 0.619, 0.616, 0.608, 0.617, 0.618, 0.611, 0.618, 0.618, 0.613, 0.619, 0.683, 0.706, 0.755, 0.789], marker="o",ms=2, label='kt/ks=0.5')
    # plt.plot([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460], [0.516, 0.535, 0.548, 0.565, 0.563, 0.631, 0.613, 0.618, 0.617, 0.631, 0.627, 0.667, 0.706, 0.71, 0.709, 0.678, 0.716, 0.74, 0.742, 0.723, 0.717, 0.774, 0.71], marker="o",ms=2, label='kt/ks=1.3')
    # plt.plot([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420], [0.498, 0.532, 0.535, 0.532, 0.542, 0.578, 0.58, 0.565, 0.644, 0.649, 0.63, 0.633, 0.646, 0.672, 0.662, 0.678, 0.713, 0.684, 0.735, 0.75, 0.695], marker="o",ms=2, label='kt/ks=2.5')
    # plt.plot([20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400], [0.498,0.494,0.533,0.538,0.535,0.536,0.526,0.549,0.637,0.659,0.678,0.652,0.664,0.669,0.709,0.724,0.720,0.703,0.702,0.827], marker="o",ms=2, label='kt/ks=4')
    # plt.hlines(0.742, 0, 500,color="darkblue",label='under random backup',linestyle="--",linewidth=1)
    # plt.xlabel('storage quantity of documents')
    # plt.ylabel('average load time in second')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    # plt.gca().invert_xaxis()
    # plt.gca().invert_yaxis()
    # plt.tight_layout(pad=0.4, w_pad=5.0, h_pad=5.0)
    # plt.savefig('./new_readingRate.jpg', dpi=500, bbox_inches='tight')
    # plt.show()


    #
    #
    # plt.vlines(45, 0, 0.4,color="gold",label='node5 relative activation value',linestyle=":",linewidth=1)#竖线
    # # plt.hlines(0.261, 0, 1,color="red",label='node1 instructive activation value',linestyle="--",linewidth=0.8)#横线
    # # plt.hlines(0.29, 0, 1,color="blue",label='node2 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.009, 0,60,color="aqua",label='node3 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.078, 0, 60,color="darkblue",label='node4 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(2.53, 0, 60,color="gold",label='node5 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.334, 0, 1,color="green",label='node6 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.02, 0, 60,color="orange",label='node7 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.239, 0, 60,color="gray",label='node8 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.139, 0, 60,color="pink",label='node9 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.395, 0, 60,color="purple",label='node10 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.plot(,,marker="o",ms = 2, label='node1',color="red")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node2',color="blue")
    # plt.plot([ 39,42, 45, 48, 51, 54, 57, 60],[0,0.018, 0.018, 0.018, 0.037, 0.037, 0.037, 0.055],marker="o",ms = 2, label='node3',color="aqua")
    # plt.plot([ 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.018, 0.018, 0.037, 0.037, 0.055, 0.055, 0.073, 0.073, 0.073, 0.092, 0.092, 0.092, 0.11, 0.11, 0.11, 0.128],marker="o",ms = 2, label='node4',color="darkblue")
    # plt.plot([ 45,48, 51, 54, 57, 60],[0,0.015, 0.015, 0.015, 0.034, 0.034], marker="o",ms = 2,label='node5',color="gold")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node6',color="green")
    # plt.plot([ 33,36, 39, 42, 45, 48, 51, 54, 57, 60],[0,0.021, 0.021, 0.021, 0.040, 0.040, 0.040, 0.058, 0.058, 0.058], marker="o",ms = 2,label='node7',color="orange")
    # plt.plot([0,3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0,0.018, 0.037, 0.055, 0.073, 0.092, 0.11, 0.128, 0.147, 0.165, 0.183, 0.202, 0.22, 0.238, 0.238, 0.256, 0.256, 0.256, 0.275, 0.275, 0.275],marker="o",ms = 2, label='node8',color="gray")
    # plt.plot([0,3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0,0.018, 0.037, 0.055, 0.073, 0.073, 0.092, 0.092, 0.11, 0.11, 0.128, 0.128, 0.128, 0.147, 0.147, 0.147, 0.165, 0.165, 0.165, 0.183, 0.183], marker="o",ms = 2,label='node9',color="pink")
    # plt.plot([0,3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0,0.018, 0.037, 0.055, 0.073, 0.092, 0.11, 0.128, 0.147, 0.165, 0.183, 0.202, 0.22, 0.238, 0.256, 0.275, 0.293, 0.311, 0.33, 0.348, 0.366],marker= "o",ms = 2,label='node10',color="purple")
    # plt.xlabel('storage quantity of documents')
    # plt.ylabel('storage rate')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    # # plt.gca().invert_xaxis()
    # plt.savefig('./node5_ktks1.jpg',dpi=500,bbox_inches = 'tight')



    # plt.vlines(84, 0, 0.6,color="gold",label='node5 relative activation value',linestyle=":",linewidth=1)#竖线
    # # plt.hlines(0.261, 0, 1,color="red",label='node1 instructive activation value',linestyle="--",linewidth=0.8)#横线
    # # plt.hlines(0.29, 0, 1,color="blue",label='node2 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.018, 0,100,color="aqua",label='node3 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.156, 0, 100,color="darkblue",label='node4 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(2.53, 0, 60,color="gold",label='node5 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.334, 0, 1,color="green",label='node6 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.04, 0, 100,color="orange",label='node7 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.478, 0, 100,color="gray",label='node8 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.278, 0, 100,color="pink",label='node9 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.79, 0, 100,color="purple",label='node10 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.plot(,,marker="o",ms = 2, label='node1',color="red")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node2',color="blue")
    # plt.plot([ 75, 78, 81, 84, 87, 90, 93, 96, 99],[0,0.018, 0.018, 0.018, 0.037, 0.037, 0.037, 0.055, 0.055],marker="o",ms = 2, label='node3',color="aqua")
    # plt.plot([ 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],[0.0, 0.018, 0.018, 0.037, 0.037, 0.055, 0.055, 0.073, 0.073, 0.092, 0.092, 0.11, 0.11, 0.128, 0.128, 0.128, 0.147, 0.147, 0.147, 0.147, 0.165, 0.165, 0.165, 0.183, 0.183, 0.183, 0.202],marker="o",ms = 2, label='node4',color="darkblue")
    # plt.plot([ 84, 87, 90, 93, 96, 99],[0.0, 0.018, 0.018, 0.018, 0.037, 0.037], marker="o",ms = 2,label='node5',color="gold")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node6',color="green")
    # plt.plot([ 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],[0.0, 0.018, 0.018, 0.018, 0.037, 0.037, 0.037, 0.055, 0.055, 0.055, 0.073, 0.073, 0.073, 0.092], marker="o",ms = 2,label='node7',color="orange")
    # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],[0.018, 0.037, 0.055, 0.073, 0.092, 0.11, 0.128, 0.147, 0.165, 0.183, 0.202, 0.22, 0.238, 0.256, 0.275, 0.293, 0.311, 0.33, 0.348, 0.366, 0.385, 0.403, 0.421, 0.44, 0.458, 0.476, 0.476, 0.495, 0.495, 0.495, 0.513, 0.513, 0.513],marker="o",ms = 2, label='node8',color="gray")
    # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],[0.018, 0.037, 0.055, 0.073, 0.092, 0.11, 0.128, 0.128, 0.147, 0.147, 0.165, 0.165, 0.183, 0.183, 0.202, 0.202, 0.22, 0.22, 0.238, 0.238, 0.238, 0.256, 0.256, 0.256, 0.275, 0.275, 0.275, 0.293, 0.293, 0.293, 0.311, 0.311, 0.311], marker="o",ms = 2,label='node9',color="pink")
    # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],[0.018, 0.037, 0.055, 0.073, 0.092, 0.11, 0.128, 0.147, 0.165, 0.183, 0.202, 0.22, 0.238, 0.256, 0.275, 0.293, 0.311, 0.33, 0.348, 0.366, 0.385, 0.403, 0.421, 0.44, 0.458, 0.476, 0.495, 0.513, 0.531, 0.55, 0.568, 0.586, 0.605],marker= "o",ms = 2,label='node10',color="purple")
    # plt.xlabel('storage quantity of documents')
    # plt.ylabel('storage rate')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    # # plt.gca().invert_xaxis()
    # plt.savefig('./node5_ktks2.jpg',dpi=500,bbox_inches = 'tight')




    # plt.vlines(21, 0, 0.175,color="gold",label='node5 relative activation value',linestyle=":",linewidth=1)#竖线
    # # plt.hlines(0.261, 0, 1,color="red",label='node1 instructive activation value',linestyle="--",linewidth=0.8)#横线
    # # plt.hlines(0.29, 0, 1,color="blue",label='node2 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.0045, 0,27,color="aqua",label='node3 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.039, 0, 27,color="darkblue",label='node4 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(2.53, 0, 60,color="gold",label='node5 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.334, 0, 1,color="green",label='node6 instructive activation value',linestyle="--",linewidth=0.8)
    # plt.hlines(0.01, 0, 27,color="orange",label='node7 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.1195, 0, 27,color="gray",label='node8 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # plt.hlines(0.0695, 0, 27,color="pink",label='node9 Theoretical storage ratio',linestyle="--",linewidth=0.8)
    # # plt.hlines(0.79, 0, 100,color="purple",label='node10 instructive activation value',linestyle="--",linewidth=0.8)
    # # plt.plot(,,marker="o",ms = 2, label='node1',color="red")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node2',color="blue")
    # plt.plot([ 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.0, 0.006, 0.006, 0.006, 0.012, 0.012, 0.012, 0.018, 0.018],marker="o",ms = 2, label='node3',color="aqua")
    # plt.plot([ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.0, 0.006, 0.006, 0.012, 0.012, 0.018, 0.018, 0.024, 0.024, 0.031, 0.031, 0.031, 0.037, 0.037, 0.037, 0.037, 0.043, 0.043, 0.043, 0.049, 0.049, 0.049],marker="o",ms = 2, label='node4',color="darkblue")
    # plt.plot([ 21, 22, 23, 24, 25, 26],[0.0, 0.006, 0.006, 0.006, 0.012, 0.012], marker="o",ms = 2,label='node5',color="gold")
    # # plt.plot([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],marker="o",ms = 2, label='node6',color="green")
    # plt.plot([ 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.0, 0.006, 0.006, 0.006, 0.006, 0.012, 0.012, 0.012, 0.018, 0.018, 0.018, 0.024], marker="o",ms = 2,label='node7',color="orange")
    # plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.006, 0.012, 0.018, 0.024, 0.031, 0.037, 0.043, 0.049, 0.055, 0.061, 0.067, 0.073, 0.079, 0.085, 0.092, 0.098, 0.104, 0.11, 0.116, 0.122, 0.122, 0.122, 0.128, 0.128, 0.128, 0.134],marker="o",ms = 2, label='node8',color="gray")
    # plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.006, 0.012, 0.018, 0.024, 0.031, 0.031, 0.037, 0.037, 0.043, 0.043, 0.049, 0.049, 0.055, 0.055, 0.061, 0.061, 0.061, 0.067, 0.067, 0.067, 0.073, 0.073, 0.073, 0.079, 0.079, 0.079], marker="o",ms = 2,label='node9',color="pink")
    # plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],[0.006, 0.012, 0.018, 0.024, 0.031, 0.037, 0.043, 0.049, 0.055, 0.061, 0.067, 0.073, 0.079, 0.085, 0.092, 0.098, 0.104, 0.11, 0.116, 0.122, 0.128, 0.134, 0.14, 0.147, 0.153, 0.159],marker= "o",ms = 2,label='node10',color="purple")
    # plt.xlabel('storage quantity of documents')
    # plt.ylabel('storage rate')
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    # # plt.gca().invert_xaxis()
    # plt.savefig('./node5_ktks0dot5.jpg',dpi=500,bbox_inches = 'tight')