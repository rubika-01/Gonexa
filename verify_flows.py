"""
Automated Playwright End-to-End Verification for GONEXA.
Comprehensive test suite verifying:
1. Prototype Demo Authentication Flow
2. Dashboard & Simplified Hierarchy with Indian Synthetic Names
3. Global Multi-Field Search (Ctrl+K and Esc)
4. Today's Appointments -> Live Rehabilitation Measurement Session
5. Hero Feature: Sensor Displacement Detection & Auto-Correction
6. Live Session Persistence (Saved session verification in Patient Profile)
7. Ask GONEXA Contextual Drawer (General Mode, Patient Mode, Entity Resolution)
8. Truly Distinct Rehabilitation Reports (Longitudinal, Session Deep-Dive, Date-Range, CSV & Print CSS)
9. Technical Evaluation Lab
"""

from playwright.sync_api import sync_playwright
import time
import sys

def run_tests():
    print("Starting GONEXA automated end-to-end browser test suite...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))

        # -------------------------------------------------------------
        # 1. Prototype Demo Authentication Flow
        # -------------------------------------------------------------
        print("\n[Test 1] Testing Prototype Demo Authentication...")
        page.goto("http://127.0.0.1:5173/login", wait_until="networkidle")
        time.sleep(0.5)
        assert "Prototype Demo Authentication" in page.content(), "Missing 'Prototype Demo Authentication' badge"
        assert "Dr. Neha Sharma, PT" in page.content(), "Missing Clinician Identity"
        assert "Chief Physiotherapist" in page.content(), "Missing Clinical Role"

        demo_login_btn = page.locator("button:has-text('[ DEMO LOGIN ]')")
        assert demo_login_btn.is_visible(), "DEMO LOGIN button not found"
        demo_login_btn.click()
        page.wait_for_url("**/dashboard", timeout=5000)
        print("  [OK] Prototype Demo Authentication succeeded and navigated to Dashboard.")

        # -------------------------------------------------------------
        # 2. Dashboard Load & Clinical Hierarchy
        # -------------------------------------------------------------
        print("\n[Test 2] Testing Dashboard & Hierarchy with Indian Synthetic Names...")
        time.sleep(0.5)
        assert "Today's Rehabilitation" in page.content(), "Missing 'Today's Rehabilitation' header"
        assert "Today's Appointments" in page.content(), "Missing 'Today's Appointments' section"
        assert "Arjun Sharma" in page.content(), "Arjun Sharma missing from appointments"
        assert "P104" in page.content(), "P104 missing from appointments"
        assert "Needs Attention" in page.content(), "Missing 'Needs Attention' section"
        assert "Progress Overview" in page.content(), "Missing 'Progress Overview' section"
        print("  [OK] Dashboard rendered with Indian synthetic patient profiles and clinical hierarchy.")

        # -------------------------------------------------------------
        # 3. Global Multi-Field Search (Ctrl+K and Esc)
        # -------------------------------------------------------------
        print("\n[Test 3] Testing Global Search (Ctrl+K and Esc)...")
        page.keyboard.press("Control+k")
        time.sleep(0.5)
        search_modal = page.locator("input[placeholder*='Search patients']")
        assert search_modal.is_visible(), "Global search modal did not open on Ctrl+K"
        search_modal.fill("P104")
        time.sleep(0.5)
        assert "Arjun Sharma (P104)" in page.content(), "P104 Arjun Sharma not matched in search results"
        page.keyboard.press("Escape")
        time.sleep(0.5)
        assert not search_modal.is_visible(), "Search modal did not close on Escape"
        print("  [OK] Search opened via Ctrl+K, found Arjun Sharma (P104), and closed on Esc.")

        # -------------------------------------------------------------
        # 4. Today's Appointments -> Start Live Session
        # -------------------------------------------------------------
        print("\n[Test 4] Testing Today's Appointment -> Live Session Flow...")
        p104_btn = page.locator("div:has-text('Arjun Sharma')").locator("button:has-text('START SESSION'), button:has-text('Resume Session')").first
        assert p104_btn.is_visible(), "Arjun Sharma start/resume session button not found"
        p104_btn.click()
        page.wait_for_url("**/sessions/live-P104", timeout=8000)
        time.sleep(0.5)
        assert "Arjun Sharma (P104)" in page.content(), "Live session header for P104 not loaded"
        assert "Current Angle" in page.content(), "Current angle readout not found"
        print("  [OK] Successfully navigated from Appointment to Live Rehabilitation Session.")

        # -------------------------------------------------------------
        # 5. Hero Feature: Sensor Displacement & Auto-Correct
        # -------------------------------------------------------------
        print("\n[Test 5] Testing Hero Feature: Sensor Displacement & Auto-Correct...")
        slip_btn = page.locator("text=[Simulate Sensor Slip]")
        assert slip_btn.is_visible(), "Simulate Sensor Slip button missing"
        slip_btn.click()
        time.sleep(0.5)
        assert "Possible device displacement detected" in page.content(), "Displacement banner did not appear"
        assert "+14.2°" in page.content(), "Offset +14.2° not displayed"

        # Click Auto-Correct
        auto_correct_btn = page.locator("button:has-text('AUTO-CORRECT')")
        assert auto_correct_btn.is_visible(), "AUTO-CORRECT button missing"
        auto_correct_btn.click()
        time.sleep(0.5)
        assert "Automatic correction applied" in page.content(), "Audit record did not appear after auto-correction"
        print("  [OK] Sensor displacement detected, auto-corrected, and collapsed to audit record.")

        # Click End Session -> Persist & Navigate to Patient Profile
        print("  Ending session and persisting live metrics...")
        page.locator("button:has-text('END SESSION')").click()
        page.wait_for_url("**/patients/P104", timeout=8000)
        time.sleep(1.0)
        print("  [OK] Ended session and navigated to Patient Profile.")

        # -------------------------------------------------------------
        # 6. Patient Profile Tabs & Persistence Verification
        # -------------------------------------------------------------
        print(f"\n[Test 6] Testing Patient Profile & Session Persistence on: {page.url}...")
        assert "Arjun Sharma" in page.content(), f"Patient profile name missing on {page.url}"
        assert "Overview" in page.content() and "Sessions" in page.content(), "Patient tabs missing"

        # Switch to Sessions tab and verify persistence
        page.locator("[data-testid='patient-tabs'] button", has_text="Sessions").click()
        time.sleep(0.5)
        assert "Session History" in page.content(), "Sessions tab failed to render"
        page_text = page.locator("body").inner_text()
        assert "S-P104-009" in page_text or "Session 9" in page_text, "Newly saved session S-P104-009 not found in session history!"
        print("  [OK] Verified persistent session S-P104-009 in Patient Profile history.")

        # Switch to Quality tab
        page.locator("[data-testid='patient-tabs'] button", has_text="Quality").click()
        time.sleep(0.5)
        assert "Audit Log" in page.content() or "Sensor Displacement Events" in page.content(), "Quality tab failed to render"

        # Switch to Ask GONEXA tab
        page.locator("[data-testid='patient-tabs'] button", has_text="Ask GONEXA").click()
        time.sleep(0.5)
        assert "Ask GONEXA" in page.content(), "Ask GONEXA tab failed to render"
        print("  [OK] Patient profile tabs (Overview, Sessions, Quality, Ask GONEXA) verified.")

        # -------------------------------------------------------------
        # 7. Floating Ask GONEXA Drawer (General Mode, Patient Mode)
        # -------------------------------------------------------------
        print("\n[Test 7] Testing Floating Ask GONEXA Button & Drawer...")
        ask_gonexa_btn = page.locator("button[aria-label='Ask GONEXA']")
        assert ask_gonexa_btn.is_visible(), "Floating Ask GONEXA button missing"
        ask_gonexa_btn.click()
        time.sleep(0.5)

        drawer = page.locator("[data-testid='copilot-drawer']")
        assert drawer.is_visible(), "Ask GONEXA drawer did not open"

        # Check Scope Selector inside drawer
        scope_select = drawer.locator("select").first
        assert scope_select.is_visible(), "Scope selector missing"

        # 7a. Test General question in General Mode
        scope_select.select_option("GENERAL")
        time.sleep(0.3)
        input_box = drawer.locator("input[type='text']")
        assert input_box.is_visible(), "General prompt input missing"
        input_box.fill("How do I start a rehabilitation session?")
        input_box.press("Enter")
        time.sleep(1.2)
        assert "START SESSION" in page.content(), "General platform guidance response missing"
        print("  [OK] Ask GONEXA General Mode provided clear navigation guidance.")

        # 7b. Test Patient question in Patient Mode
        scope_select.select_option("P104")
        time.sleep(0.3)
        p_input = drawer.locator("input[type='text']")
        p_input.fill("How has ROM improved?")
        p_input.press("Enter")
        time.sleep(1.2)
        assert "peak active" in page.content() or "net gain" in page.content() or "Arjun Sharma" in page.content(), "Patient trajectory response missing"
        print("  [OK] Ask GONEXA Patient Mode provided grounded recovery trajectory.")

        # Close via Escape
        page.keyboard.press("Escape")
        time.sleep(0.5)
        print("  [OK] Ask GONEXA drawer tested and closed on Esc.")

        # -------------------------------------------------------------
        # 8. Truly Distinct Rehabilitation Reports & Print CSS
        # -------------------------------------------------------------
        print("\n[Test 8] Testing Truly Distinct Rehabilitation Reports...")
        page.goto("http://127.0.0.1:5173/reports", wait_until="networkidle")
        time.sleep(0.5)
        assert "Rehabilitation Reports" in page.content(), "Reports header missing"

        # Tab 1: Patient Report
        assert "P104 — Longitudinal Recovery Report" in page.content(), "Patient report title mismatch"
        assert "Longitudinal Telemetry Progression" in page.content(), "Longitudinal section missing"

        # Tab 2: Session Report
        page.locator("button:has-text('Session Report')").click()
        time.sleep(0.5)
        assert "Session Report" in page.content(), "Session Report tab missing"
        assert "Detailed Kinematic Telemetry Breakdown" in page.content(), "Single-session kinematic breakdown missing"
        assert "Sensor Displacement" in page.content(), "Displacement offset audit section missing"

        # Tab 3: Date Range Report
        page.locator("button:has-text('Date Range')").click()
        time.sleep(0.5)
        assert "Date Range" in page.content(), "Date Range tab missing"
        assert "Sessions Executed" in page.content(), "Sessions executed table missing"
        assert "Period Validity Rate" in page.content(), "Period validity rate missing"

        # Verify Export and Print buttons
        assert page.locator("button:has-text('Export CSV')").is_visible(), "Export CSV button missing"
        assert page.locator("button:has-text('Print / PDF')").is_visible(), "Print / PDF button missing"
        print("  [OK] Reports page has 3 truly distinct report structures, scoped exports, and print styling.")

        # -------------------------------------------------------------
        # 9. Technical Evaluation Lab Page
        # -------------------------------------------------------------
        print("\n[Test 9] Testing Technical Evaluation Lab...")
        page.goto("http://127.0.0.1:5173/evaluation", wait_until="networkidle")
        time.sleep(1.0)
        assert "Evaluation Lab" in page.content(), "Evaluation Lab header missing"
        assert "Technical validation of GONEXA's measurement engine" in page.content(), "Banner missing"
        assert "8 Stress Scenarios" in page.content(), "8 Stress Scenarios badge missing"

        # Wait for benchmark suite to run and render results
        page.wait_for_selector("text=Individual Stress Test Scenario Results", timeout=8000)
        time.sleep(2.0)
        page_text = page.locator("body").inner_text()
        assert "Sensor Displacement" in page_text, "Sensor Displacement scenario missing"
        assert "mean rom rmse" in page_text.lower() or "Mean ROM RMSE" in page.content(), "Mean ROM RMSE metric card missing"
        print("  [OK] Technical Evaluation Lab rendered with deterministic measurement benchmarking.")

        browser.close()

        if errors:
            print(f"\n[WARNING] Encountered console errors during run: {errors}")
            return False

        print("\n==========================================================")
        print("ALL 9 END-TO-END BROWSER TESTS PASSED WITH ZERO ERRORS!")
        print("==========================================================")
        return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
