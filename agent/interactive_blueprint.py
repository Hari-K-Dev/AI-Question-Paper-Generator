# agent/interactive_blueprint.py

def build_blueprint(chapter_summary, detected_types):
    print("📘 Detected question types from your CSV:")
    print(", ".join(detected_types))

    question_types = list(detected_types)
    marks_per_type = {}

    # Ask if user wants to add custom types
    choice = input("❓ Do you want to add or modify question types? (y/n): ").strip().lower()
    if choice == 'y':
        question_types = []
        while True:
            qtype = input("🔤 Enter a question type (or press Enter to finish): ").strip()
            if not qtype:
                break
            marks = input(f"🔢 Marks for '{qtype}' questions: ").strip()
            try:
                marks = int(marks)
            except:
                print("❗ Invalid marks. Skipping this type.")
                continue
            question_types.append(qtype)
            marks_per_type[qtype] = marks
    else:
        # Ask marks per each detected type
        for qtype in question_types:
            marks = input(f"🔢 Marks for '{qtype}' questions: ").strip()
            try:
                marks_per_type[qtype] = int(marks)
            except:
                print("❗ Invalid input. Defaulting to 1 mark.")
                marks_per_type[qtype] = 1

    # Ask how many of each type per chapter
    blueprint = {}
    print("\n📗 Let's build the paper blueprint...")

    for chapter, counts in chapter_summary.items():
        print(f"\n➡️ Chapter: {chapter}")
        blueprint[chapter] = {}
        for qtype in question_types:
            max_available = counts.get(qtype, 0)
            default = min(1, max_available)
            inp = input(f"  ➕ How many '{qtype}' questions? (Available: {max_available}) [default={default}]: ").strip()
            if inp == "":
                count = default
            else:
                try:
                    count = int(inp)
                except:
                    print("  ❗ Invalid input, defaulting to 0")
                    count = 0
            if count > 0:
                blueprint[chapter][qtype] = count

    # Collect user notes
    print("\n📝 Any special notes or constraints? (e.g., no repeated concepts, focus on HOTS, etc.)")
    notes = input("👉 Notes (press Enter to skip): ").strip()

    print("\n✅ Blueprint collection complete.\n")
    return {
        "question_types": question_types,
        "marks_per_type": marks_per_type,
        "chapters": blueprint
    }, notes
