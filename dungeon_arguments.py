import cv2

# 合成饰品材料
fused_gifts = (False, False)
# 合成饰品
fused_result = False
# 当前卡包是否拥有合成饰品材料
need_card_gift = False


fused_gifts_1 = cv2.imread('./pic/dungeon/floor/floor_rewards/smokes_and_wires.png')
fused_gifts_2 = cv2.imread('./pic/dungeon/floor/floor_rewards/rusted_muzzle.png')