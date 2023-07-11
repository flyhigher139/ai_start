import openai
import os
from openai.embeddings_utils import cosine_similarity, get_embedding

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
# openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_key = os.environ["AZURE_OPENAI_KEY"]

EMBEDDING_MODEL = "text-embedding-ada-002"

# 获取"好评"和"差评"的embedding
positive_preview = get_embedding("好评", EMBEDDING_MODEL)
negative_preview = get_embedding("差评", EMBEDDING_MODEL)

positive_example = get_embedding(
    "买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质", EMBEDDING_MODEL)
negative_example = get_embedding("降价厉害，保价不合理，不推荐", EMBEDDING_MODEL)


def get_score(sample_embedding):
    return cosine_similarity(sample_embedding, positive_preview) - cosine_similarity(sample_embedding, negative_preview)


positive_score = get_score(positive_example)
negative_score = get_score(negative_example)
print("好评例子的评分 : %f" % positive_score)
print("差评例子的评分 : %f" % negative_score)
