"""
============================================================
  FORWARD CHAINING IN AI — PRESENTATION DEMO
  Author : <Your Name>
  Subject: Artificial Intelligence
  Purpose: Demonstrate Forward Chaining inference step-by-step
============================================================
"""

import os
import sys
import time

# ---------- Optional color support (works even without colorama) ----------
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    C = {
        "title": Fore.CYAN + Style.BRIGHT,
        "ok":    Fore.GREEN + Style.BRIGHT,
        "warn":  Fore.YELLOW + Style.BRIGHT,
        "err":   Fore.RED + Style.BRIGHT,
        "info":  Fore.BLUE + Style.BRIGHT,
        "mag":   Fore.MAGENTA + Style.BRIGHT,
        "dim":   Style.DIM,
        "rst":   Style.RESET_ALL,
    }
except ImportError:
    C = {k: "" for k in ["title","ok","warn","err","info","mag","dim","rst"]}


# ============================================================
#  UTILITIES
# ============================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="Press ENTER to continue..."):
    input(f"\n{C['dim']}  {msg}{C['rst']}")

def type_print(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def line(ch="─", n=68):
    print(C['info'] + "  " + ch * n + C['rst'])

def header(title):
    clear()
    line("═")
    print(C['title'] + f"   {title.center(64)}" + C['rst'])
    line("═")
    print()

def section(title):
    print(C['mag'] + f"\n  ▸ {title}" + C['rst'])
    line("─")


# ============================================================
#  FORWARD CHAINING ENGINE
# ============================================================
class ForwardChaining:
    def __init__(self, name="Knowledge Base"):
        self.name = name
        self.facts = set()
        self.rules = []          # list of dicts
        self.trace = []          # inference log

    # ---------- Knowledge Base ----------
    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premises, conclusion):
        self.rules.append({
            "id": len(self.rules) + 1,
            "premises": list(premises),
            "conclusion": conclusion,
            "used": False,
        })

    # ---------- Display Helpers ----------
    def print_facts(self, label="Current Facts", highlight=None):
        highlight = highlight or set()
        print(C['info'] + f"  📋 {label}:" + C['rst'])
        if not self.facts:
            print(C['dim'] + "     (none)" + C['rst'])
        for f in sorted(self.facts):
            if f in highlight:
                print(f"     {C['ok']}★ {f}   ← NEW{C['rst']}")
            else:
                print(f"     {C['dim']}• {f}{C['rst']}")
        print()

    def print_rules(self):
        print(C['info'] + "  📜 Rule Base:" + C['rst'])
        for r in self.rules:
            prem = " ∧ ".join(r["premises"])
            status = C['dim'] + " [used]" + C['rst'] if r["used"] else ""
            print(f"     {C['mag']}R{r['id']}{C['rst']}:  IF  {prem}")
            print(f"           THEN  {C['ok']}{r['conclusion']}{C['rst']}{status}")
        print()

    # ---------- Inference Engine ----------
    def forward_chain(self, goal=None, animate=True, verbose=True):
        iteration = 0
        new_added = True
        prev_facts = set()

        if verbose:
            section("Inference Process")
            self.print_facts("Initial Facts")

        while new_added and iteration < 50:
            new_added = False
            iteration += 1
            this_round = []

            if verbose:
                print(C['warn'] + f"  ── Iteration {iteration} ──" + C['rst'])

            for r in self.rules:
                if r["used"]:
                    continue
                if set(r["premises"]).issubset(self.facts):
                    conc = r["conclusion"]
                    if conc not in self.facts:
                        self.facts.add(conc)
                        r["used"] = True
                        new_added = True
                        this_round.append(conc)
                        self.trace.append({
                            "iter": iteration,
                            "rule": r["id"],
                            "premises": r["premises"],
                            "conclusion": conc,
                        })

                        if verbose:
                            prem_str = " ∧ ".join(r["premises"])
                            print(f"    {C['ok']}✓{C['rst']} Rule {r['id']} fires:  "
                                  f"{prem_str}  →  {C['ok']}{conc}{C['rst']}")
                            if animate:
                                time.sleep(0.35)

            if not this_round and verbose:
                print(C['dim'] + "    (no new facts derived)" + C['rst'])

            if verbose:
                print()

            # early exit if goal reached
            if goal and goal in self.facts:
                break

        # ---------- Final summary ----------
        if verbose:
            section("Final Knowledge Base")
            self.print_facts("All Derived Facts", highlight=this_round)

            if goal:
                if goal in self.facts:
                    print(C['ok'] + f"  🎯 GOAL PROVED: {goal}{C['rst']}")
                else:
                    print(C['err'] + f"  ✗ GOAL NOT PROVED: {goal}{C['rst']}")
            print(C['dim'] + f"  Total iterations: {iteration}   |   "
                             f"Rules fired: {len(self.trace)}   |   "
                             f"Facts derived: {len(self.facts)}" + C['rst'])

        return (goal in self.facts) if goal else True

    # ---------- Show Inference Chain ----------
    def show_inference_chain(self, goal):
        section(f"Inference Chain for '{goal}'")
        chain = self._build_chain(goal, set())
        if not chain:
            print(C['err'] + "  No chain found." + C['rst'])
            return
        for i, step in enumerate(chain, 1):
            prem = " ∧ ".join(step["premises"])
            print(f"  {C['info']}Step {i}:{C['rst']}  "
                  f"{C['dim']}({prem}){C['rst']}  "
                  f"→  {C['ok']}{step['conclusion']}{C['rst']}")
        print()

    def _build_chain(self, fact, seen):
        if fact in seen:
            return []
        seen = seen | {fact}
        chain = []
        for step in self.trace:
            if step["conclusion"] == fact:
                for p in step["premises"]:
                    chain.extend(self._build_chain(p, seen))
                chain.append(step)
        return chain


