# 龙芯上汉诺塔的演示
## Five-order Hanoi
在这个文件夹中包含hanoi.py与input.txt，在使用时需要在此文件夹下存入待识别的图片(例如1.bmp)，然后在终端输入

    python hanoi.py --image 1.bmp
此时可以得到step.txt文件，里面记录的是操作汉诺塔的步骤

本代码支持修改汉诺塔的截止状态，打开input.txt，其自上而下的三行分别对应从左至右的三根柱子，第一列统一为柱子上盘片的数量，其后从大至小分别记录盘片

    0
    0
    5 5 4 3 2 1
在完成一次识别-生成步骤后，务必删除step.txt文件，再进行下一次运行。
## Three-order Hanoi
在这个文件夹包含final.py，mail.py，open_uart.py，input.txt，在使用时需要在此文件夹下存入待识别的图片(例如1.bmp)，然后在终端输入

    python final.py --image 1.bmp
    python mail.py
    python open_uart.py
此时可以得到control.txt文件，里面记录的是串口通信的记录，并且将操作发送至机械臂

与Five-order Hanoi相同，其记录截止状态的input.txt也可以进行更改，语法与其一致

在完成一次识别-生成步骤后，务必删除step.txt，temp.txt与control.txt文件，再进行下一次运行。
## camshot-master
该文件夹保存了拍摄照片的代码实现方法
## contours.py
该代码可以可视化地观察：程序识别出的汉诺塔盘片的轮廓，该程序会生成一张带有矩形轮廓和其颜色标签的图像，也可以通过此程序预先检查识别模块是否正常工作
    
    python contours.py --image 1.bmp
