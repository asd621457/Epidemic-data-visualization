import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import utils

data = utils.get_wordcloud_data()
text = ""
for item in data:
    text =  text + item[0]

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))


image = Image.open(r'.\static\assets\img\tree.jpg')   #打开遮罩图片
img_array = np.array(image)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="C:\\Windows\\Fonts\\STXINGKA.TTF"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

plt.show()    #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'.\static\assets\img\word3.jpg',dpi=500)

















