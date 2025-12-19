# User Docs (LaTeX template)

Use this directory to build user-facing guides as PDFs. The template below is SRMS-free and ready to customize.

## Files
- `user_doc_template.tex`: minimal LaTeX template for a user guide.

## How to build
1) Ensure you have a LaTeX toolchain installed (e.g., `pdflatex`).
2) From the template root:
   ```bash
   cd DOCS/user_docs
   pdflatex user_doc_template.tex
   ```
3) Open `user_doc_template.pdf` once generated.

## Notes
- Keep content PII-free by default; redact sensitive examples if your project requires them.
- Update title/author/date and sections to match your project.
