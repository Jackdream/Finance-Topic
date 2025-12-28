import jieba
from collections import Counter

text = "这是一段需要被分词的中文文本。"
# 中文分词
words = jieba.lcut(text)
# 后续统计步骤与英文相同
word_counts = Counter(words)
print(word_counts.most_common(5))