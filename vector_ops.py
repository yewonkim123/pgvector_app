from db_utils import get_conn
from embedder import get_embedding

def insert_doc(content: str):
    embedding = get_embedding(content)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (content, embedding)
    )
    conn.commit()
    cur.close()
    conn.close()

def search_similar(content: str, top_k: int = 3):
    embedding = get_embedding(content)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, content, embedding <-> %s::vector AS distance
        FROM documents
        ORDER BY distance ASC
        LIMIT %s;
    """, (embedding, top_k))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
