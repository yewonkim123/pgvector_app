from db_utils import init_vector_table
from vector_ops import insert_doc, search_similar
import numpy as np

init_vector_table()

vec = np.random.rand(1536).tolist()
insert_doc("Hello PGVector!", vec)

results = search_similar(vec)
for r in results:
    print(r)
