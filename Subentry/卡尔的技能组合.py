# 三重冰！急速冷却！塞卓昂的无尽战栗🌀🌀🌀🌀🌀🌀
# 冰冰雷！幽灵漫步！米瑞特之阻碍👻👻👻👻👻👻
# 冰冰火！寒冰之墙！科瑞克斯的杀戮之墙🧊🧊🧊🧊🧊🧊
# 三重雷！电磁脉冲！西美尔的精华脉动⚡⚡⚡⚡⚡⚡
# 雷雷冰！强袭飓风！托纳鲁斯之爪🌪️🌪️🌪️🌪️🌪️🌪️
# 三重火！阳炎冲击！哈雷克之火葬魔咒🔥🔥🔥🔥🔥🔥
# 火火雷！混沌陨石！塔拉克的天坠之火🌠🌠🌠🌠🌠🌠
# 冰雷火！超震声波！布鲁冯特之无力声波🔊🔊🔊🔊🔊🔊
# 雷雷火！灵动迅捷！盖斯特的猛战号令⚔️⚔️⚔️⚔️⚔️⚔️
# 火火冰！熔炉精灵！无中生有的援军！卡尔维因的致邪造物😈😈😈😈😈😈

import itertools


def count_combinations(m, n):
    # 创建一个包含m种颜色的球的列表
    colors = list(range(m))

    # 使用itertools.combinations_with_replacement生成所有可能的组合
    combinations = list(itertools.combinations_with_replacement(colors, n))

    # 返回组合的数量
    return len(combinations)


print(count_combinations(3, 3))
