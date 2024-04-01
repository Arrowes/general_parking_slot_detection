import cv2
import os

# 设置输入文件夹和输出文件名
input_folder = 'test_case/test/image'  # 指定包含.png文件的文件夹
output_file = 'output.mp4'          # 输出MP4文件名

# 获取文件夹中所有.png文件的列表
png_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# 排序文件列表以确保按顺序合并图像
png_files.sort()

# 获取第一个图像的尺寸，以便设置输出视频的分辨率
first_image = cv2.imread(os.path.join(input_folder, png_files[0]))
height, width, layers = first_image.shape

# 创建视频编码器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4编码
out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

# 逐个添加图像到视频
for png_file in png_files:
    img = cv2.imread(os.path.join(input_folder, png_file))
    out.write(img)

# 释放视频编码器
out.release()

print("MP4视频已创建：", output_file)
