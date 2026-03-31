
 AI Handwritten Code & Text Converter System

## Project Title
AI-Powered Handwritten Code and Text Converter with Auto-Correction and Chatbot Assistance

## Introduction
This system is an AI-based application that converts handwritten code and handwritten text into digital format. It helps users by extracting handwritten content from images, correcting mistakes automatically, formatting code properly, and displaying both raw and corrected output.
The system is useful for students, developers, teachers, doctors, and office users who want to digitize handwritten notes, code, prescriptions, and documents.

## Problem Statement
Many users write code or notes on paper, but converting them into digital text manually takes a lot of time and can introduce errors.
Traditional OCR tools often fail to:
* Detect messy handwriting accurately
* Correct spelling mistakes
* Correct coding syntax errors
* Format code properly
* Show raw and corrected output separately
This system solves these problems using AI and image processing.

## Objectives
* Convert handwritten code into executable digital code
* Convert handwritten text into editable digital text
* Show raw extracted output and corrected output separately
* Automatically detect and fix code syntax errors
* Automatically correct spelling mistakes in handwritten text
* Highlight incorrect words and coding mistakes
* Support dirty or unclear handwriting with better accuracy
* Provide chatbot assistance for user queries
* 
## Main Features

### Handwritten Code Conversion

* Extract handwritten programming code from image
* Detect code language automatically
* Show raw extracted code
* Show corrected and formatted code
* Fix common errors like:

  * pritn → print
  * missing colon
  * wrong indentation
  * missing brackets
  * wrong variable names

### Handwritten Text Conversion

* Extract handwritten text from image
* Show raw OCR output
* Show corrected text output
* Correct spelling mistakes only
* Preserve original sentence meaning
* Work on notes, essays, and prescriptions

### AI Chatbot Assistant

* Gives suggestions about extracted code
* Explains corrected code
* Helps user understand text corrections
* Provides simple guidance and error explanations

### Error Highlighting

* Incorrect code lines shown separately
* Wrong text words can be highlighted
* Corrected words are displayed in readable format

---

## Technologies Used

* Python
* Streamlit
* OpenCV
* EasyOCR
* NumPy
* Pillow
* PySpellChecker
* Autopep8
* Black Formatter
* Pytesseract (optional)

---

## Modules of the System

1. Image Upload Module
2. Handwritten Code Extraction Module
3. Handwritten Text Extraction Module
4. Code Correction Module
5. Text Correction Module
6. Chatbot Assistance Module
7. Output Display Module

## System Workflow

1. User uploads handwritten image
2. System preprocesses the image
3. OCR extracts handwritten text/code
4. Raw output is displayed
5. AI correction module fixes mistakes
6. Corrected output is displayed
7. Chatbot provides explanation and suggestions

## Advantages

* Saves time
* Reduces manual typing effort
* Improves accuracy
* Easy to use interface
* Helpful for students and developers
* Works with messy handwriting
* Gives both raw and corrected results

## Applications

* Educational institutes
* Coding classes
* Student assignments
* Doctor prescription reading
* Office document digitization
* Note conversion systems
* Software development learning
* 
## Future Scope

* Support multiple languages
* Add voice explanation feature
* Add PDF export feature
* Add cloud storage integration
* Improve doctor prescription recognition
* Add support for more programming languages
* Add offline mode

---

## Conclusion

The AI Handwritten Code and Text Converter is a smart and useful system that converts handwritten content into digital format accurately. It not only extracts handwritten code and text but also corrects mistakes automatically, making the system more intelligent and user-friendly.
