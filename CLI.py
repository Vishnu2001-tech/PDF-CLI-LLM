import streamlit as st
from App import add_text_to_collection, get_answer, verify_pdf_path, clear_coll

def main():
    st.title("PDF Processing Streamlit App")

    # Sidebar for user inputs
    st.sidebar.header("User Inputs")
    file_path = st.sidebar.file_uploader("Upload PDF File", type=["pdf"])
    word_limit = st.sidebar.number_input("Word Limit for Text Chunk", value=200)
    question = st.sidebar.text_input("Ask a Question")
    clear_collection = st.sidebar.checkbox("Clear Collection")

    # Process user inputs on button click
    if st.sidebar.button("Process"):
        if file_path:
            try:
                verify_pdf_path(file_path.name)
                confirmation = add_text_to_collection(file=file_path, word=word_limit)
                st.success(confirmation)
            except Exception as e:
                st.error(f"Error processing PDF file: {e}")

        if question:
            try:
                n = st.sidebar.number_input("Number of Results", value=1)
                answer = get_answer(question, n=n)
                st.info(f"Answer: {answer}")
            except Exception as e:
                st.error(f"Error getting answer: {e}")

        if clear_collection:
            try:
                clear_coll()
                st.success("Current collection cleared successfully")
            except Exception as e:
                st.error(f"Error clearing collection: {e}")

if __name__ == "__main__":
    main()

