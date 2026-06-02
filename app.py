from flask import Flask, render_template, request, jsonify
import random
import datetime

app = Flask(__name__)

# Bot responses database
bot_responses = {
    "greetings": [
        "Hello! Welcome to your internship assistant! 🎓",
        "Hi there! Ready to make the most of your internship? 🚀",
        "Hey! I'm here to help you succeed in your internship! 💼"
    ],
    "tasks": [
        "For your internship, try to: Complete assigned tasks on time, ask questions, take notes, and network with colleagues! 📋",
        "Key internship tips: Be proactive, seek feedback, learn company tools, and document your learnings! ✨",
        "Make your internship count: Set goals, meet deadlines, collaborate, and build relationships! 🎯"
    ],
    "skills": [
        "Focus on these skills: Communication, problem-solving, time management, and adaptability! 💪",
        "Top internship skills: Technical expertise, teamwork, critical thinking, and professionalism! 🌟",
        "Develop: Active listening, attention to detail, initiative, and a growth mindset! 🧠"
    ],
    "networking": [
        "Network smartly: Attend team meetings, introduce yourself, connect on LinkedIn, and ask for coffee chats! ☕",
        "Build connections: Be genuine, show interest in others' work, and maintain professional relationships! 🤝",
        "Networking tip: Follow up after meetings, thank mentors, and stay in touch even after internship ends! 📬"
    ],
    "feedback": [
        "Seek feedback actively: Ask 'How can I improve?' and 'What did I do well?' regularly! 📝",
        "Handle feedback gracefully: Listen without defending, ask clarifying questions, and implement changes! 🔄",
        "Feedback is a gift: Schedule regular check-ins with your supervisor and be open to constructive criticism! 🎁"
    ],
    "challenges": [
        "Facing challenges? Break tasks into smaller steps, ask for help when needed, and stay positive! 💪",
        "Overcome obstacles: Stay organized, prioritize tasks, and don't hesitate to reach out to your mentor! 🆘",
        "When stuck: Research first, then ask specific questions. Show your effort before seeking help! 🔍"
    ],
    "goodbye": [
        "Good luck with your internship! You've got this! 🌟",
        "Keep pushing forward! Your hard work will pay off! 🚀",
        "Wishing you success in your internship journey! 🎉"
    ],
    "default": [
        "That's interesting! Tell me more about your internship experience! 🤔",
        "I'm here to help with your internship questions. What would you like to know? 💡",
        "Great question! Keep exploring and learning during your internship! 📚"
    ]
}

def get_bot_response(user_message):
    user_message = user_message.lower()

    if any(word in user_message for word in ['hi', 'hello', 'hey', 'greetings']):
        return random.choice(bot_responses["greetings"])
    elif any(word in user_message for word in ['task', 'work', 'assignment', 'job', 'duty']):
        return random.choice(bot_responses["tasks"])
    elif any(word in user_message for word in ['skill', 'learn', 'improve', 'develop', 'ability']):
        return random.choice(bot_responses["skills"])
    elif any(word in user_message for word in ['network', 'connect', 'colleague', 'team', 'people']):
        return random.choice(bot_responses["networking"])
    elif any(word in user_message for word in ['feedback', 'review', 'criticism', 'advice']):
        return random.choice(bot_responses["feedback"])
    elif any(word in user_message for word in ['problem', 'challenge', 'difficult', 'stuck', 'hard']):
        return random.choice(bot_responses["challenges"])
    elif any(word in user_message for word in ['bye', 'goodbye', 'see you', 'later']):
        return random.choice(bot_responses["goodbye"])
    else:
        return random.choice(bot_responses["default"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_reply = get_bot_response(user_message)

    return jsonify({
        'response': bot_reply,
        'timestamp': datetime.datetime.now().strftime('%H:%M')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
