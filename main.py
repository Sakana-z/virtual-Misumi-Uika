import pygame
import requests
import os
import pyttsx3
import sys
engine = pyttsx3.init()

# 初始化 Pygame
pygame.init()

# 创建窗口（800x600 像素）
screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("显示图片示例")
# 加载图片（注意图片路径）
# 使用 convert() 提升绘制性能
image = pygame.image.load("background.jpeg").convert()
# 如果是带透明通道的 PNG 图片，使用 convert_alpha()
cac = pygame.image.load("cac.png").convert_alpha()
cac = pygame.transform.scale(cac, (528,800))
position = (300, 100)
# 获取图片的矩形位置
image_rect = image.get_rect()
# 设置图片在窗口中的位置（居中）
image_rect.center = screen.get_rect().center
# 填充背景色（RGB白色）
screen.fill((255, 255, 255))

# 将图片绘制到屏幕上
screen.blit(image, image_rect)
screen.blit(cac, position)

# 更新显示
pygame.display.flip()



def deepseek_chat():
    # 情绪种类
    Negative = 0
    Positive = 0
    # 配置信息
    api_key = "填入api"  # 替换为你的实际API密钥
    api_url = "https://api.deepseek.com/v1/chat/completions"  # 确认使用最新API地址

    # 定义文件路径（根据你的实际路径修改）
    print("选择对话角色")

    # 定义三个txt文件的列表
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']

    # 检查文件是否存在并筛选出可用的文件
    available_files = []
    for file in file_list:
        if os.path.isfile(file):
            available_files.append(file)
        else:
            print(f"提示：文件 {file} 不存在")

    # 如果没有可用文件则退出程序
    if not available_files:
        print("错误：没有可用的文件！")
        exit()

    # 显示可选文件列表
    print("请选择要读取的文件：")
    for index, filename in enumerate(available_files, 1):
        print(f"{index}. {filename}")

    # 获取有效用户输入
    while True:
        try:
            choice = int(input("请输入数字编号选择文件："))
            if 1 <= choice <= len(available_files):
                selected_file = available_files[choice - 1]
                break
            else:
                print(f"请输入1到{len(available_files)}之间的数字！")
        except ValueError:
            print("无效输入，请确保输入的是数字！")

    file_path =selected_file
    #file_path = "提示词.txt"




    # 读取文件内容到字符串
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # 注意编码可能需要调整
            txt_content = file.read()
        print("文件内容已成功读取为字符串！")
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在。")
    except UnicodeDecodeError:
        print(f"错误：文件编码不匹配，请尝试其他编码（如 'gbk'、'latin1'）。")

    # 使用字符串内容
    # print(txt_content)  # 打印内容或进行其他操作

    # 初始化对话历史
    messages = [
        {"role": "system", "content": txt_content}
    ]

    # 设置请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    print("开始对话（输入'exit'退出）")
    while True:
            if Negative >= 5:
                print("saki酱")
                cac2 = pygame.image.load("cac2.png").convert_alpha()
                cac2 = pygame.transform.scale(cac2, (528, 800))
                position = (300, 100)

                # 将图片绘制到屏幕上
                screen.blit(image, image_rect)
                screen.blit(cac2, position)
                # 更新显示
                pygame.display.flip()
            if Positive >= 5:
                print("saki酱")
                cac3 = pygame.image.load("cac3.png").convert_alpha()
                cac3 = pygame.transform.scale(cac3, (528, 800))
                position = (300, 100)

                # 将图片绘制到屏幕上
                screen.blit(image, image_rect)
                screen.blit(cac2, position)
                # 更新显示
                pygame.display.flip()


            # 获取用户输入
            user_input = input("\n用户: ")
            if user_input.lower() == 'exit':
                break

            # 添加用户消息到历史
            messages.append({"role": "user", "content": user_input})

            # 构造请求数据
            payload = {
                "model": "deepseek-reasoner",  # 根据可用模型调整
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1000
            }

            # 发送请求
            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()  # 检查HTTP错误

            # 解析响应
            result = response.json()
            assistant_reply = result['choices'][0]['message']['content']

            # 添加助手回复到历史（注意控制对话长度）
            messages.append({"role": "assistant", "content": assistant_reply})

            #读取情绪
            if "开心" in f"\n助手: {assistant_reply}":
                print(f"检测到字符pos")
                Positive=Positive+1
            if "悲伤" in f"\n助手: {assistant_reply}":
                print(f"检测到字符Neg")
                Negative = Negative + 1
            if "愤怒" in f"\n助手: {assistant_reply}":
                print(f"检测到字符Neg")
                Negative = Negative + 1
            if "恐惧" in f"\n助手: {assistant_reply}":
                print(f"检测到字符Neg")
                Negative = Negative + 1
            if "厌恶" in f"\n助手: {assistant_reply}":
                print(f"检测到字符Neg")
                Negative = Negative + 1


         # 文字
            pygame.display.set_caption("文字绘制示例")
            font = pygame.font.Font("msyh.ttc", 10)
            text_surface = font.render(f"\n助手: {assistant_reply}", True, (50, 50, 50), (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = screen.get_rect().center

            screen.blit(text_surface, text_rect)  # 绘制文本
            pygame.display.flip()
                # 打印回复
            print(f"\n助手: {assistant_reply}")
            print(Positive,Negative)
            engine.say(f"\n助手: {assistant_reply}")
            engine.runAndWait()






if __name__ == "__main__":
    deepseek_chat()


