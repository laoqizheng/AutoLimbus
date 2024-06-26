import cv2

none_list = [
    # 信念
    cv2.imread('./pic/dungeon/store/buy_list/i.png'),
    # 膏血
    cv2.imread('./pic/dungeon/store/buy_list/c.png'),
    # 金瓮
    cv2.imread('./pic/dungeon/store/buy_list/f.png'),
    # 鲜血装饰
    cv2.imread('./pic/dungeon/store/buy_list/bl.png'),
]
bleed_list = [
    # 锈蚀的美工刀
    cv2.imread('./pic/dungeon/store/buy_list/k.png'),
    # 安息之地
    cv2.imread('pic/dungeon/store/buy_list/respite.png'),
    # 被扣留的颂歌
    cv2.imread('pic/dungeon/store/buy_list/arrested_hymn.png'),
    # 纠缠捆束
    cv2.imread('pic/dungeon/store/buy_list/tangled_bundle.png'),
]
poise_list = [
    # 四叶草
    cv2.imread('pic/dungeon/store/buy_list/si.png'),
    # 雾化吸入器
    cv2.imread('pic/dungeon/store/buy_list/wu.png'),
    # 留恋
    cv2.imread('pic/dungeon/store/buy_list/finifugality.png'),
    # 追忆吊坠
    cv2.imread('./pic/dungeon/store/buy_list/b.png'),
    # 烟斗
    cv2.imread('./pic/dungeon/store/buy_list/g.png'),
    # 老旧的木雕人偶
    cv2.imread('pic/dungeon/store/buy_list/old_wooden_doll.png'),
]
pierce_list = [
    # 黏性淤浆
    cv2.imread('./pic/dungeon/store/buy_list/h.png'),
]

list = [*bleed_list, *poise_list, *pierce_list, *none_list]