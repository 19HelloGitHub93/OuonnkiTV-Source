import json

# 配置路径
BASE_PATH = "tv_source/OuonnkiTV"
OUTPUT_DIR = "tv_source/KVideo"
FILE1 = f"{BASE_PATH}/full-noadult.json"
FILE2 = f"{BASE_PATH}/adult.json"
GROUP1="normal"
GROUP2="premium"
OUTPUT = f"{OUTPUT_DIR}/kvideo-all.json"

def convert_item(filepath: str, group: str, start_priority: int):
    """
    读取文件，转换每一项，自动递增priority
    :return: 转换后的列表, 下一个可用priority
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw_list = json.load(f)

    out = []
    current_p = start_priority
    for obj in raw_list:
        #obj.pop("type", None)
        current_p += 1
        new_item = {
            "id": obj["id"],
            "name": obj["name"],
            "baseUrl": obj["url"],
            "group": obj.get("group", group),
            "enabled": obj.get("enabled", True),
            "priority": current_p,
        }
        out.append(new_item)
    return out, current_p

if __name__ == "__main__":
    list1, next_p = convert_item(FILE1,GROUP1, start_priority=0)
    list2, final_p = convert_item(FILE2,GROUP2, start_priority=next_p)

    merged = list1 + list2

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=4)

    print(f"✅ 合并完成！总源数量：{len(merged)}")
    print(f"输出文件：{OUTPUT}")
