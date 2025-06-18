import argparse
from db_utils import init_vector_table
from vector_ops import insert_doc, search_similar

def main():
    parser = argparse.ArgumentParser(description="PGVector App with auto-embedding")
    parser.add_argument("--mode", type=str, choices=["insert", "search"], required=True)
    parser.add_argument("--text", type=str, required=True)
    parser.add_argument("--top_k", type=int, default=3)

    args = parser.parse_args()
    init_vector_table()

    if args.mode == "insert":
        insert_doc(args.text)
        print(f"Inserted: '{args.text}'")

    elif args.mode == "search":
        results = search_similar(args.text, args.top_k)
        print("Search results:")
        for r in results:
            print(f"ID: {r[0]} | Text: {r[1]} | Distance: {r[2]:.4f}")

if __name__ == "__main__":
    main()
