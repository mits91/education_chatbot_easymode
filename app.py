from flask import Flask, render_template, request, jsonify
import openai
import unicodedata

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your-API-key'

def remove_accents(input_str):
    """Αφαιρεί τους τόνους από τα ελληνικά γράμματα."""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000
    )
    return response.choices[0].message["content"].strip()

def is_science_question(prompt):
    science_keywords = [
        "περιοδικός", "πίνακας", "χημεία", "ηλεκτρόνια", "κατανομή", "ατομική",
        "ακτίνα", "στοιχείο", "χημικός", "ισότοπο", "ενέργεια", "δεσμός", "επιστήμη","επιστημονικός","χημική","τύπος","σθένος","σθένους",
        "στοιχείο","στοιχεία","Moseley","Μόζλεϋ","Μόζλι","Μόζλεϊ","Μόζλει", "Mendeleev","Μεντελέγιεφ","Μεντελέεφ","Μεντελέεβ","Μεντελέεβ","Μεντελέεφ",
        "Newlands","Νιούλαντς","Νιούλαντζ","Meyer","Μέγιερ", "νόμος","μόρια","μοριακή","μοριακά","μοριακό","μοριακοί","μοριακές","μοριακούς","μοριακά","άτομα","άτομο",
        "περιοδικού", "πίνακα", "χημείας", "ηλεκτρόνιων", "κατανομές", "ατομικών","ακτίνας", "στοιχείου", "χημικού", "ισοτόπου", "ενέργειας", "δεσμού", "επιστήμης",
        "επιστημονικού","χημικής","τύπου","σθένους","σθένος"
    ]
    # remove accents and convert to lowercase for comparison
    prompt_no_accents = remove_accents(prompt.lower())
    return any(remove_accents(keyword) in prompt_no_accents for keyword in science_keywords)

# Initialize conversation
messages = [
    {"role": "system", "content": "Είσαι ένας φιλικός επιστημονικός βοηθός. Απαντάς μόνο σε ερωτήσεις σχετικές με την επιστήμη. Δίνεις πλήρεις απαντήσεις."}
]

last_science_question = None

@app.route("/")
def index():
    # Serve the HTML page when visiting the root URL
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    global last_science_question

    data = request.get_json()
    user_prompt = data['question']

    if is_science_question(user_prompt) or (last_science_question and "πες μου περισσότερα" in user_prompt.lower()):
        # Add user message to conversation
        messages.append({"role": "user", "content": user_prompt})
        
        # Generate response
        response = generate_response(messages)
        
        # Add assistant message to conversation
        messages.append({"role": "assistant", "content": response})

        # Update last science question
        last_science_question = user_prompt if is_science_question(user_prompt) else last_science_question

        return jsonify({"response": response})
    else:
        return jsonify({"response": "Αυτό είναι εκτός θέματος, παρακαλώ εστιάστε στη μελέτη."})

if __name__ == '__main__':
    app.run(debug=True)
