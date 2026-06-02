// ===== CHAT BOT JAVASCRIPT =====
document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const typingIndicator = document.getElementById('typingIndicator');
    const quickReplies = document.getElementById('quickReplies');
    const clearChatBtn = document.getElementById('clearChat');

    let isTyping = false;

    // ===== SEND MESSAGE =====
    function sendMessage() {
        const message = userInput.value.trim();
        if (!message || isTyping) return;

        // Add user message
        addMessage(message, 'user');
        userInput.value = '';
        userInput.focus();

        // Show typing indicator
        showTyping();

        // Send to server
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            hideTyping();
            setTimeout(() => {
                addMessage(data.response, 'bot', data.timestamp);
            }, 500);
        })
        .catch(error => {
            hideTyping();
            console.error('Error:', error);
            addMessage('Sorry, I encountered an error. Please try again! 😅', 'bot');
        });
    }

    // ===== ADD MESSAGE TO CHAT =====
    function addMessage(text, sender, time = null) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const now = time || new Date().toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit',
            hour12: false 
        });

        const avatarIcon = sender === 'bot' ? 'fa-robot' : 'fa-user';
        const bubbleClass = sender === 'bot' ? 'bot-bubble' : 'user-bubble';

        // Format text with paragraphs
        const formattedText = text.split('\n').map(line => `<p>${line}</p>`).join('');

        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas ${avatarIcon}"></i>
            </div>
            <div class="message-content">
                <div class="message-bubble ${bubbleClass}">
                    ${formattedText}
                </div>
                <span class="message-time">${now}</span>
            </div>
        `;

        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    // ===== SHOW/HIDE TYPING INDICATOR =====
    function showTyping() {
        isTyping = true;
        typingIndicator.style.display = 'flex';
        scrollToBottom();
    }

    function hideTyping() {
        isTyping = false;
        typingIndicator.style.display = 'none';
    }

    // ===== SCROLL TO BOTTOM =====
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // ===== CLEAR CHAT =====
    function clearChat() {
        // Keep only welcome message
        const welcomeMessage = chatMessages.firstElementChild;
        chatMessages.innerHTML = '';
        chatMessages.appendChild(welcomeMessage);
    }

    // ===== EVENT LISTENERS =====
    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    clearChatBtn.addEventListener('click', clearChat);

    // Quick reply buttons
    document.querySelectorAll('.quick-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            userInput.value = this.getAttribute('data-message');
            sendMessage();
        });
    });

    // Auto-focus input on load
    userInput.focus();

    // ===== WELCOME ANIMATION =====
    setTimeout(() => {
        const welcomeMsg = document.querySelector('.bot-message');
        if (welcomeMsg) {
            welcomeMsg.style.animation = 'fadeInUp 0.6s ease';
        }
    }, 100);

    console.log('🤖 InternBot is ready!');
});
