
import streamlit as st
from PIL import Image
import os
import pyttsx3

from utils.image_preprocessing import preprocess_image
from utils.paddle_ocr import extract_text_paddle
from utils.syntax_fixer import clean_extracted_code
from utils.code_formatter import format_code
from utils.code_runner import run_code
from utils.save_file import save_code
from utils.language_detector import detect_language
from utils.text_cleaner import clean_handwritten_text

os.makedirs("temp", exist_ok=True)


def speak_explanation(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 160)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
    except:
        pass


st.set_page_config(
    page_title="AI Handwritten Code Converter",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #cbd5e1;
        text-align: center;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">AI Handwritten Code to Digital Code System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload handwritten images and automatically extract, correct, format, detect language, execute code, and clean handwritten text</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.title("⚙️ Settings")

    selected_theme = st.selectbox(
        "Choose Theme",
        ["Dark Professional", "Light Minimal"]
    )

    supported_languages = [
        "Auto Detect",
        "Python",
        "Java",
        "C++",
        "JavaScript"
    ]

    language_choice = st.selectbox(
        "Programming Language",
        supported_languages
    )

    st.info(
        """
Supported OCR Engines:
- PaddleOCR
- TrOCR
- EasyOCR

Supported Features:
- Handwritten Code Detection
- Handwritten Text Extraction
- Dirty Handwriting Cleaning
- AI Auto Correction
- Teacher Explanation
- Chatbot Assistant
        """
    )

mode_choice = st.radio(
    "Choose System Mode",
    ["Handwritten Code", "Handwritten Text"],
    horizontal=True
)

uploaded_file = st.file_uploader(
    "Upload Handwritten Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    uploaded_image_path = "temp/uploaded_image.png"

    with open(uploaded_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing handwritten image..."):
        processed_image = preprocess_image(uploaded_image_path)
        extracted_text = extract_text_paddle(processed_image)

        if mode_choice == "Handwritten Text":
            detected_language = "text"
        elif language_choice == "Auto Detect":
            detected_language = detect_language(extracted_text)
        else:
            detected_language = language_choice.lower()

            if detected_language == "c++":
                detected_language = "cpp"

        if detected_language == "text":
            cleaned_code = extracted_text
            formatted_code = clean_handwritten_text(extracted_text)
        else:
            cleaned_code = clean_extracted_code(
                extracted_text,
                detected_language
            )

            formatted_code = format_code(
                cleaned_code,
                detected_language
            )

        if detected_language != "text":
            execution_output = run_code(
                formatted_code,
                detected_language
            )
        else:
            execution_output = "Handwritten text extracted and corrected successfully."

        teacher_message = "Your code executed successfully."

        if "SyntaxError" in execution_output:
            teacher_message = "There is a syntax error in your code. Please check brackets, quotes, colons, or indentation."
        elif "IndentationError" in execution_output:
            teacher_message = "There is an indentation mistake in your code."
        elif "ModuleNotFoundError" in execution_output:
            teacher_message = "A required library is missing. Install it using pip install library_name."
        elif detected_language == "text":
            teacher_message = "The handwritten text has been cleaned by correcting spelling mistakes, spacing, punctuation, and readability."

        chatbot_response = ""

        if detected_language == "python":
            chatbot_response = "This looks like Python code. Make sure indentation is correct."
        elif detected_language == "java":
            chatbot_response = "This looks like Java code. Make sure class and main method are present."
        elif detected_language == "cpp":
            chatbot_response = "This looks like C++ code. Ensure headers and semicolons are correct."
        elif detected_language == "javascript":
            chatbot_response = "This looks like JavaScript code. Check brackets and function syntax."
        elif detected_language == "text":
            chatbot_response = "The handwritten text was cleaned and corrected for readability."

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📷 Uploaded Image")
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with row1_col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 Detected Language")
        st.success(detected_language.upper())
        st.markdown('</div>', unsafe_allow_html=True)

    if mode_choice == "Handwritten Text":

        st.markdown("## 📝 Handwritten Text Results")

        text_col1, text_col2 = st.columns(2)

        with text_col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📄 Raw Extracted Text")
            st.text_area(
                "Raw OCR Output",
                value=extracted_text,
                height=300
            )
            st.markdown('</div>', unsafe_allow_html=True)

        with text_col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("✨ Corrected Text")
            st.text_area(
                "AI Corrected Output",
                value=formatted_code,
                height=300
            )
            st.markdown('</div>', unsafe_allow_html=True)

    else:

        st.markdown("## 💻 Handwritten Code Results")

        code_col1, code_col2 = st.columns(2)

        with code_col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📄 Raw Extracted Code")
            st.code(extracted_text, language=detected_language)
            st.markdown('</div>', unsafe_allow_html=True)

        with code_col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("✅ Corrected & Formatted Code")
            st.code(formatted_code, language=detected_language)
            st.markdown('</div>', unsafe_allow_html=True)

    output_col1, output_col2 = st.columns(2)

    with output_col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("▶️ Execution Output")
        st.text_area("Program Output", execution_output, height=200)
        st.subheader("🎓 Teacher Explanation")
        st.info(teacher_message)
        st.markdown('</div>', unsafe_allow_html=True)

    with output_col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🤖 AI Chatbot Assistant")
        st.success(chatbot_response)
        st.markdown('</div>', unsafe_allow_html=True)

    file_extension = "txt"

    if detected_language == "python":
        file_extension = "py"
    elif detected_language == "java":
        file_extension = "java"
    elif detected_language == "cpp":
        file_extension = "cpp"
    elif detected_language == "javascript":
        file_extension = "js"

    file_path = save_code(formatted_code)

    with open(file_path, "rb") as file:
        st.download_button(
            label="⬇️ Download Corrected File",
            data=file,
            file_name=f"corrected_output.{file_extension}",
            mime="text/plain"
        )

else:
    st.info("Please upload a handwritten image to begin.")