# ============================================================
#  DEMO SCENARIOS
# ============================================================
def demo_weather():
    header("DEMO 1 : Weather Prediction")

    kb = ForwardChaining("Weather KB")

    print(C['warn'] + "  Scenario:" + C['rst'])
    type_print("  A weather station observes several conditions and must\n"
               "  decide whether to issue a 'Severe Weather Warning'.\n", 0.005)

    # Facts
    for f in ["dark_clouds", "high_humidity", "low_pressure", "temperature_dropping"]:
        kb.add_fact(f)

    # Rules
    kb.add_rule(["dark_clouds", "high_humidity"],           "cloudy")
    kb.add_rule(["low_pressure", "high_humidity"],          "storm_approaching")
    kb.add_rule(["cloudy", "temperature_dropping"],         "rain_likely")
    kb.add_rule(["storm_approaching", "rain_likely"],       "severe_weather_warning")
    kb.add_rule(["severe_weather_warning"],                 "stay_indoors")

    section("Knowledge Base")
    kb.print_facts("Initial Facts")
    kb.print_rules()

    pause("Press ENTER to begin inference...")
    kb.forward_chain(goal="severe_weather_warning", animate=True)

    pause()
    kb.show_inference_chain("severe_weather_warning")

    print(C['ok'] + "  ✔ Conclusion: Issue 'Severe Weather Warning'." + C['rst'])
    pause()


def demo_medical():
    header("DEMO 2 : Medical Diagnosis")

    kb = ForwardChaining("Medical KB")

    print(C['warn'] + "  Scenario:" + C['rst'])
    type_print("  A patient walks in with a set of symptoms. The system\n"
               "  must diagnose the most likely disease.\n", 0.005)

    for f in ["fever", "cough", "body_ache", "loss_of_taste"]:
        kb.add_fact(f)

    kb.add_rule(["fever", "cough"],                    "flu_symptoms")
    kb.add_rule(["body_ache", "flu_symptoms"],         "influenza")
    kb.add_rule(["loss_of_taste", "fever"],            "covid_symptoms")
    kb.add_rule(["influenza", "covid_symptoms"],       "viral_infection")
    kb.add_rule(["viral_infection"],                   "recommend_rtpcr_test")
    kb.add_rule(["recommend_rtpcr_test"],              "isolate_patient")

    section("Knowledge Base")
    kb.print_facts("Initial Facts")
    kb.print_rules()

    pause("Press ENTER to begin inference...")
    kb.forward_chain(goal="isolate_patient", animate=True)

    pause()
    kb.show_inference_chain("isolate_patient")
    pause()


def demo_student():
    header("DEMO 3 : Student Eligibility")

    kb = ForwardChaining("Student KB")

    print(C['warn'] + "  Scenario:" + C['rst'])
    type_print("  Determine if a student is eligible for a scholarship.\n", 0.005)

    for f in ["marks_above_85", "no_backlog", "attendance_above_90"]:
        kb.add_fact(f)

    kb.add_rule(["marks_above_85"],                        "academic_topper")
    kb.add_rule(["attendance_above_90"],                   "regular_student")
    kb.add_rule(["no_backlog", "regular_student"],         "clean_record")
    kb.add_rule(["academic_topper", "clean_record"],       "eligible_for_scholarship")
    kb.add_rule(["eligible_for_scholarship"],              "receive_award_letter")

    section("Knowledge Base")
    kb.print_facts("Initial Facts")
    kb.print_rules()

    pause("Press ENTER to begin inference...")
    kb.forward_chain(goal="receive_award_letter", animate=True)

    pause()
    kb.show_inference_chain("receive_award_letter")
    pause()


