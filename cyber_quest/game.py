import tkinter as tk
from tkinter import messagebox, PhotoImage
import sqlite3
import random
import os
from tkinter import scrolledtext
import pygame


class CyberQuest(tk.Tk):
    """
    The main application window for CyberQuest.

    Attributes:
        logged_in_user (str): The username of the currently logged-in user.
        conn (sqlite3.Connection): The connection to the SQLite database.
        cursor (sqlite3.Cursor): The cursor for the SQLite database.
        images (dict): A dictionary containing all image objects used in the application.

    """
    
    def __init__(root, logged_in_user):
        """
        Initialises the CyberQuest application.

        Args:
            logged_in_user (str): The username of the currently logged-in user.

        """
        super().__init__()
        root.title("Cyber Quest")
        root.geometry("1200x800")
        root.config(bg="#2B2D42")
        root.logged_in_user = logged_in_user
        root.conn = sqlite3.connect("cyber_quest.db")
        root.cursor = root.conn.cursor()
        root.images = {}
        root.create_welcome_screen()
        root.play_audio()

    def play_audio(self):
        """
        Plays background music using Pygame.

        """
        # Defines the audio to be played
        pygame.mixer.init()
        pygame.mixer.music.load(
            "cyber_quest/audio/Background Music [chill lofi hip hop beats].mp3"
        )
        pygame.mixer.music.play(-1)

    def set_volume(self, val):
        """
        Sets the volume of the background music.

        Args:
            val (int): The volume level as an integer between 0 and 100.

        """
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)

    def create_welcome_screen(root):
        """
        Creates the welcome screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.welcome_to_banner = PhotoImage(file=r"cyber_quest/Icons/Welcome-to.png")
        root.label_welcome = tk.Label(
            root, image=root.welcome_to_banner, fg="#2B2D42", bg="#2B2D42"
        )
        root.label_welcome.place(x=467, y=0)

        root.cyber_quest_banner = PhotoImage(file=r"cyber_quest/Icons/Cyber Quest.png")
        root.label_cyber_quest = tk.Label(
            root, image=root.cyber_quest_banner, fg="#2B2D42", bg="#2B2D42"
        )
        root.label_cyber_quest.place(x=424, y=70)

        root.play_button_image = PhotoImage(file=r"cyber_quest/Icons/button_play.png")
        root.button_play_button = tk.Button(
            root,
            image=root.play_button_image,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.topic_selection,
        )
        root.button_play_button.place(x=529, y=367)

        root.settings_icon_image = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        root.label_settings = tk.Label(
            root, image=root.settings_icon_image, bg="#2B2D42"
        )
        root.label_settings.place(x=1197, y=720)

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        # Add stats button
        root.stats_button_image = PhotoImage(
            file=r"cyber_quest/Icons/button_statistics.png"
        )
        root.button_stats_button = tk.Button(
            root,
            image=root.stats_button_image,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_stats_screen,
        )
        root.button_stats_button.place(x=502, y=450)


    def create_search_screen(root):
        """
        Creates the search screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["search_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_search.png"
        )
        tk.Label(
            root, image=root.images["search_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=464, y=85)

        # Search bar
        root.search_entry = tk.Entry(root, width=50, font=("Tahoma", 15))
        root.search_entry.place(x=250, y=250)

        # Search button
        root.search_button = tk.Button(
            root, text="Search", command=root.search_question, font=("Tahoma", 15)
        )
        root.search_button.place(x=950, y=250)

        # Result label
        root.result_label = tk.Label(
            root, text="", font=("Tahoma", 18), bg="#2B2D42", fg="#ffffff"
        )
        # root.result_label.place(x=250, y=350)
        global text_area
        text_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 100, height = 20, font=("Tahoma", 12))
        text_area.place(x=250, y=320)
        
        root.search_def_text = tk.Label(root, text="Search Key Word:", font=("Tahoma, 15"), bg="#2B2D42")
        root.search_def_text.place(x=250, y = 220)
        
        root.search_result_text = tk.Label(root, text="Search Results:", font=("Tahoma, 15"), bg="#2B2D42")
        root.search_result_text.place(x=250, y = 290)


    def search_question(root):
        """
        Searches for questions based on the user's input and displays the results.

        """
        keyword = root.search_entry.get()
        root.cursor.execute(
            "SELECT question FROM questions WHERE key_word LIKE ?", ('%' + keyword + '%',)
        )
        results = root.cursor.fetchall()

        if results:
            question_text = "\n".join(result[0] for result in results)
            text_area.insert(tk.INSERT, question_text)
            root.result_label.config(text=question_text)
        else:
            root.result_label.config(text="No matching question found.")

    def create_stats_screen(root):
        """
        Creates the stats screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["stats_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_statistics.png"
        )
        tk.Label(
            root, image=root.images["stats_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=502, y=85)

        # Create the stats table
        root.stats_table = tk.Frame(root, bg="#2B2D42")
        root.stats_table.place(x=100, y=200)

        root.stats_table_headers = ["Username", "Correct Answers", "Total Score"]
        for i, header in enumerate(root.stats_table_headers):
            tk.Label(
                root.stats_table,
                text=header,
                font=("Tahoma", 15),
                bg="#2B2D42",
                fg="#ffffff",
            ).grid(row=0, column=i, padx=10, pady=5)

        # Initialie with sorted by username
        root.display_stats("username")

        # Sort buttons
        root.button_sort_by_correct_answer = PhotoImage(
            file=r"cyber_quest/Icons/button_sort-by-correct-answers.png"
        )
        root.sort_by_correct_button = tk.Button(
            root,
            image=root.button_sort_by_correct_answer,
            command=lambda: root.display_stats("correct_answers"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.sort_by_correct_button.place(x=700, y=400)

        root.button_sort_by_total_score_button = PhotoImage(
            file=r"cyber_quest/Icons/button_sort-by-total-score.png"
        )
        root.sort_by_total_score_button = tk.Button(
            root,
            image=root.button_sort_by_total_score_button,
            command=lambda: root.display_stats("total_score"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.sort_by_total_score_button.place(x=700, y=600)

    def display_stats(root, sort_by):
        """
        Displays the user statistics on the stats screen.

        Args:
            sort_by (str): The column to sort the statistics by ('username', 'correct_answers', or 'total_score').

        """
        # Clear existing stats table
        for child in root.stats_table.winfo_children():
            child.destroy()

        # Create headers again
        root.stats_table_headers = ["Username", "Correct Answers", "Total Score"]
        for i, header in enumerate(root.stats_table_headers):
            tk.Label(
                root.stats_table,
                text=header,
                font=("Tahoma", 15),
                bg="#2B2D42",
                fg="#ffffff",
            ).grid(row=0, column=i, padx=10, pady=5)

        # Fetch and display stats data
        if sort_by == "correct_answers":
            root.cursor.execute(
                "SELECT username, correct_answers, total_score FROM users ORDER BY correct_answers DESC"
            )
        elif sort_by == "total_score":
            root.cursor.execute(
                "SELECT username, correct_answers, total_score FROM users ORDER BY total_score DESC"
            )
        else:
            root.cursor.execute(
                "SELECT username, correct_answers, total_score FROM users ORDER BY username ASC"
            )
        stats_data = root.cursor.fetchall()

        # Display stats data
        for row_num, row in enumerate(stats_data, start=1):
            for col_num, value in enumerate(row):
                tk.Label(
                    root.stats_table,
                    text=value,
                    font=("Tahoma", 12),
                    bg="#2B2D42",
                    fg="#ffffff",
                ).grid(row=row_num, column=col_num, padx=10, pady=5)

    def topic_selection(root):
        """
        Creates the topic selection screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.cyber_quest_banner = PhotoImage(file=r"cyber_quest/Icons/Cyber Quest.png")
        root.label_cyber_quest = tk.Label(
            root, image=root.cyber_quest_banner, fg="#2B2D42", bg="#2B2D42"
        )
        root.label_cyber_quest.place(x=424, y=0)

        root.topic_selection_banner = PhotoImage(
            file=r"cyber_quest/Icons/topic-selection.png"
        )
        root.label_topic_selection = tk.Label(
            root, image=root.topic_selection_banner, fg="#2B2D42", bg="#2B2D42"
        )
        root.label_topic_selection.place(x=464, y=85)

        root.label_settings = tk.Label(
            root, image=root.settings_icon_image, bg="#2B2D42"
        )
        root.label_settings.place(x=1197, y=720)

        topics = [
            (
                r"cyber_quest/Icons/button_personal-information.png",
                root.create_topic1_screen,
                54,
                294,
            ),
            (
                r"cyber_quest/Icons/button_stranger-danger.png",
                root.create_topic2_screen,
                335,
                293,
            ),
            (
                r"cyber_quest/Icons/button_cyberbullying.png",
                root.create_topic3_screen,
                616,
                293,
            ),
            (
                r"cyber_quest/Icons/button_safe-browsing.png",
                root.create_topic4_screen,
                897,
                293,
            ),
            (
                r"cyber_quest/Icons/button_online-games.png",
                root.create_topic5_screen,
                54,
                358,
            ),
            (
                r"cyber_quest/Icons/button_social-media.png",
                root.create_topic6_screen,
                335,
                358,
            ),
            (
                r"cyber_quest/Icons/button_reporting-blocking.png",
                root.create_topic7_screen,
                616,
                358,
            ),
            (
                r"cyber_quest/Icons/button_time-management.png",
                root.create_topic8_screen,
                896,
                358,
            ),
        ]
        root.search_button_image = PhotoImage(file=r"cyber_quest/Icons/button_search.png")
        root.button_search_button = tk.Button(
            root,
            image=root.search_button_image,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_search_screen,
        )
        root.button_search_button.place(x=513, y=441)  # Position the search button

        for image_path, command, x, y in topics:
            button_image = PhotoImage(file=image_path)
            button = tk.Button(
                root, image=button_image, fg="#2B2D42", bg="#2B2D42", command=command
            )
            button.image = button_image
            button.place(x=x, y=y)


    def create_topic1_screen(root):
        """
        Creates the topic 1 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic1_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-personal-information.png"
        )
        tk.Label(
            root, image=root.images["topic1_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=408, y=85)

        root.t1_score = 0
        root.t1_incorrect_answer = 0
        root.t1_correct_answer = 0
        root.t1_score_label = tk.Label(
            root, text="Score: " + str(root.t1_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t1_score_label.place(x=800, y=200)

        root.t1_number_of_questions = random.randint(3, 10)
        root.t1_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 1"
        )
        db_questions = root.cursor.fetchall()
        root.t1_questions = db_questions

        random.shuffle(root.t1_questions)
        root.t1_used_questions = random.sample(
            root.t1_questions, root.t1_number_of_questions
        )

        root.t1_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t1_used_questions[root.t1_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t1_used_questions[root.t1_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t1_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t1_validate_selection(root):
        """
        Validates the user's selection on the topic 1 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t1_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 1 screen.

        """
        if not root.t1_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t1_used_questions[root.t1_current_question][0],),
        )
        t1_correct_answer = c.fetchone()[0]

        t1_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t1_selected_answer = root.t1_used_questions[root.t1_current_question][
                    i + 1
                ]

        if t1_selected_answer == t1_correct_answer:
            root.t1_score += 1
            root.t1_score_label.config(text="Score: " + str(root.t1_score))
        else:
            root.t1_incorrect_answer += 1

        root.t1_current_question += 1
        if root.t1_current_question < root.t1_number_of_questions:
            root.question_label.config(
                text=root.t1_used_questions[root.t1_current_question][0]
            )
            for i, option in enumerate(
                root.t1_used_questions[root.t1_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t1_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t1_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the personal information quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic2_screen(root):
        """
        Creates the topic 2 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic2_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-stranger-danger.png"
        )
        tk.Label(
            root, image=root.images["topic2_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=425, y=85)

        root.t2_score = 0
        root.t2_incorrect_answer = 0
        root.t2_correct_answer = 0
        root.t2_score_label = tk.Label(
            root, text="Score: " + str(root.t2_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t2_score_label.place(x=800, y=200)

        root.t2_number_of_questions = random.randint(3, 10)
        root.t2_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 2"
        )
        db_questions = root.cursor.fetchall()
        root.t2_questions = db_questions

        random.shuffle(root.t2_questions)
        root.t2_used_questions = random.sample(
            root.t2_questions, root.t2_number_of_questions
        )

        root.t2_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t2_used_questions[root.t2_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t2_used_questions[root.t2_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t2_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t2_validate_selection(root):
        """
        Validates the user's selection on the topic 2 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t2_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 2 screen.

        """
        if not root.t2_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t2_used_questions[root.t2_current_question][0],),
        )
        t2_correct_answer = c.fetchone()[0]

        t2_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t2_selected_answer = root.t2_used_questions[root.t2_current_question][
                    i + 1
                ]

        if t2_selected_answer == t2_correct_answer:
            root.t2_score += 1
            root.t2_score_label.config(text="Score: " + str(root.t2_score))
        else:
            root.t2_incorrect_answer += 1

        root.t2_current_question += 1
        if root.t2_current_question < root.t2_number_of_questions:
            root.question_label.config(
                text=root.t2_used_questions[root.t2_current_question][0]
            )
            for i, option in enumerate(
                root.t2_used_questions[root.t2_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t2_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t2_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the stranger dange quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic3_screen(root):
        """
        Creates the topic 3 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic3_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-cyber-bullying.png"
        )
        tk.Label(
            root, image=root.images["topic3_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=442, y=85)

        root.t3_score = 0
        root.t3_incorrect_answer = 0
        root.t3_correct_answer = 0
        root.t3_score_label = tk.Label(
            root, text="Score: " + str(root.t3_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t3_score_label.place(x=800, y=200)

        root.t3_number_of_questions = random.randint(3, 10)
        root.t3_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 3"
        )
        db_questions = root.cursor.fetchall()
        root.t3_questions = db_questions

        random.shuffle(root.t3_questions)
        root.t3_used_questions = random.sample(
            root.t3_questions, root.t3_number_of_questions
        )

        root.t3_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t3_used_questions[root.t3_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t3_used_questions[root.t3_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t3_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t3_validate_selection(root):
        """
        Validates the user's selection on the topic 3 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t3_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 3 screen.

        """
        if not root.t3_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t3_used_questions[root.t3_current_question][0],),
        )
        t3_correct_answer = c.fetchone()[0]

        t3_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t3_selected_answer = root.t3_used_questions[root.t3_current_question][
                    i + 1
                ]

        if t3_selected_answer == t3_correct_answer:
            root.t3_score += 1
            root.t3_score_label.config(text="Score: " + str(root.t3_score))
        else:
            root.t3_incorrect_answer += 1

        root.t3_current_question += 1
        if root.t3_current_question < root.t3_number_of_questions:
            root.question_label.config(
                text=root.t3_used_questions[root.t3_current_question][0]
            )
            for i, option in enumerate(
                root.t3_used_questions[root.t3_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t3_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t3_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the cyberbullying quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic4_screen(root):
        """
        Creates the topic 4 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic4_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-safe-browsing.png"
        )
        tk.Label(
            root, image=root.images["topic4_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=437, y=85)

        root.t4_score = 0
        root.t4_incorrect_answer = 0
        root.t4_correct_answer = 0
        root.t4_score_label = tk.Label(
            root, text="Score: " + str(root.t4_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t4_score_label.place(x=800, y=200)

        root.t4_number_of_questions = random.randint(3, 10)
        root.t4_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 4"
        )
        db_questions = root.cursor.fetchall()
        root.t4_questions = db_questions

        random.shuffle(root.t4_questions)
        root.t4_used_questions = random.sample(
            root.t4_questions, root.t4_number_of_questions
        )

        root.t4_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t4_used_questions[root.t4_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t4_used_questions[root.t4_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t4_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t4_validate_selection(root):
        """
        Validates the user's selection on the topic 4 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t4_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 4 screen.

        """
        if not root.t4_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t4_used_questions[root.t4_current_question][0],),
        )
        t4_correct_answer = c.fetchone()[0]

        t4_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t4_selected_answer = root.t4_used_questions[root.t4_current_question][
                    i + 1
                ]

        if t4_selected_answer == t4_correct_answer:
            root.t4_score += 1
            root.t4_score_label.config(text="Score: " + str(root.t4_score))
        else:
            root.t4_incorrect_answer += 1

        root.t4_current_question += 1
        if root.t4_current_question < root.t4_number_of_questions:
            root.question_label.config(
                text=root.t4_used_questions[root.t4_current_question][0]
            )
            for i, option in enumerate(
                root.t4_used_questions[root.t4_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t4_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t4_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the safe browsing quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic5_screen(root):
        """
        Creates the topic 5 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic5_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-online-games.png"
        )
        tk.Label(
            root, image=root.images["topic5_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=442, y=85)

        root.t5_score = 0
        root.t5_incorrect_answer = 0
        root.t5_correct_answer = 0
        root.t5_score_label = tk.Label(
            root, text="Score: " + str(root.t5_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t5_score_label.place(x=800, y=200)

        root.t5_number_of_questions = random.randint(3, 10)
        root.t5_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category =5"
        )
        db_questions = root.cursor.fetchall()
        root.t5_questions = db_questions

        random.shuffle(root.t5_questions)
        root.t5_used_questions = random.sample(
            root.t5_questions, root.t5_number_of_questions
        )

        root.t5_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t5_used_questions[root.t5_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t5_used_questions[root.t5_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t5_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t5_validate_selection(root):
        """
        Validates the user's selection on the topic 5 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t5_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 5 screen.

        """
        if not root.t5_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t5_used_questions[root.t5_current_question][0],),
        )
        t5_correct_answer = c.fetchone()[0]

        t5_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t5_selected_answer = root.t5_used_questions[root.t5_current_question][
                    i + 1
                ]

        if t5_selected_answer == t5_correct_answer:
            root.t5_score += 1
            root.t5_score_label.config(text="Score: " + str(root.t5_score))
        else:
            root.t5_incorrect_answer += 1

        root.t5_current_question += 1
        if root.t5_current_question < root.t5_number_of_questions:
            root.question_label.config(
                text=root.t5_used_questions[root.t5_current_question][0]
            )
            for i, option in enumerate(
                root.t5_used_questions[root.t5_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t5_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t5_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the online games quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic6_screen(root):
        """
        Creates the topic 6 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic6_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-social-media.png"
        )
        tk.Label(
            root, image=root.images["topic6_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=447, y=85)

        root.t6_score = 0
        root.t6_incorrect_answer = 0
        root.t6_correct_answer = 0
        root.t6_score_label = tk.Label(
            root, text="Score: " + str(root.t6_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t6_score_label.place(x=800, y=200)

        root.t6_number_of_questions = random.randint(3, 10)
        root.t6_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 6"
        )
        db_questions = root.cursor.fetchall()
        root.t6_questions = db_questions

        random.shuffle(root.t6_questions)
        root.t6_used_questions = random.sample(
            root.t6_questions, root.t6_number_of_questions
        )

        root.t6_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t6_used_questions[root.t6_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t6_used_questions[root.t6_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t6_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t6_validate_selection(root):
        """
        Validates the user's selection on the topic 6 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t6_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 6 screen.

        """
        if not root.t6_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t6_used_questions[root.t6_current_question][0],),
        )
        t6_correct_answer = c.fetchone()[0]

        t6_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t6_selected_answer = root.t6_used_questions[root.t6_current_question][
                    i + 1
                ]

        if t6_selected_answer == t6_correct_answer:
            root.t6_score += 1
            root.t6_score_label.config(text="Score: " + str(root.t6_score))
        else:
            root.t6_incorrect_answer += 1

        root.t6_current_question += 1
        if root.t6_current_question < root.t6_number_of_questions:
            root.question_label.config(
                text=root.t6_used_questions[root.t6_current_question][0]
            )
            for i, option in enumerate(
                root.t6_used_questions[root.t6_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t6_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t6_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the social media quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic7_screen(root):
        """
        Creates the topic 7 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic7_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/button_topic-report-blocking.png"
        )
        tk.Label(
            root, image=root.images["topic7_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=421, y=85)

        root.t7_score = 0
        root.t7_incorrect_answer = 0
        root.t7_correct_answer = 0
        root.t7_score_label = tk.Label(
            root, text="Score: " + str(root.t7_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t7_score_label.place(x=800, y=200)

        root.t7_number_of_questions = random.randint(3, 10)
        root.t7_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 7"
        )
        db_questions = root.cursor.fetchall()
        root.t7_questions = db_questions

        random.shuffle(root.t7_questions)
        root.t7_used_questions = random.sample(
            root.t7_questions, root.t7_number_of_questions
        )

        root.t7_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t7_used_questions[root.t7_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t7_used_questions[root.t7_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t7_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t7_validate_selection(root):
        """
        Validates the user's selection on the topic 7 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t7_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 7 screen.

        """
        if not root.t7_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t7_used_questions[root.t7_current_question][0],),
        )
        t7_correct_answer = c.fetchone()[0]

        t7_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t7_selected_answer = root.t7_used_questions[root.t7_current_question][
                    i + 1
                ]

        if t7_selected_answer == t7_correct_answer:
            root.t7_score += 1
            root.t7_score_label.config(text="Score: " + str(root.t7_score))
        else:
            root.t7_incorrect_answer += 1

        root.t7_current_question += 1
        if root.t7_current_question < root.t7_number_of_questions:
            root.question_label.config(
                text=root.t7_used_questions[root.t7_current_question][0]
            )
            for i, option in enumerate(
                root.t7_used_questions[root.t7_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t7_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t7_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the report and blocking quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()

    def create_topic8_screen(root):
        """
        Creates the topic 8 screen for the application.

        """
        for child in root.winfo_children():
            child.destroy()

        # Add volume control slider
        root.volume_lbl1 = tk.Label(
            root,
            text="Volume: (Click on the grey",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl1.place(x=990, y=657)
        root.volume_lbl2 = tk.Label(
            root,
            text="box to reveal)",
            font=("Tahoma, 15"),
            bg="#2B2D42",
            fg="#ffffff",
        )
        root.volume_lbl2.place(x=1028, y=685)
        root.volume_slider = tk.Scale(
            root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="",  # Set label text
            fg="#FFFFFF",  # Set label text color
            bg="#2B2D42",  # Set label background color
            command=root.set_volume,
            length=200,
            font=("Tahoma", 20),
        )
        root.volume_slider.set(50)  # Set default volume to 50%
        root.volume_slider.place(x=965, y=710)

        root.button_home_button = PhotoImage(file=r"cyber_quest/Icons/button_home.png")
        root.label_home_button = tk.Button(
            root,
            image=root.button_home_button,
            fg="#2B2D42",
            bg="#2B2D42",
            command=root.create_welcome_screen,
        )
        root.label_home_button.place(x=36, y=698)

        root.images["settings_icon"] = PhotoImage(file=r"cyber_quest/Icons/cog.png")
        tk.Label(root, image=root.images["settings_icon"], bg="#2B2D42").place(
            x=1197, y=720
        )

        root.images["cyber_quest_banner"] = PhotoImage(
            file=r"cyber_quest/Icons/Cyber Quest.png"
        )
        tk.Label(
            root, image=root.images["cyber_quest_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=424, y=0)

        root.images["topic8_banner"] = PhotoImage(
            file=r"/Users/achintsingh/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Year 12/SDD/SDD code/cyber_quest/Icons/button_topic-time-management.png"
        )
        tk.Label(
            root, image=root.images["topic8_banner"], fg="#2B2D42", bg="#2B2D42"
        ).place(x=419, y=85)

        root.t8_score = 0
        root.t8_incorrect_answer = 0
        root.t8_correct_answer = 0
        root.t8_score_label = tk.Label(
            root, text="Score: " + str(root.t8_score), font=("Tahoma", 20), bg="#2B2D42"
        )
        root.t8_score_label.place(x=800, y=200)

        root.t8_number_of_questions = random.randint(3, 10)
        root.t8_used_questions = ""

        root.cursor.execute(
            "SELECT question, option1, option2, option3, option4 FROM questions WHERE category = 8"
        )
        db_questions = root.cursor.fetchall()
        root.t8_questions = db_questions

        random.shuffle(root.t8_questions)
        root.t8_used_questions = random.sample(
            root.t8_questions, root.t8_number_of_questions
        )

        root.t8_current_question = 0

        root.question_label = tk.Label(
            root,
            text=root.t8_used_questions[root.t8_current_question][0],
            font=("System", 20),
            bg="#2B2D42",
            wraplength=800,
            anchor="w",
            justify="left",
        )
        root.question_label.pack(anchor="w", pady=(200, 20), padx=100)

        root.option_vars = [tk.StringVar(value="") for _ in range(4)]
        root.option_buttons = []
        for i, option in enumerate(
            root.t8_used_questions[root.t8_current_question][1:]
        ):
            button = tk.Radiobutton(
                root,
                text=option,
                variable=root.option_vars[i],
                value=option,
                font=("System", 15),
                bg="#2B2D42",
            )
            button.pack(anchor="w", padx=100)
            root.option_buttons.append(button)

        root.next_button = tk.Button(
            root,
            text="Next",
            command=root.t8_next_question,
            font=("System", 15),
            bg="#2B2D42",
        )
        root.next_button.pack(anchor="w", padx=100, pady=20)

    def t8_validate_selection(root):
        """
        Validates the user's selection on the topic 8 screen.

        Returns:
            bool: True if a valid selection is made, False otherwise.

        """
        return any(var.get() for var in root.option_vars)

    def t8_next_question(root):
        """
        Processes the user's selection and moves to the next question on the topic 8 screen.

        """
        if not root.t8_validate_selection():
            messagebox.showerror("Error", "Please select an option")
            return

        c = root.conn.cursor()
        c.execute(
            "SELECT correct_option FROM questions WHERE question = ?",
            (root.t8_used_questions[root.t8_current_question][0],),
        )
        t8_correct_answer = c.fetchone()[0]

        t8_selected_answer = None
        for i, var in enumerate(root.option_vars):
            if var.get() != "":
                t8_selected_answer = root.t8_used_questions[root.t8_current_question][
                    i + 1
                ]

        if t8_selected_answer == t8_correct_answer:
            root.t8_score += 1
            root.t8_score_label.config(text="Score: " + str(root.t8_score))
        else:
            root.t8_incorrect_answer += 1

        root.t8_current_question += 1
        if root.t8_current_question < root.t8_number_of_questions:
            root.question_label.config(
                text=root.t8_used_questions[root.t8_current_question][0]
            )
            for i, option in enumerate(
                root.t8_used_questions[root.t8_current_question][1:]
            ):
                root.option_buttons[i].config(text=option)
                root.option_vars[i].set("")  # Reset the radio button selection
        else:
            # Update incorrect answers in the database
            root.cursor.execute(
                "UPDATE users SET incorrect_answers = incorrect_answers + ? WHERE username = ?",
                (root.t8_incorrect_answer, root.logged_in_user),
            )
            root.conn.commit()

            # Update correct answers in the database
            root.cursor.execute(
                "UPDATE users SET correct_answers = correct_answers + ? WHERE username = ?",
                (root.t8_score, root.logged_in_user),
            )
            root.conn.commit()

            # Update total score in databse
            root.cursor.execute(
                "SELECT correct_answers, incorrect_answers FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            result = root.cursor.fetchone()
            if result:
                correct_answers = result[0]
                incorrect_answers = result[1]
                total_score = correct_answers - incorrect_answers

                # Update total score in the database
                root.cursor.execute(
                    "UPDATE users SET total_score = ? WHERE username = ?",
                    (total_score, root.logged_in_user),
                )
                root.conn.commit()

            # Display total score
            c.execute(
                "SELECT total_score FROM users WHERE username = ?",
                (root.logged_in_user,),
            )
            total_score_db = c.fetchone()[0]
            Quiz_complete_text = f"Congratulations, you have completed the time management quiz! You now have a total score of {total_score_db}."

            messagebox.showinfo("CyberQuest", Quiz_complete_text)
            root.create_welcome_screen()


# Read the logged-in username from the temporary file
if os.path.exists("logged_in_user.txt"):
    with open("logged_in_user.txt", "r") as file:
        logged_in_user = file.read().strip()
    os.remove("logged_in_user.txt")  # Remove the file after reading
else:
    logged_in_user = None  # Handle the case where the file does not exist

# Start the quiz application
if logged_in_user:
    app = CyberQuest(logged_in_user)
    app.mainloop()
else:
    tk.messagebox.showerror("Error", "No user is logged in.")
