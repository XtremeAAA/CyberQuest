import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("cyber_quest.db")
cursor = conn.cursor()

# Drop the existing tables if they exist (for debugging purposes)
cursor.execute("DROP TABLE IF EXISTS questions")

# Create a table for questions
cursor.execute(
    """
    CREATE TABLE "questions" (
	"id"	INTEGER,
	"category"	INTEGER NOT NULL,
	"question"	TEXT NOT NULL,
	"option1"	TEXT NOT NULL,
	"option2"	TEXT NOT NULL,
	"option3"	TEXT NOT NULL,
	"option4"	TEXT NOT NULL,
	"correct_option"	TEXT NOT NULL,
	"key_word"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
)

# Create a table for users
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
	"id"	INTEGER,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"correct_answers"	INTEGER DEFAULT 0,
	"incorrect_answers"	INTEGER DEFAULT 0,
	"total_score"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
)

# List of questions with multiple choice answers
questions = [
    # Category 1: Personal Information
    (
        1,
        "What is considered personal information?",
        "Your favorite color",
        "Your home address",
        "Your favorite TV show",
        "Your friend's pet name",
        "Your home address",
        "information",
    ),
    (
        1,
        "Should you share your passwords with your friends?",
        "Yes, they are trustworthy",
        "No, passwords should be kept secret",
        "Only if they ask nicely",
        "Only for games",
        "No, passwords should be kept secret",
        "passwords",
    ),
    (
        1,
        "Where is it safe to share your full name?",
        "On a public website",
        "In a chat with strangers",
        "On your private social media account",
        "Only with trusted adults and friends",
        "Only with trusted adults and friends",
        "name",
    ),
    (
        1,
        "Who should you tell if someone asks for your personal information online?",
        "No one, keep it a secret",
        "A trusted adult",
        "Your best friend",
        "Tell the person asking",
        "A trusted adult",
        "information",
    ),
    (
        1,
        "What should you do if a website asks for your phone number?",
        "Give it to them",
        "Ignore the request",
        "Ask a parent or guardian",
        "Share it with friends",
        "Ask a parent or guardian",
        "information",
    ),
    (
        1,
        "Is it okay to post your school name online?",
        "Yes, everyone does it",
        "No, it’s personal information",
        "Only if it’s a cool school",
        "Only on your birthday",
        "No, it’s personal information",
        "school",
    ),
    (
        1,
        "When creating a password, what should you do?",
        "Use easy-to-guess words",
        "Use a mix of letters, numbers, and symbols",
        "Share it with your friends",
        "Write it down everywhere",
        "Use a mix of letters, numbers, and symbols",
        "password",
    ),
    (
        1,
        "If someone you don’t know asks for your age online, you should:",
        "Tell them the truth",
        "Give a fake age",
        "Not respond and tell a trusted adult",
        "Ask them why they want to know",
        "Not respond and tell a trusted adult",
        "information",
    ),
    (
        1,
        "What information should you never share in a chat room?",
        "Your favorite hobby",
        "Your birthday",
        "Your phone number",
        "Both B and C",
        "Both B and C",
        "information",
    ),
    (
        1,
        "Why is it important to keep your personal information private?",
        "To make more friends",
        "To stay safe and protect your privacy",
        "To get free stuff online",
        "To be popular",
        "To stay safe and protect your privacy",
        "information",
    ),
    # Category 2: Stranger Danger
    (
        2,
        "What should you do if a stranger sends you a message online?",
        "Reply and make friends",
        "Ignore it and tell a trusted adult",
        "Ask them questions",
        "Share your personal information",
        "Ignore it and tell a trusted adult",
        "stranger",
    ),
    (
        2,
        "If someone you don’t know asks to meet you in person, you should:",
        "Agree and go alone",
        "Bring a friend and go",
        "Tell a trusted adult immediately",
        "Ignore them",
        "Tell a trusted adult immediately",
        "safety",
    ),
    (
        2,
        "Why should you be cautious about talking to strangers online?",
        "They might be boring",
        "They could be pretending to be someone they are not",
        "They might not like your favorite games",
        "They could be from a different country",
        "They could be pretending to be someone they are not",
        "safety",
    ),
    (
        2,
        "When is it safe to share your home address with someone online?",
        "Never",
        "Only if they ask politely",
        "If they say they are from your school",
        "If they promise to send you gifts",
        "Never",
        "safety",
    ),
    (
        2,
        "What should you do if someone online makes you feel uncomfortable?",
        "Keep talking to them",
        "Tell a trusted adult",
        "Block them and ignore it",
        "Share your feelings with them",
        "Tell a trusted adult",
        "safety",
    ),
    (
        2,
        "Who should you accept friend requests from?",
        "Everyone",
        "Only people you know in real life",
        "Strangers with many mutual friends",
        "Anyone who looks nice",
        "Only people you know in real life",
        "safety",
    ),
    (
        2,
        "What should you do if a stranger online knows your personal information?",
        "Tell a trusted adult",
        "Chat with them to find out more",
        "Ignore it",
        "Change your username",
        "Tell a trusted adult",
        "safety",
    ),
    (
        2,
        "Why shouldn't you trust online profiles at face value?",
        "They are always real",
        "They might not be who they say they are",
        "They are always accurate",
        "They don't matter",
        "They might not be who they say they are",
        "catfish",
    ),
    (
        2,
        "How should you handle an online stranger asking personal questions?",
        "Answer them politely",
        "Share only some information",
        "Don't respond and tell a trusted adult",
        "Ask them why they need to know",
        "Don't respond and tell a trusted adult",
        "safety",
    ),
    (
        2,
        "Who should you tell if a stranger keeps messaging you online?",
        "No one",
        "A trusted adult",
        "Your best friend",
        "The stranger",
        "A trusted adult",
        "safety",
    ),
    # Category 3: Cyberbullying
    (
        3,
        "What is cyberbullying?",
        "Sending nice messages",
        "Posting kind comments",
        "Being mean or hurtful online",
        "Ignoring someone online",
        "Being mean or hurtful online",
        "cyberbullying",
    ),
    (
        3,
        "If someone is being mean to you online, what should you do?",
        "Be mean back",
        "Ignore it",
        "Tell a trusted adult",
        "Share it with friends",
        "Tell a trusted adult",
        "cyberbullying",
    ),
    (
        3,
        "How can you help someone being cyberbullied?",
        "Join in",
        "Ignore it",
        "Support them and tell a trusted adult",
        "Laugh at them",
        "Support them and tell a trusted adult",
        "cyberbullying",
    ),
    (
        3,
        "Why is it important to report cyberbullying?",
        "To get revenge",
        "To keep others safe",
        "To be mean back",
        "To ignore it",
        "To keep others safe",
        "cyberbullying",
    ),
    (
        3,
        "Who should you talk to if you see cyberbullying?",
        "No one",
        "Your friends",
        "A trusted adult",
        "The bully",
        "A trusted adult",
        "cyberbullying",
    ),
    (
        3,
        "What should you do if you are being bullied online?",
        "Tell a trusted adult",
        "Keep it a secret",
        "Bully back",
        "Change your profile",
        "Tell a trusted adult",
        "cyberbullying",
    ),
    (
        3,
        "Why shouldn't you respond to cyberbullies?",
        "It might make things worse",
        "They will stop",
        "It's fun",
        "They might become friends",
        "It might make things worse",
        "cyberbullying",
    ),
    (
        3,
        "What's the first step if you are cyberbullied?",
        "Ignore it",
        "Keep chatting",
        "Report and block the bully",
        "Share personal info",
        "Report and block the bully",
        "cyberbullying",
    ),
    (
        3,
        "How can you prevent cyberbullying?",
        "Be kind online",
        "Bully others first",
        "Ignore everyone",
        "Post mean comments",
        "Be kind online",
        "cyberbullying",
    ),
    (
        3,
        "What is a good way to support a friend being cyberbullied?",
        "Ignore them",
        "Laugh with them",
        "Stand by them and report it",
        "Stay out of it",
        "Stand by them and report it",
        "cyberbullying",
    ),
    # Category 4: Safe Downloads and Websites
    (
        4,
        "What should you do before downloading a new app?",
        "Download it right away",
        "Ask a trusted adult",
        "Ignore the risks",
        "Download multiple times",
        "Ask a trusted adult",
        "safe downloads",
    ),
    (
        4,
        "Why is it important to use safe websites?",
        "To get free stuff",
        "To stay safe online",
        "To meet new people",
        "To have fun",
        "To stay safe online",
        "safe websites",
    ),
    (
        4,
        "How can you tell if a website is safe?",
        "It looks colorful",
        "It has HTTPS in the URL",
        "It has many ads",
        "It has cool games",
        "It has HTTPS in the URL",
        "safe websites",
    ),
    (
        4,
        "What should you avoid clicking on?",
        "Safe links",
        "Friends' posts",
        "Pop-ups and ads",
        "School websites",
        "Pop-ups and ads",
        "safe websites",
    ),
    (
        4,
        "Where can you find safe apps to download?",
        "On any website",
        "From the app store or trusted websites",
        "On a CD",
        "From your friends",
        "From the app store or trusted websites",
        "safe downloads",
    ),
    (
        4,
        "What should you do if a website asks for your email address?",
        "Give it right away",
        "Ignore the request",
        "Ask a trusted adult",
        "Share it with friends",
        "Ask a trusted adult",
        "safe websites",
    ),
    (
        4,
        "How can you protect your computer from viruses?",
        "Download lots of free stuff",
        "Use antivirus software",
        "Share your passwords",
        "Click on every link",
        "Use antivirus software",
        "safe downloads",
    ),
    (
        4,
        "Why should you update your apps and software?",
        "It makes them slower",
        "It adds new features and fixes security issues",
        "It's a waste of time",
        "It costs money",
        "It adds new features and fixes security issues",
        "safe downloads",
    ),
    (
        4,
        "What should you do if a website asks for your credit card number?",
        "Give it right away",
        "Ignore the request",
        "Ask a trusted adult",
        "Share it with friends",
        "Ask a trusted adult",
        "safe websites",
    ),
    (
        4,
        "What’s the safest way to shop online?",
        "Share your personal details",
        "Use secure payment methods",
        "Click on ads",
        "Save your payment details online",
        "Use secure payment methods",
        "safe shopping",
    ),
    (
        5,
        "How should you choose an online game to play?",
        "Any game you find",
        "Ask a trusted adult",
        "The most popular one",
        "Random selection",
        "Ask a trusted adult",
        "safe games",
    ),
    (
        5,
        "What should you use as your username?",
        "Your full name",
        "A nickname",
        "Your home address",
        "Your phone number",
        "A nickname",
        "safe usernames",
    ),
    (
        5,
        "Why should you be cautious about online games?",
        "They are boring",
        "They might have strangers trying to talk to you",
        "They are too easy",
        "They are expensive",
        "They might have strangers trying to talk to you",
        "safe games",
    ),
    (
        5,
        "When is it safe to meet someone from an online game?",
        "Anytime",
        "Never",
        "If they seem nice",
        "If they are your age",
        "Never",
        "safe games",
    ),
    (
        5,
        "How can you stay safe while playing online games?",
        "Share your personal info",
        "Use a nickname and keep personal info private",
        "Meet new people",
        "Chat with everyone",
        "Use a nickname and keep personal info private",
        "safe games",
    ),
    (
        5,
        "What should you do if someone in a game asks for your address?",
        "Tell them",
        "Ignore them",
        "Report and tell a trusted adult",
        "Ask why",
        "Report and tell a trusted adult",
        "safe games",
    ),
    (
        5,
        "Why is it important to play age-appropriate games?",
        "To meet older friends",
        "For safety and appropriate content",
        "To win more",
        "To get free stuff",
        "For safety and appropriate content",
        "safe games",
    ),
    (
        5,
        "Who should you play online games with?",
        "Anyone",
        "Strangers",
        "Only people you know and trust",
        "Everyone",
        "Only people you know and trust",
        "safe games",
    ),
    (
        5,
        "What should you do if you see bullying in an online game?",
        "Join in",
        "Ignore it",
        "Report it and tell a trusted adult",
        "Laugh at it",
        "Report it and tell a trusted adult",
        "safe games",
    ),
    (
        5,
        "How often should you update your game passwords?",
        "Never",
        "Every few months",
        "Only when asked",
        "Once a year",
        "Every few months",
        "safe games",
    ),
    (
        6,
        "Who should you accept friend requests from on social media?",
        "Everyone",
        "Only people you know in real life",
        "Strangers",
        "Popular accounts",
        "Only people you know in real life",
        "safe social media",
    ),
    (
        6,
        "What information should you share on social media?",
        "Everything",
        "Only safe and non-personal info",
        "Personal details",
        "Your location",
        "Only safe and non-personal info",
        "safe social media",
    ),
    (
        6,
        "How can you keep your social media profile safe?",
        "Keep it public",
        "Share everything",
        "Keep it private",
        "Post frequently",
        "Keep it private",
        "safe social media",
    ),
    (
        6,
        "Why is it important to have privacy settings?",
        "To show off",
        "To keep your information safe",
        "To get more followers",
        "To look cool",
        "To keep your information safe",
        "safe social media",
    ),
    (
        6,
        "What should you do if you see something upsetting on social media?",
        "Ignore it",
        "Share it with friends",
        "Report it and tell a trusted adult",
        "Comment on it",
        "Report it and tell a trusted adult",
        "safe social media",
    ),
    (
        6,
        "Why shouldn't you post your location online?",
        "It's fun",
        "It’s safe",
        "It can let strangers know where you are",
        "It's cool",
        "It can let strangers know where you are",
        "safe social media",
    ),
    (
        6,
        "What is a good practice for posting online?",
        "Share all personal details",
        "Only post appropriate content",
        "Post all the time",
        "Never post",
        "Only post appropriate content",
        "safe social media",
    ),
    (
        6,
        "How should you handle rude comments on your posts?",
        "Respond rudely",
        "Delete them",
        "Ignore them and tell a trusted adult",
        "Share them",
        "Ignore them and tell a trusted adult",
        "safe social media",
    ),
    (
        6,
        "Why is it important to be kind online?",
        "To get likes",
        "To make more friends",
        "To create a positive online environment",
        "To be popular",
        "To create a positive online environment",
        "safe social media",
    ),
    (
        6,
        "Who should you talk to about social media safety?",
        "No one",
        "Friends",
        "Trusted adults",
        "Strangers",
        "Trusted adults",
        "safe social media",
    ),
    (
        7,
        "What should you do if someone is mean to you online?",
        "Be mean back",
        "Ignore them",
        "Report and block them",
        "Share their message",
        "Report and block them",
        "safe social media",
    ),
    (
        7,
        "Why is reporting mean behavior online important?",
        "To get them in trouble",
        "To stay safe and keep others safe",
        "For fun",
        "To make friends",
        "To stay safe and keep others safe",
        "safe social media",
    ),
    (
        7,
        "How can you block someone online?",
        "Click on their profile",
        "Ask a friend",
        "Use the blocking feature",
        "Ignore them",
        "Use the blocking feature",
        "safe social media",
    ),
    (
        7,
        "What should you do if you see inappropriate content?",
        "Share it",
        "Report it and tell a trusted adult",
        "Ignore it",
        "Comment on it",
        "Report it and tell a trusted adult",
        "safe social media",
    ),
    (
        7,
        "Why might you need to report someone online?",
        "They are nice",
        "They post fun content",
        "They are being mean or inappropriate",
        "They are your friend",
        "They are being mean or inappropriate",
        "safe social media",
    ),
    (
        7,
        "Who can help you with reporting and blocking?",
        "Friends",
        "Strangers",
        "Trusted adults",
        "No one",
        "Trusted adults",
        "safe social media",
    ),
    (
        7,
        "How can reporting and blocking keep you safe?",
        "It can't",
        "It helps control who can contact you",
        "It's fun",
        "It's complicated",
        "It helps control who can contact you",
        "safe social media",
    ),
    (
        7,
        "When should you use the report feature?",
        "When you like someone's post",
        "When someone is being mean or inappropriate",
        "For fun",
        "When you see a friend online",
        "When someone is being mean or inappropriate",
        "safe social media",
    ),
    (
        7,
        "What is a sign that you should block someone?",
        "They are friendly",
        "They post interesting stuff",
        "They make you uncomfortable",
        "They share memes",
        "They make you uncomfortable",
        "safe social media",
    ),
    (
        7,
        "Who should you tell if you block or report someone?",
        "No one",
        "Friends",
        "Trusted adults",
        "The person you blocked",
        "Trusted adults",
        "safe social media",
    ),
    (
        8,
        "Why is it important to manage your online time?",
        "To stay online longer",
        "To have a balanced life",
        "To ignore other activities",
        "To play more games",
        "To have a balanced life",
        "safe social media",
    ),
    (
        8,
        "What should you do if you spend too much time online?",
        "Keep going",
        "Take breaks and do other activities",
        "Ignore it",
        "Stay online",
        "Take breaks and do other activities",
        "safe social media",
    ),
    (
        8,
        "How can you balance online and offline activities?",
        "Stay online all day",
        "Plan your day with different activities",
        "Only play games",
        "Skip school",
        "Plan your day with different activities",
        "safe social media",
    ),
    (
        8,
        "Why shouldn't you spend all your time online?",
        "It's healthy",
        "It can affect your sleep and other activities",
        "It's fun",
        "It's educational",
        "It can affect your sleep and other activities",
        "safe social media",
    ),
    (
        8,
        "What is a good practice for online time management?",
        "Use all free time online",
        "Set a daily time limit",
        "Skip meals",
        "Stay up late",
        "Set a daily time limit",
        "safe social media",
    ),
    (
        8,
        "Who can help you set limits for online time?",
        "Strangers",
        "Your parents or guardians",
        "Friends",
        "Online friends",
        "Your parents or guardians",
        "safe social media",
    ),
    (
        8,
        "What is a sign you need a break from the screen?",
        "You feel fine",
        "You feel tired or get headaches",
        "You win a game",
        "You find a new game",
        "You feel tired or get headaches",
        "safe social media",
    ),
    (
        8,
        "How can you make sure you have time for homework?",
        "Skip it",
        "Do it online",
        "Plan your time and limit online activities",
        "Ignore it",
        "Plan your time and limit online activities",
        "safe social media",
    ),
    (
        8,
        "Why is playing outside important?",
        "It's not",
        "For fresh air and exercise",
        "To avoid online games",
        "To make friends",
        "For fresh air and exercise",
        "safe social media",
    ),
    (
        8,
        "What should you do if your online time affects your sleep?",
        "Keep playing",
        "Go to bed earlier",
        "Skip sleep",
        "Ignore it",
        "Go to bed earlier",
        "safe social media",
    ),
]


# Insert the questions into the database
cursor.executemany(
    """
    INSERT INTO questions (category, question, option1, option2, option3, option4, correct_option, key_word)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    questions,
)

# Commit the changes and close the connection
conn.commit()
conn.close()
