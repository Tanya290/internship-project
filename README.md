# ˙⋆✮ Match Scheduler Web Application

A **Streamlit-based sports match scheduling system** that allows users to view past and future matches for selected players, along with player statistics. The application handles real-world data inconsistencies (like missing match times) and presents clean, user-friendly tables.

---

## ˙⋆✮ Features

* - Select any player and view their **past and future matches**
* - Clean separation of **past vs future matches** based on date
* - Intelligent handling of **match times**

  * Existing times are preserved
  * Missing times are auto-assigned realistic time slots
* - View **player statistics** in a structured table
* - Dark-themed UI with banners and styled headings
* - Fun sports facts for better user engagement

---

## ˙⋆✮ Tech Stack

* **Python**
* **Streamlit** – frontend & UI
* **Pandas** – data processing
* **NumPy** – randomization & utilities
* **Excel (.xlsx)** – data source

---

## ˙⋆✮ Project Structure

```
.
├── app.py
├── 1_Match_Scheduler.py
├── updated_players_1000.xlsx
├── player_stats_1000.xlsx
├── banner_3.jpg
├── banner_4.jpg
└── README.md
```

---

## ˙⋆✮ How the App Works

1. Match and player data are loaded from Excel files.
2. Match dates are normalized to ensure accurate comparison.
3. Match times are:

   * formatted to `HH:MM`
   * randomly assigned **only when missing**, using realistic time slots.
4. Matches are filtered into **past** and **future** using today’s date.
5. Clean display versions of data are shown in the UI.

---

## ˙⋆✮ How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/match-scheduler.git
   ```

2. Navigate to the project folder:

   ```bash
   cd match-scheduler
   ```

3. Install dependencies:

   ```bash
   pip install streamlit pandas numpy openpyxl
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## ˙⋆✮ Design Decisions

* **Datetime normalization** is used for correct filtering logic.
* **Display formatting** is handled separately to avoid logic bugs.
* Missing match times are filled using randomized time slots to maintain realism.
* Existing data is never overwritten.

---

## ˙⋆✮ Future Improvements

* Sport-specific time slots
* Admin panel to edit schedules
* Database integration instead of Excel
* Match reminders and notifications

---

## ˙⋆✮ Author

**Tanya Nair**
B.Tech CSE (AI & Data)
Lovely Professional University

---

˙⋆✮˙⋆✮ If you like this project, feel free to star the repository! ˙⋆✮˙⋆✮
