# import yaml
#
#
# data_msg = {"aa": 77,
#      "bb":{"cc":66}
#      }
#
#
# # 读取
# with open("yaml/read.yaml", 'r', encoding="UTF8") as f:
#     msg = yaml.safe_load(f)
#     print(msg)
#
#
# # 追加
# with open("yaml/additional.yaml", 'a', encoding="UTF8") as f:
#     yaml.dump(data_msg, f)
#
#
# # 写入
# with open("yaml/write.yaml", 'w', encoding="UTF8") as f:
#     yaml.dump(data_msg, f)
