# E-Sa-Bum-Nim 🥋
### A Python-powered Taekwondo form reader and training companion

## Overview
E-Sa-Bum-Nim is a Python-based tool that reads out Taekwondo forms step-by-step, helping practitioners train independently, reinforce memory, and build confidence. It acts as a digital instructor—always ready to guide you through poomsae with clarity and consistency.

You can run the program in two ways:
* Provide a direct file path to any .txt form file
* Or let the program automatically detect forms inside the `forms/` directory

This makes it flexible for both structured training and quick, on-the-fly practice.

---

## Why I Built This
My name is **Yash Modak**, and I have been practicing martial arts for over **10 years**. I am a **3rd-degree black belt in Taekwondo** and a **sophomore at Evergreen Valley High School**.

This project began after a difficult moment in my martial arts journey. In **September 2023**, I appeared for my **2nd Dan test**. Unlike 1st Dan, where you earn your black belt, 2nd Dan marks the point where you begin assisting and teaching at your dojang—and the expectations rise sharply. I did not fully understand how high that bar was, and because I did not have all **15 forms** fully memorized, I made mistakes. When I learned I had not passed, I was devastated.

Instead of letting the setback define me, I decided to combine my two passions—technology and Taekwondo—to solve the exact problem that held me back. I used this tool to prepare for my retest one month later, and the difference was dramatic. I walked in confident, focused, and fully prepared. I passed with ease. Today, I use it regularly to run through my forms anytime, anywhere.

---

## Features
* 🔊 **Audio read-outs** of Taekwondo form steps
* 📁 **Two input modes** (Direct file path or `forms/` directory)
* 🧩 **Modular design** for adding new forms
* 🐍 **Simple Python interface** for running and customizing sessions
* 🎯 **Built for real training**, not just demonstration
* 💻 **Open-source and extensible** for future development

---

## Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/ymodak25/e-sa-bum-nim](https://github.com/ymodak25/e-sa-bum-nim)
cd e-sa-bum-nim

```

### 2. Run the program

```bash
python main.py

```

### Input Options

When the program starts, you will be prompted:
`Enter a file path, or press Enter to choose from the forms folder`

**Option A: Provide a file path**
Example: `/Users/yash/Desktop/taegeuk1.txt`

**Option B: Use the forms folder**
Place `.txt` files inside the `forms/` directory, then press Enter to select from the menu.

---

## Future Plans

* Add more forms and variations
* Introduce pacing and timing controls
* Explore pose-estimation integration for accuracy scoring
* Build a more polished user interface

---

## Contributing

Suggestions and contributions are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is released under the MIT License.
