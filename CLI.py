import argparse
from App import add_text_to_collection, get_answer, verify_pdf_path, clear_coll

def main():
    parser = argparse.ArgumentParser(description="PDF Processing CLI Tool")
    parser.add_argument("-f", "--file", help="Path to the input PDF file")
    parser.add_argument("-v", "--value", default=200, type=int, help="Optional integer value for no. words in a single chunk")
    parser.add_argument("-q", "--question", type=str, help="Ask a question")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear existing collection data")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of results to be fetched from collection")

    args = parser.parse_args()

    if args.file:
        try:
            verify_pdf_path(args.file)
            confirmation = add_text_to_collection(file=args.file, word=args.value)
            print(confirmation)
        except Exception as e:
            print(f"Error processing PDF file: {e}")

    if args.question:
        try:
            n = args.number if args.number else 1
            answer = get_answer(args.question, n=n)
            print("Answer:", answer)
        except Exception as e:
            print(f"Error getting answer: {e}")

    if args.clear:
        try:
            clear_coll()
            print("Current collection cleared successfully")
        except Exception as e:
            print(f"Error clearing collection: {e}")

if __name__ == "__main__":
    main()
