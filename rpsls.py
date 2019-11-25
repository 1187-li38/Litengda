#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李腾达
日期：2019/11/20
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
        print("您的选择为:%s"%(name))
        name=0
    elif name=='史波克':
        print("您的选择为:%s"%(name))
        name=1
    elif name=='纸':
        print("您的选择为:%s"%(name))
        name=2
    elif name=='蜥蜴':
        print("您的选择为:%s"%(name))
        name=3
    elif name=='剪刀':
        print("您的选择为:%s"%(name))
        name=4
    else:
        print("Error: No Correct Name")
    return name


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        computer_print='石头'
        print("计算机的选择为：石头")
        number=0
    elif number==1:
        computer_print='史波克'
        print("计算机的选择为：史波克")
        number=1
    elif number==2:
        computer_print='纸'
        print("计算机的选择为：纸")
        number=2
    elif number==3:
        computer_print='蜥蜴'
        print("计算机的选择为：蜥蜴")
        number=3
    else:
        computer_print='剪刀'
        print("计算机的选择为：剪刀")
        number=4
    return number

    


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("---------------------")
    if choice_name=='石头' or choice_name=='剪刀' or choice_name=='史波克' or choice_name=='蜥蜴' or choice_name=='纸':
        player_choice_number=name_to_number(choice_name)
        comp_number=random.randrange(0,5)
        number_to_name(comp_number)
        if player_choice_number==0 and comp_number==3 :
            print("您赢了")
        elif player_choice_number==0 and comp_number==4:
            print("您赢了")
        elif player_choice_number==1 and comp_number==4:
            print("您赢了")
        elif player_choice_number==1 and comp_number==0:
            print("您赢了")
        elif player_choice_number==2 and comp_number==0:
            print("您赢了")
        elif player_choice_number==2 and comp_number==1:
            print("您赢了")
        elif player_choice_number==3 and comp_number==2:
            print("您赢了")
        elif player_choice_number==3 and comp_number==1:
            print("您赢了")
        elif player_choice_number==4 and comp_number==3:
            print("您赢了")
        elif player_choice_number==4 and comp_number==2:
            print("您赢了")
        elif player_choice_number==comp_number:
            print("您和机器的选择一样，所以此局平局")
        else:
            print("机器赢了")
    else:
	    name_to_number(choice_name)
   
    


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
