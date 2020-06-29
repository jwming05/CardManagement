import cards_tools

ACTION_ADD="1"
ACTION_SHOW_ALL="2"
ACTION_SEARCH="3"

ACTION_QUIT="0"

while True:
    cards_tools.show_menu()

    action_str=input("请选择希望执行的操作：").strip()
    print("您选择的操作是【%s】" % action_str)

    if action_str in [ACTION_ADD,ACTION_SHOW_ALL,ACTION_SEARCH]:
        if action_str == ACTION_ADD:
            cards_tools.new_card()
        elif action_str==ACTION_SHOW_ALL:
            cards_tools.show_all()
        elif action_str==ACTION_SEARCH:
            cards_tools.search_card()

    elif action_str == ACTION_QUIT:
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请重新选择")
