# Portfolio maintenance — October 1, 2026

Original midterm: November 2, 2025, by Daniel Pena Arias.

- Replaced repeated recursive menu calls with a loop so long sessions do not accumulate function calls.
- Returned normally when quitting and removed unused imports/data.
- Added an import guard so tests can load the module without prompting.
- Used `time.monotonic()` for the elapsed dance duration.
- Added run instructions, control reference, and regression tests.

Portfolio preparation and these focused repairs were assisted by ChatGPT. The original simulation behavior and student-written functions were retained. The original script in Downloads was preserved.
