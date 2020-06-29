import pickle
import os

card_list=None

#card_list=[{"name":"张三",
#               "phone":"11111111",
#               "qq":"123456",
#               "email":"abc"}]

def load_data():
    data=[]
    if os.path.exists("data.pkl"):
        with open('data.pkl','rb') as input:
            data = pickle.load(input)
    return data

def save_data():
    global card_list
    if (card_list is not None) and len(card_list)>0:
        with open('data.pkl','wb') as output:
            pickle.dump(card_list,output)
        card_list=None

def get_card_list():
    global card_list
    if card_list is None:
        card_list=load_data()
    return card_list

def show_menu():

    """显示菜单"""
    print()
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print()
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print()
    print("0. 退出系统")
    print("*" * 50)
    print()

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    name=input("请输入姓名：").strip()
    phone=input("请输入电话：").strip()
    qq=input("请输入QQ：").strip()
    email=input("请输入邮箱：").strip()

    # TODO 验证数据有效

    card_dict={"name":name,
               "phone":phone,
               "qq":qq,
               "email":email}

    get_card_list().append(card_dict)    
    save_data()
    #print(card_list)
    print("添加 %s 的名片成功！" % name)


def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    if len(get_card_list())==0:
        print("当前没有任何名片记录，请使用新增功能添加名片！")
        return

    print_head()
    
    for card_dict in get_card_list():
        print_card(card_dict)
        

def print_card(card_dict):
    print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                card_dict["phone"],
                card_dict["qq"],
                card_dict["email"]))
    
def print_head():
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")

    print()
    print("=" * 50)

def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    find_name=input("请输入要搜索的姓名：").strip()

    for card_dict in get_card_list():
        if card_dict["name"]==find_name:
            print_head()
            print_card(card_dict)
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到 %s" % find_name)
        return

def deal_card(find_card):
    #print(find_card)
    action_str=input("请选择要执行的操作 "
                     "[1] 修改 [2] 删除 [0] 返回上级菜单").strip()

    modified=False
    if action_str=="1":
        # TODO 验证数据有效

        find_card["name"]=input_card_info(find_card["name"], "姓名：").strip()
        find_card["phone"]=input_card_info(find_card["phone"], "电话：").strip()
        find_card["qq"]=input_card_info(find_card["qq"], "QQ：").strip()
        find_card["email"]=input_card_info(find_card["email"], "邮箱：").strip()

        modified=True
        print("修改名片成功！")
        
    elif action_str=="2":
        card_list.remove(find_card)
        modified=True        
        print("删除名片成功！")

    if modified==True:
        save_data()

def input_card_info(default_value,prompt):
    input_str=input(prompt).strip()

    if len(input_str)>0:
        return input_str
    else:
        return default_value
