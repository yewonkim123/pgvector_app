from db_utils import get_conn

def insert_doc(content, embedding):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (content, embedding)
    )
    conn.commit()
    cur.close()
    conn.close()

def search_similar(query_embedding, top_k=3):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, content, embedding <-> %s::vector AS distance
        FROM documents
        ORDER BY distance ASC
        LIMIT %s;
    """, (query_embedding, top_k))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results