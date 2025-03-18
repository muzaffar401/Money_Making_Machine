# 💰 Money Making Machine

## 🚀 About the Project
The **Money Making Machine** is a fun and interactive web application built using **Streamlit**. This app provides a virtual way to generate random money, get side hustle ideas, and receive motivational quotes related to money-making. It is designed to be an engaging and lighthearted experience while giving users useful ideas and inspiration.

## 🏗️ How It Works
This application consists of three main features:
1. **Instant Cash Generator** 🎰
   - Click a button to generate a random amount of money between **$1 and $1000**.
   - A **loading spinner** appears for **5 seconds** before revealing the amount.

2. **Side Hustle Ideas** 💼
   - Click a button to receive a random **side hustle idea**.
   - The idea is fetched from an **API endpoint**.
   - If the API fails, a default idea ("Freelancing") is displayed.

3. **Money-Making Motivation** 🔥
   - Click a button to receive a **money-related motivational quote**.
   - The quote is fetched from an **API endpoint**.
   - If the API fails, a default quote is shown.

## 🔧 Modules Used
The project relies on the following Python modules:

| Module    | Purpose |
|-----------|---------|
| `streamlit` | Used to create the web application and UI elements |
| `random` | Generates a random amount of money |
| `time` | Adds delay to simulate money counting effect |
| `requests` | Fetches side hustle ideas and money quotes from an API |

## 📜 Installation Guide
Follow these steps to run the project on your local machine:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/muzaffar401/Money_Making_Machine.git
   cd Money_Making_Machine
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```sh
   streamlit run app.py
   ```

## 🔗 API Endpoints Used
The project fetches data from external APIs:
- **Side Hustle Ideas API:** `https://fast-api-two-plum.vercel.app/side_hustles`
- **Money Quotes API:** `https://fast-api-two-plum.vercel.app/money_quotes`

## 🎯 Features Overview
- 🎰 **Generate random money amounts**
- 💼 **Get side hustle ideas from an API**
- 🔥 **Receive motivational money-related quotes**
- 🎨 **User-friendly and engaging UI with emojis**
- 🚀 **API error handling with fallback values**

## 📜 License
This project is licensed under the MIT License.

## 📞 Contact
For any issues or suggestions, feel free to reach out:
- **GitHub:** (https://github.com/muzaffar401)
- **Email:** ma9400667@gmail.com

---
### 🌟 Keep hustling, and you'll be a millionaire in no time! 🌟