def demo_custom():
    header("DEMO 4 : Custom Knowledge Base")

    print(C['warn'] + "  Enter your own facts and rules.\n" + C['rst'])

    kb = ForwardChaining("Custom KB")

    # --- Facts ---
    section("Step 1 : Enter Facts")
    print(C['dim'] + "  (comma-separated, e.g.  A, B, C)\n" + C['rst'])
    facts_in = input(C['ok'] + "  Facts: " + C['rst']).strip()
    for f in facts_in.split(","):
        if f.strip():
            kb.add_fact(f.strip().lower().replace(" ", "_"))

    # --- Rules ---
    section("Step 2 : Enter Rules")
    print(C['dim'] + "  Format:  premise1,premise2 -> conclusion" + C['rst'])
    print(C['dim'] + "  Type 'done' to finish.\n" + C['rst'])

    n = 1
    while True:
        r = input(C['ok'] + f"  Rule {n}: " + C['rst']).strip()
        if r.lower() == "done":
            break
        if "->" not in r:
            print(C['err'] + "  ✗ Invalid — use '->'" + C['rst'])
            continue
        left, right = r.split("->")
        premises = [p.strip().lower().replace(" ", "_") for p in left.split(",") if p.strip()]
        conclusion = right.strip().lower().replace(" ", "_")
        kb.add_rule(premises, conclusion)
        n += 1

    # --- Goal ---
    section("Step 3 : Enter Goal (optional)")
    goal = input(C['ok'] + "  Goal (or blank to skip): " + C['rst']).strip()
    goal = goal.lower().replace(" ", "_") if goal else None

    # --- Run ---
    section("Knowledge Base")
    kb.print_facts("Initial Facts")
    kb.print_rules()

    pause("Press ENTER to begin inference...")
    kb.forward_chain(goal=goal, animate=True)

    if goal:
        pause()
        kb.show_inference_chain(goal)
    pause()


# ============================================================
#  THEORY SLIDE
# ============================================================
def show_theory():
    header("THEORY : Forward Chaining")

    print(f"""
  {C['info']}Definition:{C['rst']}
    Forward chaining is a {C['mag']}data-driven{C['rst']} inference method that starts
    with known facts and repeatedly applies inference rules to
    derive new facts until a goal is reached (or no more rules
    can fire).

  {C['info']}Algorithm:{C['rst']}
    1. Add all known facts to the working memory.
    2. For every rule, check whether all premises are satisfied.
    3. If yes → add the conclusion as a new fact.
    4. Repeat until no new fact can be derived.

  {C['info']}Characteristics:{C['rst']}
    • Data-driven (bottom-up)
    • Complete — finds all derivable facts
    • Used in expert systems, monitoring, business rules

  {C['info']}Example Rule:{C['rst']}
    IF   fever  AND  cough
    THEN flu

  {C['info']}Applications:{C['rst']}
    • Medical diagnosis          • Weather prediction
    • Network fault detection    • Loan approval systems
    • Robotics / planning        • Game AI
""")
    pause()


# ============================================================
#  MAIN MENU
# ============================================================
def main_menu():
    while True:
        clear()
        print(C['title'] + """
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║        F O R W A R D   C H A I N I N G   D E M O         ║
  ║           Artificial Intelligence — Presentation         ║
  ║                                                          ║
  ╚══════════════════════════════════════════════════════════╝
        """)
        print(C['rst'] + "  " + "─" * 60)
        print(f"   {C['ok']}[1]{C['rst']}  📖 Theory of Forward Chaining")
        print(f"   {C['ok']}[2]{C['rst']}  🌦  Demo 1 — Weather Prediction")
        print(f"   {C['ok']}[3]{C['rst']}  🏥  Demo 2 — Medical Diagnosis")
        print(f"   {C['ok']}[4]{C['rst']}  🎓  Demo 3 — Student Scholarship")
        print(f"   {C['ok']}[5]{C['rst']}  ⚙️   Demo 4 — Custom Knowledge Base")
        print(f"   {C['ok']}[6]{C['rst']}  🚪  Exit")
        print("  " + "─" * 60)

        ch = input(C['info'] + "  ➤ Choose an option: " + C['rst']).strip()

        if   ch == "1": show_theory()
        elif ch == "2": demo_weather()
        elif ch == "3": demo_medical()
        elif ch == "4": demo_student()
        elif ch == "5": demo_custom()
        elif ch == "6":
            print(C['ok'] + "\n  Thank you! End of presentation.\n" + C['rst'])
            break
        else:
            print(C['err'] + "  ✗ Invalid choice." + C['rst'])
            time.sleep(0.7)


# ============================================================
#  ENTRY POINT
# ============================================================
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(C['warn'] + "\n\n  Demo interrupted. Bye!\n" + C['rst'])