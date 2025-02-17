**AI_Pyramid: A Web-Based AI-Driven Triangle Pattern Generator**  
**Overview**  
AI_Pyramid is an innovative web application that leverages artificial intelligence to generate right-aligned triangle patterns. Built with Flask, HTML, CSS, and JavaScript, this interactive tool allows users to specify the number of rows and uses AI algorithms to generate the patterns in real time.

**Features**  
✅ AI-powered pattern generation for dynamic and optimized results  
✅ User-friendly web interface with seamless interaction  
✅ Real-time updates powered by Flask API  
✅ Responsive UI for an intuitive experience on all devices  
✅ Smart error handling to guide users through invalid inputs  
✅ Instant pattern updates without page reloads  

**Technologies Used**  
- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS, JavaScript (AJAX)  
- **AI Integration**: AI algorithms for pattern optimization  
- **Styling**: CSS for responsiveness and modern design  

**Installation**  
**Prerequisites**  
- Python 3.x installed  
- Flask installed (`pip install flask`)

**Steps**  
1. Clone the Repository  
   ```bash
   git clone https://github.com/DarkDev20/AI_Pyramid.git
   cd AI_Pyramid
   ```

2. Install Dependencies  
   ```bash
   pip install flask
   ```

3. Run the Application  
   ```bash
   python app.py
   ```

4. Open in Browser  
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

**Project Structure**  
```
AI_Pyramid/
│── app.py                # Flask backend with AI pattern generation
│── templates/
│   └── index.html        # Frontend UI with pattern display
│── static/
│   ├── styles.css        # CSS styling for UI
│   └── script.js         # JavaScript for AJAX-based interaction
│── README.md             # Project documentation
```

**Usage**  
1. Enter the number of rows for your desired triangle pattern.  
2. Click the "Generate" button.  
3. Watch as AI intelligently creates and displays the pattern on your screen.

**Example Output**  
For an input of 5 rows, the pattern generated will be:

```
    *
   **
  ***
 ****
*****
```

**Future Enhancements**  
🎨 Add various AI-generated pattern styles  
📐 Implement support for different triangle orientations (left-aligned, centered)  
🌐 Deploy the application as a live web service  

Happy coding with AI! 🚀
